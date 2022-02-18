from abc import ABCMeta
from abc import abstractmethod
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar

from src.entities import Barcode
from src.entities import Customer
from src.entities import ID
from src.entities import Variable

EntityType = TypeVar("EntityType")


class AbstractRetrieveRepository(Generic[EntityType], metaclass=ABCMeta):
    @abstractmethod
    def get(self, uuid) -> Optional[EntityType]:
        ...


class AbstractListRepository(Generic[EntityType], metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> List[EntityType]:
        ...


class AbstractCreateRepository(Generic[EntityType], metaclass=ABCMeta):
    @abstractmethod
    def create(self, ent: EntityType, *args, **kwargs) -> Optional[EntityType]:
        ...


class AbstractUpdateRepository(Generic[EntityType], metaclass=ABCMeta):
    @abstractmethod
    def update(self, uuid: ID, ent: EntityType, *args, **kwargs) -> Optional[EntityType]:
        ...


class AbstractDeleteRepository(Generic[EntityType], metaclass=ABCMeta):
    @abstractmethod
    def delete(self, uuid: ID, *args, **kwargs) -> bool:
        ...


class AbstractCustomersRepository(AbstractListRepository[Customer], metaclass=ABCMeta):
    pass


class AbstractTopTicketsCustomersRepository(Generic[EntityType], AbstractListRepository[Customer], metaclass=ABCMeta):
    @abstractmethod
    def get_top_customers_by_tickets(self, count) -> List[EntityType]:
        pass


class AbstractUnusedBarcodesRepository(AbstractListRepository[Barcode], metaclass=ABCMeta):
    pass


class AbstractSettingsRepository(AbstractRetrieveRepository[Variable], metaclass=ABCMeta):
    pass
