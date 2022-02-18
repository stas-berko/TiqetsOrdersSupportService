from typing import Dict
from typing import List
from typing import Optional

from src.domain.interfaces.repositories import AbstractCustomersRepository
from src.domain.interfaces.repositories import AbstractSettingsRepository
from src.domain.interfaces.repositories import AbstractTopTicketsCustomersRepository
from src.domain.interfaces.repositories import AbstractUnusedBarcodesRepository
from src.domain.interfaces.repositories import EntityType
from src.entities import Customer
from src.entities import EmptyOrder
from src.entities import Variable
from src.infrastructure.services import CSVStorageReader


class CSVCustomersRepository(AbstractCustomersRepository):
    def __init__(self, csv_storage_service: CSVStorageReader):
        self._csv_storage_service = csv_storage_service

    def get_all(self) -> List[EntityType]:
        return self._csv_storage_service.load_customers()


class CSVTopTicketsCustomersRepository(AbstractTopTicketsCustomersRepository[Customer]):
    def __init__(self, csv_storage_service):
        self._csv_storage_service = csv_storage_service

    def get_all(self) -> List[EntityType]:
        return self._csv_storage_service.load_customers()

    def get_top_customers_by_tickets(self, count) -> List[Customer]:
        customers: List[Customer] = self.get_all()
        ordered_by_tickets_count = sorted(customers, key=lambda x: x.tickets_count, reverse=True)
        return ordered_by_tickets_count[:count]


class CSVUnusedBarcodesRepository(AbstractUnusedBarcodesRepository):
    def __init__(self, csv_storage_service):
        self._csv_storage_service = csv_storage_service

    def get_all(self) -> List[EntityType]:
        barcodes = self._csv_storage_service.load_barcodes()
        return barcodes.get(EmptyOrder(), [])


class SettingsRepository(AbstractSettingsRepository):
    def __init__(self, settings: Dict):
        self._settings = settings

    def get(self, uuid: str) -> Optional[Variable]:
        val = self._settings.get(uuid)
        return None if val is None else Variable(key=uuid, val=val)
