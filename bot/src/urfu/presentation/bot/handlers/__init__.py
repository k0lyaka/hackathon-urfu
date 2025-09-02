from aiogram import Router

from . import command


def setup_handlers(router: Router) -> None:
    router.include_routers(
        command.router,
    )
