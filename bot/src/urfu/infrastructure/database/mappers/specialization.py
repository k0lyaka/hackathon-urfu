from urfu.domain.dto.specialization import Specialization, SpecializationScore
from urfu.domain.entities.specialization import SpecializationEntity
from urfu.domain.entities.specialization_score import SpecializationScoreEntity


def specialization_score_entity_to_dto(
    entity: SpecializationScoreEntity,
) -> SpecializationScore:
    return SpecializationScore(
        id=entity.id.value,
        minimal_score=entity.minimal_score,
        year=entity.year,
    )


def specialization_entity_to_dto(entity: SpecializationEntity) -> Specialization:
    return Specialization(
        id=entity.id.value,
        name=entity.name,
        code=entity.code,
        institute=entity.institute,
        tags=entity.tags,
        scores=[specialization_score_entity_to_dto(score) for score in entity.scores],
    )
