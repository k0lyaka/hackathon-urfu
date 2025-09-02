from pydantic import BaseModel

from urfu.domain.value_objects.user import TelegramId


class CreateOrUpdateUserRequest(BaseModel):
    telegram_id: TelegramId
    username: str | None
