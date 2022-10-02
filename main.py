from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from api.app import app

app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# def index():
#     return FileResponse('index.html')


@app.get("/favicon.ico")
def favicon():
    return FileResponse('favicon.ico')
