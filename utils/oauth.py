import os
from functools import lru_cache

from authlib.integrations.starlette_client import OAuth, StarletteOAuth2App
from starlette.config import Config


@lru_cache
def google_oauth_client() -> StarletteOAuth2App:
    oauth = OAuth(
        Config(
            environ={
                "GOOGLE_CLIENT_ID": os.environ["GOOGLE_CLIENT_ID"],
                "GOOGLE_CLIENT_SECRET": os.environ["GOOGLE_CLIENT_SECRET"],
            }
        )
    )
    return oauth.register(
        name="google",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
    )
