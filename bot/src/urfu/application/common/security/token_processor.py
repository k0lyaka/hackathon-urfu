from typing import Protocol

from urfu.domain.value_objects.user import UserId


class TokenProcessor(Protocol):
    async def create(self, user_id: UserId) -> str: ...
    async def verify(self, token: str, **kwargs: str) -> int: ...
