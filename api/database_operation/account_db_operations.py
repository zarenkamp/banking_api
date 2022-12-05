from typing import List

from api.model.account import Account
from api.model.customer import Customer
from api.utils.exceptions import CustomerDoesNotExistException, AccountDoesNotExistException, WrongAccountException
from database import db


class AccountDatabaseOperations:

    @staticmethod
    def get_account_of_customer_by_account_number(customer_id, account_number: int) -> Account:
        customer = Customer.query.get(customer_id)
        if customer is None:
            raise CustomerDoesNotExistException(customer_id)

        accounts_of_customer = Account.query.filter_by(owner=customer_id)
        account = Account.query.get(account_number)

        if account is None:
            raise AccountDoesNotExistException(account_number)

        if account not in accounts_of_customer:
            raise WrongAccountException(customer_id, account_number)

        return Account.query.get(account_number)

    @staticmethod
    def add_new_account_for_customer(owner: int, balance: float = 0) -> Account:
        customer = Customer.query.get(owner)
        if customer is None:
            raise CustomerDoesNotExistException(owner)

        new_account = Account(owner, balance)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    @staticmethod
    def delete_account(customer_id: int, account_number: int) -> None:
        customer = Customer.query.get(customer_id)
        if customer is None:
            raise CustomerDoesNotExistException(customer_id)

        accounts_of_customer = Account.query.filter_by(owner=customer_id)
        account = Account.query.get(account_number)

        if account is None:
            raise AccountDoesNotExistException(account_number)

        if account not in accounts_of_customer:
            raise WrongAccountException(customer_id, account_number)

        db.session.delete(account)
        db.session.commit()
        return None

    @staticmethod
    def get_accounts_by_customer_id(customer_id: int) -> List[Account]:
        customer = Customer.query.get(customer_id)
        if customer is None:
            raise CustomerDoesNotExistException(customer_id)
        return Account.query.filter_by(owner=customer_id)
