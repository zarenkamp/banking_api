"""Create a data base for local development"""
import os

from database import db
from test.db_mock_data import mock_accounts, mock_customers, mock_transfers

basedir = os.path.abspath(os.path.dirname(__file__))
file_name = 'db.sqlite'
path = os.path.join(basedir, file_name)


def create_test_database(app):
    if os.path.exists(path):
        os.remove(os.path.join(basedir, file_name))

    with app.app_context():
        db.create_all()
        for c in mock_customers:
            db.session.execute(c)
        for a in mock_accounts:
            db.session.execute(a)
        for t in mock_transfers:
            db.session.execute(t)

        db.session.commit()


