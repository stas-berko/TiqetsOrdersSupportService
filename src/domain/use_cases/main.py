from abc import ABCMeta
from abc import abstractmethod
from typing import List

from src.domain.interfaces import repositories as repo
from src.entities import Barcode
from src.entities import Customer


class UseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class GetCustomersOrdersUseCase(UseCase):
    def __init__(
        self,
        customers_repo: repo.AbstractCustomersRepository,
    ):
        self._customers_repo = customers_repo

    def execute(self) -> List[Customer]:
        return self._customers_repo.get_all()


class GetTopCustomersByTicketsCountUseCase(UseCase):
    def __init__(
        self, top_by_tickets_customers_repo: repo.AbstractTopTicketsCustomersRepository, top_customers_count: int
    ):
        self._top_by_tickets_customers_repo = top_by_tickets_customers_repo
        self.top_customers_count = top_customers_count

    def execute(self) -> List[Customer]:
        return self._top_by_tickets_customers_repo.get_top_customers_by_tickets(count=self.top_customers_count)


class GetUnusedBarcodesUseCase(UseCase):
    def __init__(
        self,
        barcodes_repo: repo.AbstractUnusedBarcodesRepository,
    ):
        self._barcodes_repo = barcodes_repo

    def execute(self) -> List[Barcode]:
        return self._barcodes_repo.get_all()
