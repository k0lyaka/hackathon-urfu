from dataclasses import dataclass

from sqlalchemy import insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from urfu.application.gateways.user import UserReader, UserUpdater, UserWriter
from urfu.domain.dto.user import CreateUserDTO, UpdateUserDTO
from urfu.domain.entities.user import UserEntity
from urfu.domain.value_objects.user import TelegramId, UserId
from urfu.infrastructure.database.models.user import UserModel
from urfu.infrastructure.errors.gateways.user import UserNotFoundError

OPTIONS = [joinedload(UserModel.exam_scores)]


@dataclass
class UserGateway(UserReader, UserWriter, UserUpdater):
    session: AsyncSession

    async def with_id(self, user_id: UserId) -> UserEntity:
        stmt = select(UserModel).where(UserModel.id == user_id.value).options(*OPTIONS)

        try:
            result = (await self.session.scalars(stmt)).one()
        except NoResultFound as err:
            raise UserNotFoundError from err

        return result.to_entity()

    async def with_telegram_id(self, telegram_id: TelegramId) -> UserEntity:
        stmt = (
            select(UserModel)
            .where(UserModel.telegram_id == telegram_id.value)
            .options(*OPTIONS)
        )

        try:
            result = (await self.session.scalars(stmt)).unique().one()
        except NoResultFound as err:
            raise UserNotFoundError from err

        return result.to_entity()

    async def save(self, dto: CreateUserDTO) -> UserEntity:
        stmt = (
            insert(UserModel)
            .values(
                telegram_id=dto.telegram_id.value,
                username=dto.username,
            )
            .returning(UserModel.id)
        )

        user_id = (await self.session.execute(stmt)).scalar_one()

        return await self.with_id(UserId(user_id))

    async def update(self, dto: UpdateUserDTO) -> UserEntity:
        stmt = (
            update(UserModel)
            .values(dto.model_dump(exclude={"id"}, exclude_unset=True))
            .where(UserModel.id == dto.id.value)
        )

        await self.session.execute(stmt)

        return await self.with_id(dto.id)
