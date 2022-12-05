from init_marshmallow import ma


class TransferSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('id',
                  'amount',
                  'sending_customer',
                  'sending_account',
                  'receiving_customer',
                  'receiving_account',
                  'transfer_date')


transfer_schema = TransferSchema()
transfers_schema = TransferSchema(many=True)
