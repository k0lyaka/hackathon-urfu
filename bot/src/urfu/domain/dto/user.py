from pydantic import BaseModel

from urfu.domain.dto.exam_score import ExamScoreDTO
from urfu.domain.value_objects.user import TelegramId, UserId


class UserDTO(BaseModel):
    id: int
    telegram_id: int

    username: str | None
    interest_tags: list[str] | None = None
    full_interest_text: str | None = None

    exam_scores: list[ExamScoreDTO]


class CreateUserDTO(BaseModel):
    telegram_id: TelegramId
    username: str | None


class UpdateUserDTO(BaseModel):
    id: UserId

    username: str | None = None
    interest_tags: list[str] | None = None
    full_interest_text: str | None = None
