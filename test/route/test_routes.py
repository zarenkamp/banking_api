import pytest
from api.utils.endpoints import Endpoints

customer_id = '1'
account_number = '2'

customer_id_pattern = '<int:customer_id>'
account_number_pattern = '<int:account_number>'


@pytest.mark.parametrize("route",
                         [Endpoints.CUSTOMERS,
                          Endpoints.CUSTOMER_DETAIL
                             .replace(customer_id_pattern, customer_id),
                          Endpoints.CUSTOMER_ACCOUNTS
                             .replace(customer_id_pattern, customer_id),
                          Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                             .replace(customer_id_pattern, customer_id)
                             .replace(account_number_pattern, account_number),
                          Endpoints.CUSTOMER_ACCOUNT_HISTORY
                             .replace(customer_id_pattern, customer_id)
                             .replace(account_number_pattern, account_number)]
                         )
def test_route_status(client, route):
    response = client.get(route)
    assert response.status_code == 200


@pytest.mark.parametrize("route",
                         [Endpoints.CUSTOMERS,
                          Endpoints.CUSTOMER_ACCOUNTS
                             .replace(customer_id_pattern, customer_id),
                          Endpoints.CUSTOMER_ACCOUNT_HISTORY
                             .replace(customer_id_pattern, customer_id)
                             .replace(account_number_pattern, account_number),
                          Endpoints.TRANSFER]
                         )
def test_base_route_methods_delete(client, route):
    response = client.delete(route)
    assert response.status_code == 405


@pytest.mark.parametrize("route",
                         [Endpoints.CUSTOMER_DETAIL
                             .replace(customer_id_pattern, customer_id),
                          Endpoints.CUSTOMER_ACCOUNTS_DETAIL
                             .replace(customer_id_pattern, customer_id)
                             .replace(account_number_pattern, account_number),
                          Endpoints.CUSTOMER_ACCOUNT_HISTORY
                             .replace(customer_id_pattern, customer_id)
                             .replace(account_number_pattern, account_number)]
                         )
def test_base_route_methods_post(client, route):
    response = client.post(route)
    assert response.status_code == 405
