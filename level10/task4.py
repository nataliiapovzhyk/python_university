

def censor(text_to_check):
    banned_words = {"buy", "crypto", "free", "click"}
    words = set(text_to_check.lower().split())
    return len(words.intersection(banned_words))==0

text = input("Введіть текст: ")
if censor(text):
    print("OK")
else:
    print("BLOCK")