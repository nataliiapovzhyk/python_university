class Account:
    cout_accounts = 0
    def __init__(self, acc_number, owner):
        self.__acc_number = acc_number
        self.owner = owner
        self.__balance = 0

    def __str__(self):
        return f"Рахунок №{self.__acc_number} (Власник {self.owner}) - Баланс {self.__balance} грн"
