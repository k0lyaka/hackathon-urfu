from pydantic import BaseModel

from urfu.domain.value_objects.specialization import SpecializationId


class SpecializationScore(BaseModel):
    id: int

    minimal_score: int
    year: int
    seats: int


class Specialization(BaseModel):
    id: int
    name: str
    code: str
    institute: str
    tags: list[str]

    scores: list[SpecializationScore]


class CreateSpecializationDTO(BaseModel):
    name: str
    code: str
    institute: str
    tags: list[str]


class UpdateSpecializationDTO(BaseModel):
    id: SpecializationId
    name: str | None = None
    code: str | None = None
    institute: str | None = None
    tags: list[str] | None = None


class CreateSpecializationScoreDTO(BaseModel):
    specialization_id: SpecializationId
    minimal_score: int
    seats: int
    year: int
