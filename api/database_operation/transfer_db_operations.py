from typing import List

from api.model.transfer import Transfer
from api.model.customer import Customer
from api.model.account import Account
from api.database_operation.account_db_operations import AccountDatabaseOperations
from api.utils.exceptions import CoveringNotSufficientException, AccountDoesNotExistException, \
    CustomerDoesNotExistException, WrongAccountException
from database import db


class TransferDatabaseOperations:

    @staticmethod
    def do_transfer(sending_customer: int, sending_account: int, receiving_customer: int, receiving_account: int, amount: float = 0) -> Transfer:
        sender_account = AccountDatabaseOperations.get_account_of_customer_by_account_number(sending_customer,
                                                                                             sending_account)
        receiver_account = AccountDatabaseOperations.get_account_of_customer_by_account_number(receiving_customer,
                                                                                               receiving_account)

        if amount > sender_account.balance:
            raise CoveringNotSufficientException

        sender_account.balance -= amount
        receiver_account.balance += amount

        new_transfer = Transfer(sending_customer, sending_account, receiving_customer, receiving_account, amount)
        db.session.add(new_transfer)
        db.session.commit()
        db.session.refresh(new_transfer)

        return new_transfer

    @staticmethod
    def get_all_transfers_of_account(customer_id: int, account_number: int) -> List[Transfer]:

        customer = Customer.query.get(customer_id)
        if customer is None:
            raise CustomerDoesNotExistException(customer_id)

        accounts_of_customer = Account.query.filter_by(owner=customer_id)
        account = Account.query.get(account_number)

        if account is None:
            raise AccountDoesNotExistException(account_number)

        if account not in accounts_of_customer:
            raise WrongAccountException(customer_id, account_number)

        all_transfers = Transfer.query\
            .filter((Transfer.receiving_account == account_number) | (Transfer.sending_account == account_number))\
            .order_by(Transfer.transfer_date.desc())
        return all_transfers
