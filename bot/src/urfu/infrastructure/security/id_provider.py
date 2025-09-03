import base64
from dataclasses import dataclass

from fastapi import Request

from urfu.application.common.security.id_provider import IdProvider
from urfu.application.common.security.token_processor import TokenProcessor
from urfu.application.gateways.user import UserReader
from urfu.domain.entities.user import UserEntity
from urfu.domain.value_objects.user import TelegramId
from urfu.infrastructure.errors.security import UnauthenticatedError
from urfu.infrastructure.settings import AppSettings


@dataclass
class UserIdProvider(IdProvider[UserEntity]):
    user_reader: UserReader

    request: Request

    token_processor: TokenProcessor
    settings: AppSettings

    async def get_user(self) -> UserEntity:
        token = self.request.headers.get("Authorization")

        if not token:
            raise UnauthenticatedError

        # TODO: refactor this part, so dirty...
        token = base64.b64decode(token).decode()

        telegram_id = self.token_processor.verify(
            token, bot_id=self.settings.bot.bot_id
        )

        return await self.user_reader.with_telegram_id(TelegramId(telegram_id))
