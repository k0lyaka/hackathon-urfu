from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.security.id_provider import IdProvider
from urfu.application.common.uow import UnitOfWork
from urfu.application.contracts.exam_scores.add_exam_scores import AddExamScoresRequest
from urfu.application.gateways.exam_score import ExamScoreWriter
from urfu.domain.dto.exam_score import CreateExamScoreDTO
from urfu.domain.dto.user import UserDTO
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.database.mappers.user import user_entity_to_dto


@dataclass
class AddExamScores(Interactor[AddExamScoresRequest, UserDTO]):
    exam_score_writer: ExamScoreWriter

    id_provider: IdProvider[UserEntity]

    uow: UnitOfWork

    async def __call__(self, data: AddExamScoresRequest) -> UserDTO:
        user = await self.id_provider.get_user()

        async with self.uow:
            await self.exam_score_writer.delete_exams(user.id)

            for exam in data.exams:
                await self.exam_score_writer.save(
                    CreateExamScoreDTO(
                        user_id=user.id,
                        subject=exam.subject,
                        score=exam.score,
                        year=exam.year,
                    )
                )

            await self.uow.commit()

        return user_entity_to_dto(user)
