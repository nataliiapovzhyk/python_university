number_one = int(input("Введіть перше число: "))
number_two = int(input("Введіть друге число: "))
operator = input("Вкажіть операцію *, -, + чи /: ")

print(f"{number_one} {operator} {number_two} = ", end="")
if operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "/":
    if number_two != 0:
        print(number_one / number_two)
    else:
        print("Ділення не нуль неможливе")
else:
    print("Операція не коректна")