from abc import ABCMeta
from abc import abstractmethod
from typing import List

from src.entities import Barcode
from src.entities import Customer


class TopCustomersByTicketsPresenterPort(metaclass=ABCMeta):
    @abstractmethod
    def render(self, customers: List[Customer]):
        ...


class CustomersOrdersPresenterPort(metaclass=ABCMeta):
    @abstractmethod
    def render(self, customers: List[Customer]):
        ...


class UnusedBarcodesPresenterPort(metaclass=ABCMeta):
    @abstractmethod
    def render(self, barcodes: List[Barcode]):
        ...
