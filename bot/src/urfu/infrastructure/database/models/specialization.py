from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import ARRAY

from urfu.domain.entities.specialization import SpecializationEntity
from urfu.infrastructure.database.models.base import BaseModel
from urfu.infrastructure.database.models.specialization_score import (
    SpecializationScoreModel,
)


class SpecializationModel(BaseModel):
    __tablename__ = "specializations"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()
    code: Mapped[str] = mapped_column()
    institute: Mapped[str] = mapped_column()

    tags: Mapped[list[str]] = mapped_column(ARRAY(String()), server_default="{}")

    scores: Mapped[list[SpecializationScoreModel]] = relationship()

    def to_entity(self) -> SpecializationEntity:
        return SpecializationEntity.model_validate(self)
