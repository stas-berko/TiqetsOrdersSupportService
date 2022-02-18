from src.infrastructure.controllers import GetCustomersOrdersController
from src.infrastructure.controllers import GetTopCustomersByTicketsCountController
from src.infrastructure.controllers import GetUnusedBarcodesController
from src.infrastructure.presenters import CustomersOrdersPresenter
from src.infrastructure.presenters import TopCustomersByTicketsPresenter
from src.infrastructure.presenters import UnusedBarcodesPresenter
from src.infrastructure.services import STDLogger


def main():
    GetCustomersOrdersController(presenter=CustomersOrdersPresenter(file_name="out/customers.txt")).handle()
    GetTopCustomersByTicketsCountController(presenter=TopCustomersByTicketsPresenter(logger=STDLogger())).handle()
    GetUnusedBarcodesController(presenter=UnusedBarcodesPresenter(logger=STDLogger())).handle()


if __name__ == "__main__":
    main()
