class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    """Класс для пользовательского исключения при отрицательном значении."""

    def __init__(self, value, message="недостатньо коштів"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'

class InvalidAmountError(BankError):
    def __init__(self, value, message="сума менша за нуль або не число"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'

class AccountLockedError(BankError):
    def __init__(self, value, message="рахунок заморожений"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'