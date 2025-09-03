from pydantic import BaseModel, Field

from urfu.domain.value_objects.specialization import SpecializationId


class CreateSpecializationScoreRequest(BaseModel):
    minimal_score: int = Field(ge=0, le=400)
    year: int = Field(ge=2000, le=2100)
    seats: int = Field(ge=0)


class FullCreateSpecializationScoreRequest(CreateSpecializationScoreRequest):
    specialization_id: SpecializationId
