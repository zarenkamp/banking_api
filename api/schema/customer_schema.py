from init_marshmallow import ma


class CustomerSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('id', 'first_name', 'last_name')


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
