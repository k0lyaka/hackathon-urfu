from urfu.domain.entities.base import BaseEntity
from urfu.domain.entities.specialization_score import SpecializationScoreEntity
from urfu.domain.value_objects.specialization import SpecializationId


class SpecializationEntity(BaseEntity[SpecializationId]):
    name: str
    code: str
    institute: str
    tags: list[str]
    scores: list[SpecializationScoreEntity]
