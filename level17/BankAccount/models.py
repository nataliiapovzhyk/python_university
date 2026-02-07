class Account:
    cout_accounts = 0
    def __init__(self, acc_number, owner):
        self.__acc_number = acc_number
        self.owner = owner
        self.__balance = 0

    @property
    def acc_number(self):
        return self.__acc_number

    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, value: float):
        print("Setting balance")
        self.__balance = value

    def __str__(self):
        return f"Рахунок №{self.__acc_number} (Власник {self.owner}) - Баланс {self.__balance} грн"

