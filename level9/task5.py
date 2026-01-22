winning_numbers = (15, 23, 4, 8, 42, 16)

def check_ticket(number):
    if number in winning_numbers:
        print("Виграш!")
    else:
        print("Спробуйте ще")


check_ticket(input("Введіть номер: "))