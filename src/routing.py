import os

from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from instance.const import PUBLIC_PATH
from src.templating import HttpBase


async def index(request: Request):
    return await HttpBase(request=request).response()


routes = [
    Route("/", endpoint=index, methods=["GET", "POST"], name="index"),
    Route("/{path}", endpoint=index, methods=["GET", "POST"], name="index"),
    Route("/panel", endpoint=index, methods=["GET", "POST"], name="panel"),
    Route("/panel/{path}", endpoint=index, methods=["GET", "POST"], name="panel"),
    Mount("/static", app=StaticFiles(directory=os.path.join(PUBLIC_PATH, "static")), name="static"),
]
