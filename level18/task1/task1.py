import os
import shutil

with open("rules.txt", "w") as file:
    file.write("Не списувати! Коментувати код!")

os.mkdir("Python_Course")
os.chdir("Python_Course")

for i in range(5):
    number = i +1
    os.mkdir(f"Lesson_{number}")
    os.chdir(f"Lesson_{number}")
    with open("main.py", "w") as file:
        file.write("")
    with open("info.txt", "w") as file:
        file.write(f"Це папка для уроку номер {str(number).upper()}")
    shutil.copyfile("../../rules.txt", "rules.txt")
    os.chdir("..")

