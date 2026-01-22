
test_string = "АААВВВВВААССССДДЕЕЕААВВСС"

def compress_string(string):
    counter = 0
    prev_letter = ""
    typle = []

    for i in string:
        if i != prev_letter:
            if counter != 0:
                typle.append((prev_letter, counter))

            prev_letter = i
            counter = 1

        else:
            counter += 1
    return typle

print(compress_string(test_string))
