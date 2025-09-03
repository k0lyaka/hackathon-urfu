from dataclasses import dataclass

from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from urfu.application.gateways.specialization import SpecializationWriter
from urfu.application.gateways.specialization_score import SpecializationScoreReader
from urfu.domain.dto.specialization import (
    CreateSpecializationScoreDTO,
)
from urfu.domain.entities.specialization import SpecializationEntity
from urfu.domain.entities.specialization_score import SpecializationScoreEntity
from urfu.domain.value_objects.specialization import (
    SpecializationId,
    SpecializationScoreId,
)
from urfu.infrastructure.database.models.specialization_score import (
    SpecializationScoreModel,
)
from urfu.infrastructure.errors.gateways.specialization import (
    SpecializationScoreNotFoundError,
)


@dataclass
class SpecializationScoreGateway(SpecializationScoreReader, SpecializationWriter):
    session: AsyncSession

    async def with_id(
        self, specialization_score_id: SpecializationScoreId
    ) -> SpecializationScoreEntity:
        stmt = select(SpecializationScoreModel).where(
            SpecializationScoreModel.id == specialization_score_id.value
        )

        try:
            result = (await self.session.scalars(stmt)).one()
        except NoResultFound as exc:
            raise SpecializationScoreNotFoundError from exc

        return result.to_entity()

    async def with_specialization_id(
        self, specialization_id: SpecializationId
    ) -> list[SpecializationScoreEntity]:
        stmt = select(SpecializationScoreModel).where(
            SpecializationScoreModel.specialization_id == specialization_id.value
        )

        results = (await self.session.scalars(stmt)).all()

        return [result.to_entity() for result in results]

    async def save(self, dto: CreateSpecializationScoreDTO) -> SpecializationEntity:
        stmt = (
            insert(SpecializationScoreModel)
            .values(
                specialization_id=dto.specialization_id.value,
                minimal_score=dto.minimal_score,
                year=dto.year,
            )
            .returning(SpecializationScoreModel.id)
        )

        result = (await self.session.scalars(stmt)).one()

        return await self.with_id(SpecializationScoreId(result))
