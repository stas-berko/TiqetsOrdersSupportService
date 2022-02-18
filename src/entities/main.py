from dataclasses import dataclass
from dataclasses import field
from functools import reduce
from typing import List
from typing import Optional

from .ext_types import ID


@dataclass(eq=True, frozen=True)
class Entity:
    pass


@dataclass(eq=True, frozen=True)
class Identity(Entity):
    id: Optional[ID] = None


@dataclass(eq=True, frozen=True)
class Customer(Identity):
    orders: List["Order"] = field(default_factory=list, hash=False)

    @property
    def tickets_count(self):
        return reduce(lambda base, orders: base + len(orders.barcodes), self.orders, 0)


@dataclass(eq=True, frozen=True)
class Order(Identity):
    barcodes: List["Barcode"] = field(default_factory=list, hash=False)

    def is_any_barcodes_connected(self) -> bool:
        return bool(len(self.barcodes))


@dataclass(eq=True, frozen=True)
class Barcode:
    code: str


@dataclass(eq=True, frozen=True)
class EmptyOrder:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance
