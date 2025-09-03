from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.contracts.users.get import GetUserRequest
from urfu.domain.entities.user import UserEntity


@dataclass
class GetUser(Interactor[GetUserRequest, UserEntity]):
    id_provider: IdProvider[UserEntity]

    async def __call__(self, _: GetUserRequest) -> UserEntity:
        return await self.id_provider.get_user()
