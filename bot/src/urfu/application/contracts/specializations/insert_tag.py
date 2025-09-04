from pydantic import BaseModel


class InsertTagsRequest(BaseModel):
    specialization_id: int
    tags: list[str]
