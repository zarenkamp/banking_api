import json

from api.utils.endpoints import Endpoints

mimetype = 'application/json'
headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
        }

# Customer 1 has three accounts: 2, 14, 18
customer_1 = '1'
valid_account_number_customer_1 = '2'
invalid_bank_account_customer_1 = '9'
non_existing_customer_id = '100'
non_existing_account_number = '1000'

customer_id_pattern = '<int:customer_id>'
account_number_pattern = '<int:account_number>'


def test_get_all_accounts_of_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS.replace(customer_id_pattern, customer_1))
    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_all_accounts_of_non_existing_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS.replace(customer_id_pattern, non_existing_customer_id))
    assert response.status_code == 404


def test_get_bank_account_of_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                          .replace(customer_id_pattern, customer_1)
                          .replace(account_number_pattern, valid_account_number_customer_1))
    assert response.status_code == 200


def test_get_invalid_account_of_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                          .replace(customer_id_pattern, customer_1)
                          .replace(account_number_pattern, invalid_bank_account_customer_1))
    assert response.status_code == 400


def test_get_non_existing_account_of_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                          .replace(customer_id_pattern, customer_1)
                          .replace(account_number_pattern, non_existing_account_number))
    assert response.status_code == 404


def test_get_account_of_non_existing_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                          .replace(customer_id_pattern, non_existing_customer_id)
                          .replace(account_number_pattern, valid_account_number_customer_1))
    assert response.status_code == 404


def test_get_non_existing_account_of_non_existing_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                          .replace(customer_id_pattern, non_existing_customer_id)
                          .replace(account_number_pattern, non_existing_account_number))
    assert response.status_code == 404


def test_create_bank_account(client):
    data = {
        'balance': 1
    }
    response = client.post(Endpoints.CUSTOMER_ACCOUNTS.replace(customer_id_pattern, customer_1),
                           data=json.dumps(data),
                           headers=headers)
    assert response.status_code == 200
    assert response.json['owner'] == int(customer_1)
    assert response.json['balance'] == data['balance']


def test_create_bank_account_with_non_existing_owner(client):
    data = {
        'balance': 1
    }
    response = client.post(Endpoints.CUSTOMER_ACCOUNTS.replace(customer_id_pattern, non_existing_customer_id),
                           data=json.dumps(data),
                           headers=headers)
    assert response.status_code == 404


def test_delete_bank_account_by_account_number(client):
    response = client.delete(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                             .replace(customer_id_pattern, customer_1)
                             .replace(account_number_pattern, valid_account_number_customer_1), headers=headers)
    assert response.status_code == 200


def test_delete_non_existing_bank_account_by_account_number(client):
    response = client.delete(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                             .replace(customer_id_pattern, customer_1)
                             .replace(account_number_pattern, non_existing_account_number), headers=headers)
    assert response.status_code == 404
    assert response.json['message'] == f'Account with id: {non_existing_account_number}, does not exist'


def test_delete_existing_bank_account_from_wrong_customer(client):
    wrong_account_number = '10'
    response = client.delete(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                             .replace(customer_id_pattern, customer_1)
                             .replace(account_number_pattern, wrong_account_number), headers=headers)
    assert response.status_code == 400
    assert response.json['message'] == f'Account {wrong_account_number} does not belong customer {customer_1}'


def test_delete_account_of_non_existing_customer(client):
    response = client.delete(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                             .replace(customer_id_pattern, non_existing_customer_id)
                             .replace(account_number_pattern, non_existing_account_number), headers=headers)
    assert response.status_code == 404
    assert response.json['message'] == f'Customer with id: {non_existing_customer_id}, does not exist'
