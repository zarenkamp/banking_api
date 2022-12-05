from typing import List

from database import db
from api.model.customer import Customer

from api.utils.exceptions import CustomerDoesNotExistException


class CustomerDatabaseOperations:

    @staticmethod
    def get_all_customers() -> List[Customer]:
        return Customer.query.all()

    @staticmethod
    def get_customer_by_id(customer_id: int) -> Customer:
        customer = Customer.query.get(customer_id)
        if customer is None:
            raise CustomerDoesNotExistException(customer_id)
        return customer

    @staticmethod
    def add_new_customer(first_name: str, last_name: str) -> Customer:
        new_customer = Customer(first_name, last_name)
        db.session.add(new_customer)
        db.session.commit()
        return new_customer

    @staticmethod
    def delete_customer(customer_id: int) -> None:
        customer = Customer.query.get(customer_id)
        if customer is None:
            raise CustomerDoesNotExistException(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return None


