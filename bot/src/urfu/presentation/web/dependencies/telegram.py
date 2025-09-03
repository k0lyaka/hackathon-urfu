from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Header, HTTPException

from urfu.infrastructure.settings import AppSettings


@inject
async def validate_telegram_hook(
    x_telegram_bot_api_secret_token: Annotated[str, Header()],
    settings: FromDishka[AppSettings],
) -> None:
    if settings.bot.secret.get_secret_value() != x_telegram_bot_api_secret_token:
        raise HTTPException(status_code=401, detail="Invalid token")
