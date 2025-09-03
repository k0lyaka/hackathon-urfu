from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from urfu.domain.entities.exam_score import ExamScoreEntity
from urfu.domain.enums.subject import SubjectEnum
from urfu.infrastructure.database.models.base import BaseModel

if TYPE_CHECKING:
    from .user import UserModel


class ExamScoreModel(BaseModel):
    __tablename__ = "exam_scores"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="exam_scores")

    subject: Mapped[SubjectEnum] = mapped_column(ENUM(SubjectEnum, name="subject_enum"))
    score: Mapped[int] = mapped_column()
    year: Mapped[int] = mapped_column()

    def to_entity(self) -> ExamScoreEntity:
        return ExamScoreEntity.model_validate(self)
