from fastapi import FastAPI

from . import hooks


def setup_routers(app: FastAPI) -> None:
    app.include_router(hooks.router)
