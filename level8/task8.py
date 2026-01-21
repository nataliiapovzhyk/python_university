marks_list = [4,34,563,45,60, 59, 64, 90, 23,4,88]
best_marks = []
for marks in marks_list:
    if marks > 60 or marks == 60:
        best_marks.append(marks)

print(best_marks)
