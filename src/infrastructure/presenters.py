from abc import ABCMeta
from typing import List

from src.entities import Barcode
from src.entities import Customer
from src.infrastructure.presenters_ports import CustomersOrdersPresenterPort
from src.infrastructure.presenters_ports import TopCustomersByTicketsPresenterPort
from src.infrastructure.presenters_ports import UnusedBarcodesPresenterPort


class BaseFileOutPresenter(metaclass=ABCMeta):
    def __init__(self, file_name: str):
        self._file_name = file_name


class BaseSTDPresenter(metaclass=ABCMeta):
    def __init__(self, logger):
        self._logger = logger


class CustomersOrdersPresenter(CustomersOrdersPresenterPort, BaseFileOutPresenter):
    def render(self, customers: List[Customer]):
        with open(self._file_name, "w") as f:
            for customer in customers:
                for order in customer.orders:
                    f.write(f"{customer.id}, {order.id} ,[{','.join(bc.code for bc in order.barcodes)}]\n")


class TopCustomersByTicketsPresenter(TopCustomersByTicketsPresenterPort, BaseSTDPresenter):
    def render(self, customers: List[Customer]):
        for customer in customers:
            self._logger.info(f"{customer.id}, {customer.tickets_count}")


class UnusedBarcodesPresenter(UnusedBarcodesPresenterPort, BaseSTDPresenter):
    def render(self, barcodes: List[Barcode]):
        for barcode in barcodes:
            self._logger.info(f"{barcode.code}")
