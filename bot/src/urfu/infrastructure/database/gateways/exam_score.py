from dataclasses import dataclass

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from urfu.application.gateways.exam_score import ExamScoreReader, ExamScoreWriter
from urfu.domain.dto.exam_score import CreateExamScoreDTO
from urfu.domain.entities.exam_score import ExamScoreEntity
from urfu.domain.value_objects.user import UserId
from urfu.infrastructure.database.models.exam_score import ExamScoreModel


@dataclass
class ExamScoreGateway(ExamScoreReader, ExamScoreWriter):
    session: AsyncSession

    async def with_user_id(self, user_id: UserId) -> list[ExamScoreEntity]:
        stmt = select(ExamScoreModel).where(ExamScoreModel.user_id == user_id.value)

        results = (await self.session.scalars(stmt)).all()

        return [result.to_entity() for result in results]

    async def save(self, dto: CreateExamScoreDTO) -> ExamScoreEntity:
        stmt = (
            insert(ExamScoreModel)
            .values(
                user_id=dto.user_id.value,
                subject=dto.subject,
                score=dto.score,
                year=dto.year,
            )
            .returning(ExamScoreModel)
        )

        result = (await self.session.execute(stmt)).scalar_one()
        return result.to_entity()

    async def delete_exams(self, user_id: UserId) -> None:
        stmt = delete(ExamScoreModel).where(ExamScoreModel.user_id == user_id.value)
        await self.session.execute(stmt)
