import string


def is_pangram(text):
    letters_set = set(text.lower().replace(" ",""))
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(letters_set)

#The quick brown fox jumps over the lazy dog.

print(is_pangram(input("Please enter text: ")))