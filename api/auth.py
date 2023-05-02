"""
The user auth flow:
1. The user calls our /login/, a login url is created
2. User redirected to a Google hosted login page
3. User logs inn to their Google account
4. Google redirects user back to our /callback/
5. We call Google service and validates callback data
6. We store a validated data in the user session
7. Starlette middleware validate on every request user session based on crypto magic and SECRET_KEY
"""

from authlib.integrations.starlette_client import StarletteOAuth2App
from fastapi import APIRouter, Depends, Request
from starlette.responses import RedirectResponse

from api.session import SESSION_VAR_GOOGLE_ACCOUNT
from models.external.google import GoogleAccount
from utils.oauth import google_oauth_client

router = APIRouter()


@router.get("/login/")
async def login(
    request: Request,
    oauth_client: StarletteOAuth2App = Depends(google_oauth_client),
) -> RedirectResponse:
    redirect_uri = request.url_for("callback")
    return await oauth_client.authorize_redirect(request, str(redirect_uri))


@router.get("/callback/")
async def callback(
    request: Request,
    oauth_client: StarletteOAuth2App = Depends(google_oauth_client),
) -> RedirectResponse:
    token = await oauth_client.authorize_access_token(request)
    request.session[SESSION_VAR_GOOGLE_ACCOUNT] = GoogleAccount.parse_obj(token["userinfo"]).dict()
    return RedirectResponse(url="/")


@router.get("/logout/")
def logout(request: Request) -> RedirectResponse:
    request.session.pop(SESSION_VAR_GOOGLE_ACCOUNT, None)
    return RedirectResponse(url="/")
