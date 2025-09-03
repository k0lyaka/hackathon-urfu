from pydantic import BaseModel


class UpdateInterestsRequest(BaseModel):
    interests: str
