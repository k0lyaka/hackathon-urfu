from dataclasses import dataclass

from sqlalchemy import insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from urfu.application.gateways.specialization import (
    SpecializationReader,
    SpecializationUpdater,
    SpecializationWriter,
)
from urfu.domain.dto.specialization import (
    CreateSpecializationDTO,
    UpdateSpecializationDTO,
)
from urfu.domain.entities.specialization import SpecializationEntity
from urfu.domain.value_objects.specialization import SpecializationId
from urfu.infrastructure.database.models.specialization import SpecializationModel
from urfu.infrastructure.errors.gateways.specialization import (
    SpecializationNotFoundError,
)

OPTIONS = [joinedload(SpecializationModel.scores)]


@dataclass
class SpecializationGateway(
    SpecializationReader, SpecializationWriter, SpecializationUpdater
):
    session: AsyncSession

    async def with_id(
        self, specialization_id: SpecializationId
    ) -> SpecializationEntity:
        stmt = (
            select(SpecializationModel)
            .where(SpecializationModel.id == specialization_id.value)
            .options(*OPTIONS)
        )

        try:
            result = (await self.session.scalars(stmt)).unique().one()
        except NoResultFound as err:
            raise SpecializationNotFoundError from err

        return result.to_entity()

    async def get_all_tags(self) -> set[str]:
        stmt = select(SpecializationModel.tags)

        tags = (await self.session.scalars(stmt)).all()
        result = set()

        for tag in tags:
            result.update(tag)

        return result

    async def save(self, dto: CreateSpecializationDTO) -> SpecializationEntity:
        stmt = (
            insert(SpecializationModel)
            .values(**dto.model_dump())
            .returning(SpecializationModel.id)
        )
        result = (await self.session.execute(stmt)).scalar_one()
        return await self.with_id(SpecializationId(result))

    async def update(self, dto: UpdateSpecializationDTO) -> SpecializationEntity:
        stmt = (
            update(SpecializationModel)
            .where(SpecializationModel.id == dto.id.value)
            .values(**dto.model_dump())
        )

        await self.session.execute(stmt)

        return await self.with_id(dto.id)
