import pytest

from database import db
from app import create_app

from test.db_mock_data import mock_customers, mock_accounts, mock_transfers


@pytest.fixture
def client():
    app = create_app('testing')

    client = app.test_client()
    with app.app_context():
        db.create_all()
        for c in mock_customers:
            db.session.execute(c)
        for a in mock_accounts:
            db.session.execute(a)
        for t in mock_transfers:
            db.session.execute(t)
        db.session.commit()

    yield client


