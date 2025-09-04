from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.common.uow import UnitOfWork
from urfu.application.contracts.specializations.create import (
    CreateSpecializationRequest,
)
from urfu.application.gateways.specialization import (
    SpecializationReader,
    SpecializationWriter,
)
from urfu.application.usecases.specializations_scores.create import (
    CreateSpecializationScoresBatch,
)
from urfu.domain.dto.specialization import (
    CreateSpecializationDTO,
    CreateSpecializationScoreDTO,
    Specialization,
)
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.adapters.openai.client import AiAdapter
from urfu.infrastructure.database.mappers.specialization import (
    specialization_entity_to_dto,
)
from urfu.infrastructure.settings import AppSettings


@dataclass
class CreateSpecialization(Interactor[CreateSpecializationRequest, Specialization]):
    id_provider: IdProvider[UserEntity]
    settings: AppSettings

    specialization_writer: SpecializationWriter
    specialization_reader: SpecializationReader

    ai_adapter: AiAdapter
    uow: UnitOfWork

    create_specialization_scores: CreateSpecializationScoresBatch

    async def __call__(self, data: CreateSpecializationRequest) -> Specialization:
        user = await self.id_provider.get_user()
        user.has_access(self.settings.bot.admin_ids)

        all_tags = await self.specialization_reader.get_all_tags()

        tags = await self.ai_adapter.create_tags_from_program_description(
            data.name, data.code, data.description, tags=all_tags
        )

        async with self.uow:
            specialization = await self.specialization_writer.save(
                CreateSpecializationDTO(
                    name=data.name,
                    code=data.code,
                    institute=data.institute,
                    tags=tags,
                )
            )

            await self.uow.commit()

        await self.create_specialization_scores(
            [
                CreateSpecializationScoreDTO(
                    specialization_id=specialization.id,
                    minimal_score=item.minimal_score,
                    year=item.year,
                    seats=item.seats,
                )
                for item in data.scores
            ]
        )

        spec = await self.specialization_reader.with_id(specialization.id)

        return specialization_entity_to_dto(spec)
