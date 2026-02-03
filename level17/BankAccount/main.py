from level17.BankAccount import InvalidAmountError, InsufficientFundsError
from models import Account
from operations import deposit
from operations import withdraw


def start_banking():
    print("Start Banking")
    account_one = Account(1,"Test Name")
    try:
        deposit(account_one,600)
        deposit(account_one, 200)

        withdraw(account_one, 100)
        withdraw(account_one, 300)
        withdraw(account_one, 700)
    except InvalidAmountError as e:
        print(e)
    except InsufficientFundsError as e:
        print(e)

    print(account_one)

start_banking()