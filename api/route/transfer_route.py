from flask import request, Blueprint

from api.schema.transfer_schema import transfer_schema
from api.database_operation.transfer_db_operations import TransferDatabaseOperations
from api.utils.endpoints import Endpoints
from api.utils.exceptions import CoveringNotSufficientException, AccountDoesNotExistException

transfer_route = Blueprint('transaction_route', __name__)


@transfer_route.route(Endpoints.TRANSFER, methods=['POST'])
def transfer():
    if request.method == 'POST':
        sending_customer = request.json['sending_customer']
        sending_account = request.json['sending_account']
        receiving_customer = request.json['receiving_customer']
        receiving_account = request.json['receiving_account']
        amount = request.json['amount']
        try:
            new_transfer = TransferDatabaseOperations.do_transfer(sending_customer,
                                                                  sending_account,
                                                                  receiving_customer,
                                                                  receiving_account,
                                                                  amount)
        except CoveringNotSufficientException as e:
            return {'message': e.message}, 400
        except AccountDoesNotExistException as e:
            return {'message': e.message}, 400

        return transfer_schema.jsonify(new_transfer), 200


