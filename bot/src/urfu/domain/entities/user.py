from urfu.domain.entities.base import BaseEntity
from urfu.domain.value_objects.user import TelegramId, UserId


class UserEntity(BaseEntity[UserId]):
    telegram_id: TelegramId
    username: str | None

    interest_tags: list[str]
    full_interest_text: str | None
