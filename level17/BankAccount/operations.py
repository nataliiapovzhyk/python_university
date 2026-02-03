from level17.BankAccount import InvalidAmountError
from level17.BankAccount import InsufficientFundsError


def validate_transaction(func):
    def wrapper(*args, **kwargs):
        print(f"Validating transaction for value: {args[1]}")

        if not isinstance(args[1], (int, float)):
            raise InvalidAmountError(args[1])
        elif args[1]<0 :
            raise InvalidAmountError(args[1])
        else:
            print("Validation Passed")
        func(*args, **kwargs)
    return wrapper

@validate_transaction
def deposit(account, value):
    account._set_balance(account.balance+value)
    print("Deposit Successful")

@validate_transaction
def withdraw(account, value):
    if account.balance < value:
        raise InsufficientFundsError(account.balance)
    else:
        print("Withdraw Validation Successful")
    account._set_balance(account.balance-value)
    print("Withdraw was Successful")
