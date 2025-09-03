from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.common.uow import UnitOfWork
from urfu.application.contracts.users.update_interests import UpdateInterestsRequest
from urfu.application.gateways.specialization import SpecializationReader
from urfu.application.gateways.user import UserUpdater
from urfu.domain.dto.user import UpdateUserDTO, UserDTO
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.adapters.openai.client import AiAdapter
from urfu.infrastructure.database.mappers.user import user_entity_to_dto


@dataclass
class UpdateInterests(Interactor[UpdateInterestsRequest, UserDTO]):
    specialization_reader: SpecializationReader
    user_updater: UserUpdater

    ai_adapter: AiAdapter
    id_provider: IdProvider[UserEntity]

    uow: UnitOfWork

    async def __call__(self, data: UpdateInterestsRequest) -> UserDTO:
        user = await self.id_provider.get_user()
        all_tags = await self.specialization_reader.get_all_tags()

        tags = await self.ai_adapter.create_tags_from_user_input(
            data.interests, tags=f"[{', '.join(all_tags)}]"
        )

        async with self.uow:
            user = await self.user_updater.update(
                UpdateUserDTO(
                    id=user.id,
                    full_interest_text=data.interests,
                    interest_tags=tags,
                )
            )

            await self.uow.commit()

        return user_entity_to_dto(user)
