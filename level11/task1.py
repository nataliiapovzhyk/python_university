categories = ["Laptops", "Smartphones", "Tablets", "Accessories"]
shipment = [
    ("Laptops", "MacBook Air"),
    ("Smartphones", "iPhone 15"),
    ("Laptops", "Lenovo ThinkPad"),
    ("Accessories", "Mouse"),
    ("Smartphones", "Samsung S24"),
    ("Fridges", "Bosch") # Увага: нова категорія!
]

inventory = dict.fromkeys(categories, None)

print(inventory)

for key, item in shipment:
    print(f"{key}:{item}")
    items = inventory.setdefault(key, [])
    if items is None:
        inventory[key] = []
        items = inventory[key]
    items.append(item)


print(inventory)






