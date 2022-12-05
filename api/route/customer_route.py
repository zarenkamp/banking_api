from flask import request, Blueprint

from api.schema.customer_schema import customer_schema, customers_schema
from api.database_operation.customer_db_operations import CustomerDatabaseOperations
from api.utils.endpoints import Endpoints
from api.utils.exceptions import CustomerDoesNotExistException

customer_route = Blueprint('customer_route', __name__)


@customer_route.route(Endpoints.CUSTOMERS, methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        all_customers = CustomerDatabaseOperations.get_all_customers()
        return customers_schema.jsonify(all_customers)

    if request.method == 'POST':
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        new_customer = CustomerDatabaseOperations.add_new_customer(first_name, last_name)
        return customer_schema.jsonify(new_customer)


@customer_route.route(Endpoints.CUSTOMER_DETAIL, methods=['GET', 'DELETE'])
def customer_detail(customer_id):
    if request.method == 'GET':
        try:
            customer = CustomerDatabaseOperations.get_customer_by_id(customer_id)
            return customer_schema.jsonify(customer)
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404

    if request.method == 'DELETE':
        try:
            CustomerDatabaseOperations.delete_customer(customer_id)
            return {'message': f'Deleted customer with id {customer_id}'}, 200
        except CustomerDoesNotExistException as e:
            return {'message': e.message}, 404
