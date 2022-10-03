import os
from typing import Union
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api.game_nights import router as game_nights_router
from api.users import router as users_router
from api.auth import router as auth_router, SESSION_VAR_GOOGLE_USER

from fastapi import FastAPI
from fastapi import Request
from starlette.responses import RedirectResponse

import os
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from authlib.integrations.starlette_client import OAuthError

# App init
app = FastAPI(title="GN Stats Api")
app.include_router(game_nights_router, tags=["Game Nights"], prefix="/api/gamenights")
app.include_router(auth_router, tags=["Auth"], prefix="/api/auth")
app.include_router(users_router, tags=["Users"], prefix="/api/users")
app.add_middleware(SessionMiddleware, secret_key=os.environ['SECRET_KEY'])


# @app.get('/')
# def public(request: Request):
#     google_user = request.session.get(SESSION_VAR_GOOGLE_USER)
#     if google_user:
#         return HTMLResponse(f'<p>Hello {google_user}!</p><a href=/api/auth/logout/>Logout</a>')
#     return HTMLResponse('<a href=/api/auth/login/>Login</a>')
