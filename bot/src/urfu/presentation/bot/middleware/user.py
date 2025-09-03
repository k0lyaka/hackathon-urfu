from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from dishka import AsyncContainer
from dishka.integrations.aiogram import CONTAINER_NAME

from urfu.application.contracts.users.create_or_update import CreateOrUpdateUserRequest
from urfu.application.usecases.users.create_or_update import CreateOrUpdateUser
from urfu.domain.value_objects.user import TelegramId


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        telegram_user: User = data["event_from_user"]
        container: AsyncContainer = data[CONTAINER_NAME]

        create_or_update = await container.get(CreateOrUpdateUser)
        data["user"] = await create_or_update(
            CreateOrUpdateUserRequest(
                telegram_id=TelegramId(telegram_user.id),
                username=telegram_user.username,
            )
        )

        return await handler(event, data)
