from datetime import datetime

from api.model.customer import Customer
from database import db
from api.model.account import Account


class Transfer(db.Model):

    transfer_id = db.Column(db.Integer, primary_key=True)
    sending_customer = db.Column(db.ForeignKey(Customer.id), nullable=False)
    sending_account = db.Column(db.ForeignKey(Account.account_number), nullable=False)
    receiving_customer = db.Column(db.ForeignKey(Customer.id), nullable=False)
    receiving_account = db.Column(db.ForeignKey(Account.account_number), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transfer_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, sending_customer, sending_account, receiving_customer, receiving_account, amount):
        self.sending_customer = sending_customer
        self.sending_account = sending_account
        self.receiving_customer = receiving_customer
        self.receiving_account = receiving_account
        self.amount = amount
