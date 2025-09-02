from typing import Protocol


class Interactor[Input, Output](Protocol):
    async def __init__(self, data: Input) -> Output: ...
