from database import db
from api.model.customer import Customer


class Account(db.Model):
    account_number = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.ForeignKey(Customer.id, ondelete='CASCADE'), nullable=False)
    balance = db.Column(db.Float(10), default=0, nullable=False)

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
