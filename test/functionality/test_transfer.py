import json
from api.utils.endpoints import Endpoints

mimetype = 'application/json'
headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
        }

customer_1 = '1'
account_2_customer_1 = '2'
invalid_account_customer_1 = '9'
non_existing_sender = 100

customer_2 = '2'
account_9_customer_2 = '9'
non_existing_receiver = 101

non_existing_customer_id = '100'
non_existing_account_number = '1000'

amount = 100
invalid_amount = 1000000

customer_id_pattern = '<int:customer_id>'
account_number_pattern = '<int:account_number>'


def test_do_transfer(client):
    data = {
        'sending_customer': customer_1,
        'sending_account': account_2_customer_1,
        'receiving_customer': customer_2,
        'receiving_account': account_9_customer_2,
        'amount': amount
    }
    sender_account_initial_balance = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                                                .replace(customer_id_pattern, customer_1)
                                                .replace(account_number_pattern, account_2_customer_1)).json['balance']

    receiver_account_initial_balance = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                                                  .replace(customer_id_pattern, customer_2)
                                                  .replace(account_number_pattern, account_9_customer_2)).json['balance']

    response = client.post(Endpoints.TRANSFER, data=json.dumps(data), headers=headers)

    sender_account_final_balance = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                                              .replace(customer_id_pattern, customer_1)
                                              .replace(account_number_pattern, account_2_customer_1)).json['balance']

    receiver_account_final_balance = client.get(Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                                                .replace(customer_id_pattern, customer_2)
                                                .replace(account_number_pattern, account_9_customer_2)).json['balance']

    assert response.status_code == 200
    assert sender_account_final_balance == sender_account_initial_balance - data['amount']
    assert receiver_account_final_balance == receiver_account_initial_balance + data['amount']


def test_do_transfer_with_insufficient_covering(client):
    data = {
        'sending_customer': customer_1,
        'sending_account': account_2_customer_1,
        'receiving_customer': customer_2,
        'receiving_account': account_9_customer_2,
        'amount': invalid_amount
    }
    response = client.post(Endpoints.TRANSFER, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['message'] == 'Insufficient covering'


def test_do_transfer_to_non_existing_account(client):
    data = {
        'sending_customer': customer_1,
        'sending_account': account_2_customer_1,
        'receiving_customer': customer_2,
        'receiving_account': non_existing_account_number,
        'amount': invalid_amount
    }
    response = client.post(Endpoints.TRANSFER, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['message'] == f'Account with id: {data["receiving_account"]}, does not exist'


def test_do_transfer_from_non_exiting_account(client):
    data = {
        'sending_customer': customer_1,
        'sending_account': non_existing_sender,
        'receiving_customer': account_9_customer_2,
        'receiving_account': account_9_customer_2,
        'amount': amount
    }
    response = client.post(Endpoints.TRANSFER, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    assert response.json['message'] == f'Account with id: {data["sending_account"]}, does not exist'


def test_get_transfer_history(client):

    response = client.get(Endpoints.CUSTOMER_ACCOUNT_HISTORY
                          .replace(customer_id_pattern, customer_1)
                          .replace(account_number_pattern, account_2_customer_1))
    assert response.status_code == 200
    assert len(response.json) == 3

    response = client.get(Endpoints.CUSTOMER_ACCOUNT_HISTORY
                          .replace(customer_id_pattern, customer_2)
                          .replace(account_number_pattern, account_9_customer_2))

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_transfer_history_of_non_existing_account_of_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNT_HISTORY
                          .replace(customer_id_pattern, customer_1)
                          .replace(account_number_pattern, non_existing_account_number))
    assert response.status_code == 404


def test_get_transfer_history_of_account_of_non_existing_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNT_HISTORY
                          .replace(customer_id_pattern, non_existing_customer_id)
                          .replace(account_number_pattern, account_2_customer_1))
    assert response.status_code == 404


def test_get_transfer_history_of_invalid_account_of_customer(client):
    response = client.get(Endpoints.CUSTOMER_ACCOUNT_HISTORY
                          .replace(customer_id_pattern, customer_1)
                          .replace(account_number_pattern, invalid_account_customer_1))
    assert response.status_code == 400


