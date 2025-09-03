from pydantic import BaseModel

from urfu.domain.enums.subject import SubjectEnum


class ExamScore(BaseModel):
    subject: SubjectEnum
    score: int
    year: int
