from level17.BankAccount import InvalidAmountError, InsufficientFundsError
from models import Account
from operations import deposit
from operations import withdraw


def start_banking():
    try:
        account_one = Account(1, "Test Name")

        isConnect = True

        while isConnect:
            print("")
            print("============")
            print("Hello to Bank Account:")
            print("1. Deposit Account")
            print("2. Withdraw Account")
            print("3. Show Balance")
            print("4. Exit")
            print("============")
            print("")

            selected_menu = int(input("Select a menu option: "))
            if selected_menu == 1:
                value = int(input("Enter a sum to deposit: "))
                deposit(account_one, value)
            elif selected_menu == 2:
                value = int(input("Enter a sum to withdraw: "))
                withdraw(account_one, value)
            elif selected_menu == 3:
                print(account_one)
            elif selected_menu == 4:
                isConnect = False

    except ValueError as e:
        print(e)
    except InvalidAmountError as e:
        print(e)
    except InsufficientFundsError as e:
        print(e)

    print(account_one)

start_banking()