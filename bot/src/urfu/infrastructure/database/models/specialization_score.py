from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from urfu.domain.entities.specialization_score import SpecializationScoreEntity
from urfu.infrastructure.database.models.base import BaseModel

if TYPE_CHECKING:
    from urfu.infrastructure.database.models.specialization import SpecializationModel


class SpecializationScoreModel(BaseModel):
    __tablename__ = "specialization_scores"

    id: Mapped[int] = mapped_column(primary_key=True)

    specialization_id: Mapped[int] = mapped_column(ForeignKey("specializations.id"))
    specialization: Mapped["SpecializationModel"] = relationship(
        back_populates="scores"
    )

    minimal_score: Mapped[int] = mapped_column()
    seats: Mapped[int] = mapped_column()

    year: Mapped[int] = mapped_column()

    def to_entity(self) -> SpecializationScoreEntity:
        return SpecializationScoreEntity.model_validate(self)
