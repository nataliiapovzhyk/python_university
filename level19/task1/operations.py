import os

import deserialize
import datetime
import json
from level19.task1.coder import CustomEncoder

def save_data_to_file():

    with open("transaction_list.json", "w") as file:
        json.dump(transaction_list, file, cls=CustomEncoder)


transaction_list = []
if not os.path.exists("transaction_list.json"):
    save_data_to_file()




def add_income():
    sum = float(input("Введіть суму: "))
    date = datetime.datetime.now()
    transaction_list.append(
        {"type": "income",
         "amount": sum, "date": date})

def add_expense():
    sum = float(input("Введіть суму: "))
    date = datetime.datetime.now()
    transaction_list.append(
        {"type": "expense",
         "amount": sum, "date": date})

def count_balance():
    sum = 0
    for transaction in transaction_list:
        if transaction["type"] == "expense":
            sum -= transaction["amount"]
        elif transaction["type"] == "income":
            sum += transaction["amount"]
    print(f"Баланс транзакцій {sum}")

def print_transactions():
    if len(transaction_list) == 0:
        print("Ще не було внесено жодної транзакції")
    for transaction in transaction_list:
        if transaction["type"] == "expense":
            print(f"{transaction["date"]} -{transaction["amount"]}грн")
        elif transaction["type"] == "income":
            print(f"{transaction["date"]} +{transaction["amount"]}грн")