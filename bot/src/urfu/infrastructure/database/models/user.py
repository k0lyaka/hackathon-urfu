from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.database.models.base import BaseModel
from urfu.infrastructure.database.models.exam_score import ExamScoreModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    telegram_id: Mapped[int] = mapped_column(BigInteger(), unique=True, index=True)
    username: Mapped[str | None] = mapped_column(nullable=True)

    exam_scores: Mapped[list[ExamScoreModel]] = relationship()

    def to_entity(self) -> UserEntity:
        return UserEntity.model_validate(self)
