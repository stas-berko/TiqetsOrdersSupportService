from abc import ABCMeta

from src.domain.use_cases.main import GetCustomersOrdersUseCase
from src.domain.use_cases.main import GetTopCustomersByTicketsCountUseCase
from src.domain.use_cases.main import GetUnusedBarcodesUseCase
from src.infrastructure.presenters_ports import CustomersOrdersPresenterPort
from src.infrastructure.presenters_ports import TopCustomersByTicketsPresenterPort
from src.infrastructure.presenters_ports import UnusedBarcodesPresenterPort
from src.infrastructure.repositories import CSVCustomersRepository
from src.infrastructure.repositories import CSVTopTicketsCustomersRepository
from src.infrastructure.repositories import CSVUnusedBarcodesRepository
from src.infrastructure.repositories import SettingsRepository
from src.infrastructure.services import CSVStorageReader
from src.infrastructure.services import STDLogger
from src.infrastructure.settings import BARCODES_CSV_STORAGE
from src.infrastructure.settings import ORDERS_CSV_STORAGE
from src.infrastructure.settings import settings
from src.infrastructure.settings import TOP_CUSTOMERS_COUNT
from src.infrastructure.validators import OrdersProcessingValidator


class BaseConsoleController(metaclass=ABCMeta):
    @property
    def settings(self):
        return SettingsRepository(settings=settings)

    @property
    def csv_storage_service(self):
        return CSVStorageReader(
            orders_file_name=self.settings.get(ORDERS_CSV_STORAGE).val,
            barcodes_file_name=self.settings.get(BARCODES_CSV_STORAGE).val,
            validator=OrdersProcessingValidator(logger=STDLogger()),
        )

    @property
    def customers_repo(self):
        return CSVCustomersRepository(csv_storage_service=self.csv_storage_service)

    @property
    def top_by_tickets_customers_repo(self):
        return CSVTopTicketsCustomersRepository(csv_storage_service=self.csv_storage_service)

    @property
    def barcodes_repo(self):
        return CSVUnusedBarcodesRepository(csv_storage_service=self.csv_storage_service)


class GetCustomersOrdersController(BaseConsoleController):
    def __init__(self, presenter: CustomersOrdersPresenterPort):
        self._presenter = presenter

    def handle(self):
        uc = GetCustomersOrdersUseCase(customers_repo=self.customers_repo)
        output = uc.execute()
        self._presenter.render(output)


class GetTopCustomersByTicketsCountController(BaseConsoleController):
    def __init__(self, presenter: TopCustomersByTicketsPresenterPort):
        self._presenter = presenter

    def handle(self):
        uc = GetTopCustomersByTicketsCountUseCase(
            top_by_tickets_customers_repo=self.top_by_tickets_customers_repo,
            top_customers_count=self.settings.get(TOP_CUSTOMERS_COUNT).val,
        )
        output = uc.execute()
        self._presenter.render(output)


class GetUnusedBarcodesController(BaseConsoleController):
    def __init__(self, presenter: UnusedBarcodesPresenterPort):
        self._presenter = presenter

    def handle(self):
        uc = GetUnusedBarcodesUseCase(barcodes_repo=self.barcodes_repo)
        output = uc.execute()
        self._presenter.render(output)
