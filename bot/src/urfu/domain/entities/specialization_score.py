from urfu.domain.entities.base import BaseEntity
from urfu.domain.value_objects.specialization import (
    SpecializationId,
    SpecializationScoreId,
)


class SpecializationScoreEntity(BaseEntity[SpecializationScoreId]):
    specialization_id: SpecializationId
    minimal_score: int
    seats: int
    year: int
