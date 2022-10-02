from starlette.staticfiles import StaticFiles

from api.app import app

app.mount("/static", StaticFiles(directory="static"), name="static")