from typing import Protocol

from urfu.domain.dto.specialization import CreateSpecializationScoreDTO
from urfu.domain.entities.specialization_score import SpecializationScoreEntity
from urfu.domain.value_objects.specialization import (
    SpecializationId,
    SpecializationScoreId,
)


class SpecializationScoreReader(Protocol):
    async def with_id(
        self, specialization_score_id: SpecializationScoreId
    ) -> SpecializationScoreEntity: ...

    async def with_specialization_id(
        self, specialization_id: SpecializationId
    ) -> list[SpecializationScoreEntity]: ...


class SpecializationScoreWriter(Protocol):
    async def save(
        self, dto: CreateSpecializationScoreDTO
    ) -> SpecializationScoreEntity: ...

    async def delete_scores(self, specialization_id: SpecializationId) -> None: ...
