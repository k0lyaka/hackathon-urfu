from typing import Protocol


class IdProvider[IdType](Protocol):
    async def get_user(self) -> IdType: ...
