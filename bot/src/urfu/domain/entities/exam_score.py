from urfu.domain.entities.base import BaseEntity
from urfu.domain.enums.subject import SubjectEnum
from urfu.domain.value_objects.exam_score import ExamScoreId


class ExamScoreEntity(BaseEntity[ExamScoreId]):
    subject: SubjectEnum
    score: int
    year: int
