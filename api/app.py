import os
from typing import Union
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from api.gamenights import router as gamenights_router

from fastapi import FastAPI

app = FastAPI(title="GN Stats Api")
app.include_router(gamenights_router, tags=["Gamenights"], prefix="/gamenights")
