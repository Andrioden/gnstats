import os
from typing import Union
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from api.game_nights import router as game_nights_router
from api.users import router as users_router

from fastapi import FastAPI
from fastapi import Request
from starlette.responses import RedirectResponse

import os
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from authlib.integrations.starlette_client import OAuthError


app = FastAPI(title="GN Stats Api")
app.include_router(game_nights_router, tags=["Game Nights"], prefix="/api/gamenights")
app.include_router(users_router, tags=["Users"], prefix="/api/users")


# Set up OAuth
oauth = OAuth(Config(environ={'GOOGLE_CLIENT_ID': os.environ['GOOGLE_CLIENT_ID'], 'GOOGLE_CLIENT_SECRET': os.environ['GOOGLE_CLIENT_SECRET']}))
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)
app.add_middleware(SessionMiddleware, secret_key=os.environ['SECRET_KEY'])


@app.route('/login')
async def login(request: Request):
    # redirect_uri = request.url_for('auth')  # This creates the url for the /auth endpoint
    # return await oauth.google.authorize_redirect(request, redirect_uri)

    google = oauth.create_client('google')
    redirect_uri = request.url_for('auth')
    return await google.authorize_redirect(request, redirect_uri)


@app.route('/auth')
async def auth(request: Request):
    google = oauth.create_client('google')
    token = await google.authorize_access_token(request)
    # do something with the token and userinfo
    request.session['user'] = token["userinfo"]
    print(token)
    return RedirectResponse(url='/')
    # return '...'

    # try:
    #     access_token = await oauth.google.authorize_access_token(request)
    # except OAuthError:
    #     return RedirectResponse(url='/')
    # print(request)
    # user_data = await oauth.google.parse_id_token(request, access_token)
    # request.session['user'] = dict(user_data)
    # return RedirectResponse(url='/')


@app.get('/')
def public(request: Request):
    user = request.session.get('user')
    if user:
        name = user.get('name')
        return HTMLResponse(f'<p>Hello {name} {user}!</p><a href=/logout>Logout</a>')
    return HTMLResponse('<a href=/login>Login</a>')


@app.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')