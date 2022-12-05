from flask import request, Blueprint

from api.schema.account_schema import account_schema, accounts_schema
from api.schema.transfer_schema import transfers_schema
from api.database_operation.account_db_operations import AccountDatabaseOperations
from api.database_operation.transfer_db_operations import TransferDatabaseOperations
from api.utils.endpoints import Endpoints
from api.utils.exceptions import CustomerDoesNotExistException, AccountDoesNotExistException, WrongAccountException

account_route = Blueprint('account_route', __name__)


@account_route.route(Endpoints.CUSTOMER_ACCOUNTS, methods=['GET', 'POST'])
def customer_accounts(customer_id):

    if request.method == 'GET':
        try:
            accounts = AccountDatabaseOperations.get_accounts_by_customer_id(customer_id)
            return accounts_schema.jsonify(accounts)
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404

    if request.method == 'POST':
        balance = request.json['balance']
        try:
            new_account = AccountDatabaseOperations.add_new_account_for_customer(owner=customer_id, balance=balance)
            return account_schema.jsonify(new_account)
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404


@account_route.route(Endpoints.CUSTOMER_ACCOUNTS_DETAIL, methods=['GET', 'DELETE'])
def customer_account_detail(customer_id, account_number):

    if request.method == 'GET':
        try:
            account = AccountDatabaseOperations.get_account_of_customer_by_account_number(customer_id, account_number)
            return account_schema.jsonify(account)
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404
        except AccountDoesNotExistException as e:
            return {'message': e.message}, 404
        except WrongAccountException as e:
            return {'message': e.message}, 400

    if request.method == 'DELETE':
        try:
            AccountDatabaseOperations.delete_account(customer_id, account_number)
            return {'message': f'Account with id: {account_number}, deleted'}
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404
        except AccountDoesNotExistException as e:
            return {'message': e.message}, 404
        except WrongAccountException as e:
            return {'message': e.message}, 400


@account_route.route(Endpoints.CUSTOMER_ACCOUNT_HISTORY, methods=['GET'])
def customer_account_history(customer_id, account_number):
    if request.method == 'GET':
        try:
            transfer_history = TransferDatabaseOperations.get_all_transfers_of_account(customer_id, account_number)
            return transfers_schema.jsonify(transfer_history)
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404
        except AccountDoesNotExistException as e:
            return{'message':  e.message}, 404
        except WrongAccountException as e:
            return {'message': e.message}, 400

