from pydantic import BaseModel

from urfu.application.contracts.specializations_scores.create import (
    CreateSpecializationScoreRequest,
)


class CreateSpecializationRequest(BaseModel):
    name: str
    code: str
    description: str
    institute: str
    scores: list[CreateSpecializationScoreRequest]
