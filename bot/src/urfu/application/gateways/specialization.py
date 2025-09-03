from typing import Protocol

from urfu.domain.dto.specialization import (
    CreateSpecializationDTO,
    UpdateSpecializationDTO,
)
from urfu.domain.entities.specialization import SpecializationEntity
from urfu.domain.entities.user import UserEntity
from urfu.domain.value_objects.specialization import SpecializationId


class SpecializationReader(Protocol):
    async def with_id(
        self, specialization_id: SpecializationId
    ) -> SpecializationEntity: ...

    async def get_all_tags(self) -> set[str]: ...

    async def get_all_with_scores(self) -> list[SpecializationEntity]: ...

    async def get_suitable_for_user(
        self, user: UserEntity
    ) -> list[SpecializationEntity]: ...


class SpecializationWriter(Protocol):
    async def save(self, dto: CreateSpecializationDTO) -> SpecializationEntity: ...


class SpecializationUpdater(Protocol):
    async def update(self, dto: UpdateSpecializationDTO) -> SpecializationEntity: ...
