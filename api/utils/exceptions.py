class AccountDoesNotExistException(Exception):
    def __init__(self, non_existing_account: int):
        self.non_existing_customer = non_existing_account
        self.message = f'Account with id: {non_existing_account}, does not exist'
        super().__init__(self.message)


class CustomerDoesNotExistException(Exception):
    def __init__(self, non_existing_customer: int):
        self.non_existing_customer = non_existing_customer
        self.message = f'Customer with id: {non_existing_customer}, does not exist'
        super().__init__(self.message)


class CoveringNotSufficientException(Exception):
    def __init__(self):
        self.message = f"Insufficient covering"
        super().__init__(self.message)


class WrongAccountException(Exception):
    def __init__(self, customer_id, account_number):
        self.message = f'Account {account_number} does not belong customer {customer_id}'
        super().__init__(self.message)

