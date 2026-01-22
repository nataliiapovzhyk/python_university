def clean_test(text):
    return (text.replace(",", "")
            .replace(".", "")
            .replace("?", "")
            .replace("!", ""))

def words_stat(words_list):
    length = len(words_list)
    if length == 0:
        print("Тексту не знайдено.")
        return 0
    print(f"Загальна кількіть слів: {length}")

    word_long = ""
    word_short = ""
    max = 0
    min = 2000
    total_length = 0
    parazit = False
    for word in words_list:

        if word == "ну" or word == "коротше":
            parazit = True


        total_length += len(word)
#пошук максимального слова
        if len(word) > max:
            word_long = word
            max = len(word)

#пошук мінімального слова
        if len(word) < min:
            word_short = word
            min = len(word)

    average_length = round(total_length / length, 2)

    if parazit: print("Знайдено слова паразити!")
    print("Найдовше слово: " + word_long)
    print("Найкоротше слово: " + word_short)
    print(f"Середня довжина слова: {average_length}")


def count_letters(text):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    golosni = []
    prigolosni = []

    for i in range (0, len(text)):
        if text[i] in vowels:
            golosni.append(text[i])
        else:
            prigolosni.append(text[i])

    print(f"Кількість голосних: {len(golosni)}")
    print(f"Кількість приголосних: {len(prigolosni)}")



text = input("Введіть текст для аналізу: ")
text = clean_test(text)
words_list = text.split()

words_stat(words_list)

letters = text.replace(" ", "")
count_letters(letters)


