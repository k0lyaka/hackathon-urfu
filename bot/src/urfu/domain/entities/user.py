from pydantic import computed_field

from urfu.domain.entities.base import BaseEntity
from urfu.domain.entities.exam_score import ExamScoreEntity
from urfu.domain.errors.auth import UnauthorizedError
from urfu.domain.value_objects.user import TelegramId, UserId


class UserEntity(BaseEntity[UserId]):
    telegram_id: TelegramId
    username: str | None

    interest_tags: list[str]
    full_interest_text: str | None

    exam_scores: list[ExamScoreEntity]

    @computed_field
    @property
    def is_profile_created(self) -> bool:
        return self.full_interest_text is not None and len(self.exam_scores) >= 2

    def has_access(self, admin_ids: list[int]) -> None:
        if self.telegram_id.value not in admin_ids:
            raise UnauthorizedError
