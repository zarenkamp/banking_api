from enum import StrEnum


class Endpoints(StrEnum):
    # GET, POST
    CUSTOMERS = '/api/customers'
    # GET, DELETE
    CUSTOMER_DETAIL = '/api/customers/<int:customer_id>'
    # GET, POST
    CUSTOMER_ACCOUNTS = '/api/customers/<int:customer_id>/accounts'
    # GET, DELETE
    CUSTOMER_ACCOUNTS_DETAIL = '/api/customers/<int:customer_id>/accounts/<int:account_number>'
    # GET
    CUSTOMER_ACCOUNT_HISTORY = '/api/customers/<int:customer_id>/accounts/<int:account_number>/history'

    # POST
    TRANSFER = '/api/transfer'


