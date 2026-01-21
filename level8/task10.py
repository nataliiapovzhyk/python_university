def average_value(marks_list):
    marks_sum = 0
    for marks in marks_list:
        marks_sum += marks
    return marks_sum / len(marks_list)

marks_list = []
for i in range(10):
    marks_list.append(int(input("Введіть число в список")))

print(marks_list)
print(average_value(marks_list))