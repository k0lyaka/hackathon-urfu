from pydantic import BaseModel, Field

from urfu.domain.enums.subject import SubjectEnum


class ExamScoreItem(BaseModel):
    subject: SubjectEnum
    score: int = Field(..., ge=0, le=100)
    year: int = Field(..., ge=2000, le=2100)


class AddExamScoresRequest(BaseModel):
    exams: list[ExamScoreItem] = Field(..., min_length=1, max_length=5)
