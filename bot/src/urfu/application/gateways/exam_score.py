from typing import Protocol

from urfu.domain.dto.exam_score import CreateExamScoreDTO
from urfu.domain.entities.exam_score import ExamScoreEntity
from urfu.domain.value_objects.user import UserId


class ExamScoreReader(Protocol):
    async def with_user_id(self, user_id: UserId) -> list[ExamScoreEntity]: ...


class ExamScoreWriter(Protocol):
    async def save(self, dto: CreateExamScoreDTO) -> ExamScoreEntity: ...
    async def delete_exams(self, user_id: UserId) -> None: ...
