from typing import Protocol

from urfu.domain.dto.specialization import (
    CreateSpecializationDTO,
    UpdateSpecializationDTO,
)
from urfu.domain.entities.specialization import SpecializationEntity
from urfu.domain.value_objects.specialization import SpecializationId


class SpecializationReader(Protocol):
    async def with_id(
        self, specialization_id: SpecializationId
    ) -> SpecializationEntity: ...

    async def get_all_tags(self) -> set[str]: ...


class SpecializationWriter(Protocol):
    async def save(self, dto: CreateSpecializationDTO) -> SpecializationEntity: ...


class SpecializationUpdater(Protocol):
    async def update(self, dto: UpdateSpecializationDTO) -> SpecializationEntity: ...
