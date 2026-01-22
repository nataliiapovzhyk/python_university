numbers = [5, 12, 7, 10, 1, 45, 8, 43]

def split_numbers(numbers):
    odd_numbers = []
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    typle = (odd_numbers, even_numbers)
    return typle


print(split_numbers(numbers))


