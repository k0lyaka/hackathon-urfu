from typing import Protocol

from urfu.domain.dto.user import CreateUserDTO, UpdateUserDTO
from urfu.domain.entities.user import UserEntity
from urfu.domain.value_objects.user import TelegramId, UserId


class UserReader(Protocol):
    async def with_id(self, user_id: UserId) -> UserEntity: ...
    async def with_telegram_id(self, telegram_id: TelegramId) -> UserEntity: ...


class UserWriter(Protocol):
    async def save(self, dto: CreateUserDTO) -> UserEntity: ...


class UserUpdater(Protocol):
    async def update(self, dto: UpdateUserDTO) -> UserEntity: ...
