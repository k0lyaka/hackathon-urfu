import logging

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from urfu.infrastructure.ioc import get_container
from urfu.presentation.web.routers import setup_routers


def create_app() -> FastAPI:
    logging.basicConfig(level=logging.INFO)

    app = FastAPI(
        title="Urfu Hackathon Bot",
        description="A bot for the Urfu Hackathon",
        version="1.0.0",
    )

    container = get_container()

    setup_dishka(container, app)
    setup_routers(app)

    return app
