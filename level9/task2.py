def clean_names(names):
    corrected_names = []
    for name in names:
        corrected_names.append(name.strip().capitalize())
    return corrected_names


test_names = [
    "аНнА",
    "оЛекСаНдР",
    "мАРіЯ",
    "дМиТрО",
    "іРиНа",
    "бОгДаН",
    "вІкТоР",
    "нАтаЛіЯ",
    "сЕрГіЙ",
    "кАтЕрИНа"
]
corrected_names = clean_names(test_names)
print(corrected_names)