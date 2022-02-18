from collections import Counter
from typing import Dict, List
from typing import Iterable
from typing import Optional
from typing import Tuple

from src.entities import Order


class OrdersProcessingValidator:
    DUPLICATION_ISSUE = "Duplicated Barcode {}"
    EMPTY_ORDER = "Empty Order {}"

    def __init__(self, logger):
        self._logger = logger

    def validate_order(self, order: Order) -> Optional[Order]:
        if order.is_any_barcodes_connected():
            return order
        else:
            self._logger.warning(self.EMPTY_ORDER.format(order.id))
            return None

    def _have_duplicate(self, x: str, duplicates: Dict) -> bool:
        return x in duplicates and duplicates[x] > 1

    def barcode_duplication_remove(self, barcodes: List[Tuple[str, int]]) -> Iterable:
        duplicates_storage = Counter(barcode for barcode, _ in barcodes)
        valid_barcodes = filter(lambda x: not self._have_duplicate(x[0], duplicates=duplicates_storage), barcodes)
        invalid_barcodes = filter(lambda x: self._have_duplicate(x[0], duplicates=duplicates_storage), barcodes)
        for i_barcode in invalid_barcodes:
            self._logger.warning(self.DUPLICATION_ISSUE.format(i_barcode[0]))
        return valid_barcodes

    def validate_barcodes(self, barcodes: List[Tuple[str, int]]) -> Iterable:
        valid_orders = self.barcode_duplication_remove(barcodes)
        return valid_orders
