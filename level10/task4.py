

def censor(text_to_check):
    banned_words = {"buy", "crypto", "free", "click"}

    test_set = set(text_to_check.split(" "))

    if(len(test_set.intersection(banned_words))==0):
        return True
    else:
        return False

text = input("Введіть текст: ")
if censor(text):
    print("OK")
else:
    print("BLOCK")