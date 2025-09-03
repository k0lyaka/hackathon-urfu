import logging

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from urfu.infrastructure.ioc import get_container
from urfu.presentation.web.routers import setup_routers
from urfu.presentation.web.routers.errors import setup_error_handler


def create_app() -> FastAPI:
    logging.basicConfig(level=logging.INFO)

    app = FastAPI(
        title="Urfu Hackathon Bot",
        description="A bot for the Urfu Hackathon",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    container = get_container()

    setup_dishka(container, app)
    setup_error_handler(app)
    setup_routers(app)

    return app
