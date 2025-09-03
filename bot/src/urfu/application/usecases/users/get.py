from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.contracts.users.get import GetUserRequest
from urfu.domain.dto.user import UserDTO
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.database.mappers.user import user_entity_to_dto


@dataclass
class GetUser(Interactor[GetUserRequest, UserDTO]):
    id_provider: IdProvider[UserEntity]

    async def __call__(self, _: GetUserRequest) -> UserDTO:
        user = await self.id_provider.get_user()
        return user_entity_to_dto(user)
