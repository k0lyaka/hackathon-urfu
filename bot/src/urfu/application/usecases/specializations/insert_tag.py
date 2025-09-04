from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.common.uow import UnitOfWork
from urfu.application.contracts.specializations.insert_tag import InsertTagsRequest
from urfu.application.gateways.specialization import (
    SpecializationReader,
    SpecializationUpdater,
)
from urfu.domain.dto.specialization import Specialization, UpdateSpecializationDTO
from urfu.domain.entities.user import UserEntity
from urfu.domain.value_objects.specialization import SpecializationId
from urfu.infrastructure.database.mappers.specialization import (
    specialization_entity_to_dto,
)
from urfu.infrastructure.settings import AppSettings


@dataclass
class InsertTags(Interactor[InsertTagsRequest, Specialization]):
    id_provider: IdProvider[UserEntity]
    specialization_reader: SpecializationReader
    specialization_updater: SpecializationUpdater
    settings: AppSettings
    uow: UnitOfWork

    async def __call__(self, data: InsertTagsRequest) -> Specialization:
        user = await self.id_provider.get_user()
        user.has_access(self.settings.bot.admin_ids)

        async with self.uow:
            specialization = await self.specialization_reader.with_id(
                SpecializationId(data.specialization_id)
            )
            specialization = await self.specialization_updater.update(
                UpdateSpecializationDTO(
                    id=specialization.id,
                    tags=specialization.tags + data.tags,
                )
            )
            await self.uow.commit()

        return specialization_entity_to_dto(specialization)
