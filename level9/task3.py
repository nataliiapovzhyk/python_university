products = [
    ("Хліб", 25),
    ("Молоко", 38),
    ("Яйця", 72),
    ("Сир", 140),
    ("Масло", 95),
    ("Цукор", 42),
    ("Борошно", 50),
    ("Кава", 210),
    ("Чай", 85),
    ("Шоколад", 60)
]

def calculate_total(cart):
    total_price = 0
    for name, price in cart:
        total_price += price

    return total_price

print(calculate_total(products))
