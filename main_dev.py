from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from api.app import app

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse("static/index.html")


@app.get("/favicon.ico", include_in_schema=False)
def favicon() -> FileResponse:
    return FileResponse("static/favicon.ico")
