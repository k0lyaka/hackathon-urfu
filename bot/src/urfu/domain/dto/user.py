from pydantic import BaseModel

from urfu.domain.value_objects.user import TelegramId, UserId


class CreateUserDTO(BaseModel):
    telegram_id: TelegramId
    username: str | None


class UpdateUserDTO(BaseModel):
    id: UserId
    username: str | None = None
