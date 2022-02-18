import csv
import sys
from collections import defaultdict

from src.entities import Barcode
from src.entities import Customer
from src.entities import Order
from src.entities.main import EmptyOrder


class CSVStorageReader:
    def __init__(self, orders_file_name: str, barcodes_file_name: str, validator):
        self._orders_file_name = orders_file_name
        self._barcodes_file_name = barcodes_file_name
        self._validator = validator

    @staticmethod
    def _load(file_name: str):
        with open(file_name) as csv_file:
            orders_reader = csv.reader(csv_file)
            next(orders_reader, None)
            resp = list(orders_reader)
        return resp

    def _barcodes_load(self):
        return self._load(self._barcodes_file_name)

    def _orders_load(self):
        return self._load(self._orders_file_name)

    def load_barcodes(self):
        validated_barcodes = self._validator.validate_barcodes(self._barcodes_load())

        orders_storage = defaultdict(list)
        for row in validated_barcodes:
            barcode, order = row
            if order == "":
                order = EmptyOrder()
            orders_storage[order].append(Barcode(code=barcode))
        return orders_storage

    def load_customers(self):
        orders_with_barcodes = self.load_barcodes()

        stor = {}

        for c_order, customer_id in self._orders_load():
            customer = stor.setdefault(customer_id, Customer(id=customer_id))
            valid_order = self._validator.validate_order(Order(id=c_order, barcodes=orders_with_barcodes[c_order]))
            if valid_order:
                customer.orders.append(valid_order)
        return stor.values()


class STDLogger:
    @staticmethod
    def info(*msg):
        print(*msg, file=sys.stdout)

    @staticmethod
    def warning(*msg):
        print(*msg, file=sys.stderr)
