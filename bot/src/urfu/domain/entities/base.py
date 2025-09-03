from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BaseEntity[T](BaseModel):
    model_config = ConfigDict(from_attributes=True, frozen=True)

    id: T

    created_at: datetime
    updated_at: datetime
