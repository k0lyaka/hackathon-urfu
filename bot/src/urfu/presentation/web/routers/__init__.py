from fastapi import FastAPI

from . import hooks, profile, specialization


def setup_routers(app: FastAPI) -> None:
    app.include_router(hooks.router)
    app.include_router(profile.router)
    app.include_router(specialization.router)
