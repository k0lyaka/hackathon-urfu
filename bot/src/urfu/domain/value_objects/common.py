from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Self

from pydantic import ValidationInfo


@dataclass(slots=True, frozen=True)
class ValueObject[T]:
    value: T

    @classmethod
    def __get_validators__(cls) -> Iterator[Any]:
        yield cls.__validate

    @classmethod
    def __validate(cls, v: Any, _: ValidationInfo) -> Self:
        if isinstance(v, cls):
            return v
        if isinstance(v, dict):
            return cls(**v)
        return cls(v)


class PositiveInteger(ValueObject[int]):
    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("integer must be positive")


class Integer(ValueObject[int]):
    pass
