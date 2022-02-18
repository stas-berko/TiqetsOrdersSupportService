from dataclasses import dataclass
from typing import Any


@dataclass
class ID:
    id: int


@dataclass
class Variable:
    key: str
    val: Any
