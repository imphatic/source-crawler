students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39], ['Steve', 39]]

students.sort(key=lambda x: x[1])

lowest = students[0][1]
second_lowest = 0
second_lowest_students = []

for student in students:
    score = student[1]
    second_lowest = score if second_lowest == 0 and score > lowest else second_lowest

    if score == second_lowest:
        second_lowest_students.append(student[0])

print(*sorted(second_lowest_students), sep='\n')

