from init_marshmallow import ma


class AccountSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('account_number', 'owner', 'balance')


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
