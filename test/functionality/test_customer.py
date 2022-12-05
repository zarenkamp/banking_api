import json
from api.utils.endpoints import Endpoints

mimetype = 'application/json'
headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
        }

customer_id = '1'
non_existing_customer_id = '100'
account_number = '2'
non_existing_account_number = '1000'

customer_id_pattern = '<int:customer_id>'
account_number_pattern = '<int:account_number>'


def test_get_all_customers(client):
    response = client.get(Endpoints.CUSTOMERS, headers=headers)

    assert len(response.json) == 10
    assert response.json[0]['first_name'] == 'Aguste'


def test_get_specific_customer_by_id(client):
    response = client.get(Endpoints.CUSTOMER_DETAIL.replace(customer_id_pattern, customer_id), headers=headers)
    assert response.status_code == 200
    assert response.json['first_name'] == 'Aguste'
    assert response.json['last_name'] == 'Suerz'


def test_get_non_existing_customer_by_id(client):
    response = client.get(Endpoints.CUSTOMER_DETAIL.replace(customer_id_pattern, non_existing_customer_id),
                          headers=headers)
    assert response.status_code == 404
    # assert response.json['message'] == 'Customer not found'


def test_create_customer(client):
    data = {
        'first_name': 'e',
        'last_name': 'f'
    }
    response = client.post(Endpoints.CUSTOMERS, data=json.dumps(data), headers=headers)

    assert response.json['first_name'] == data['first_name']
    assert response.json['last_name'] == data['last_name']
    assert response.content_type == mimetype


def test_delete_customer(client):
    response = client.delete(Endpoints.CUSTOMER_DETAIL.replace(customer_id_pattern, customer_id), headers=headers)
    assert response.status_code == 200


def test_delete_non_existing_customer(client):
    response = client.delete(Endpoints.CUSTOMER_DETAIL.replace(customer_id_pattern, non_existing_customer_id),
                             headers=headers)
    assert response.status_code == 404

