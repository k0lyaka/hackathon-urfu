from pydantic import BaseModel

from urfu.domain.enums.subject import SubjectEnum
from urfu.domain.value_objects.user import UserId


class ExamScoreDTO(BaseModel):
    id: int
    subject: SubjectEnum
    score: int
    year: int


class CreateExamScoreDTO(BaseModel):
    user_id: UserId
    subject: SubjectEnum
    score: int
    year: int
