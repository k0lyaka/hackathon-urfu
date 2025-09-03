from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.contracts.specializations.get_raiting import (
    GetSpecializationsRequest,
)
from urfu.application.gateways.specialization import SpecializationReader
from urfu.domain.dto.specialization import Specialization
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.database.mappers.specialization import (
    specialization_entity_to_dto,
)


@dataclass
class GetSpecializations(Interactor[GetSpecializationsRequest, list[Specialization]]):
    id_provider: IdProvider[UserEntity]
    specialization_reader: SpecializationReader

    async def __call__(self, _: GetSpecializationsRequest) -> list[Specialization]:
        user = await self.id_provider.get_user()

        suitable_specializations = await (
            self.specialization_reader.get_suitable_for_user(user)
        )

        return [specialization_entity_to_dto(spec) for spec in suitable_specializations]
