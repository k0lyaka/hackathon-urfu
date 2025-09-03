from typing import Protocol


class Interactor[Input, Output](Protocol):
    async def __call__(self, data: Input) -> Output: ...
