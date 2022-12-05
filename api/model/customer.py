from database import db


class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    db.UniqueConstraint('first_name', 'last_name')
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
