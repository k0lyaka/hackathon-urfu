from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.uow import UnitOfWork
from urfu.application.contracts.users.create_or_update import CreateOrUpdateUserRequest
from urfu.application.gateways.user import UserReader, UserUpdater, UserWriter
from urfu.domain.dto.user import CreateUserDTO, UpdateUserDTO
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.errors.gateways.user import UserNotFoundError


@dataclass
class CreateOrUpdateUser(Interactor[CreateOrUpdateUserRequest, UserEntity]):
    user_reader: UserReader
    user_writer: UserWriter
    user_updater: UserUpdater

    uow: UnitOfWork

    async def __call__(self, data: CreateOrUpdateUserRequest) -> UserEntity:
        async with self.uow:
            try:
                user = await self.user_reader.with_telegram_id(data.telegram_id)
            except UserNotFoundError:
                user = await self.user_writer.save(
                    CreateUserDTO(
                        telegram_id=data.telegram_id,
                        username=data.username,
                    )
                )

            if user.username != data.username:
                user = await self.user_updater.update(
                    UpdateUserDTO(
                        id=user.id,
                        username=data.username,
                    )
                )

            await self.uow.commit()

        return user
