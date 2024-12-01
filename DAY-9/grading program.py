student_scores = {
    "Henry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Dracula": 74,
    "Neville": 62,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    # print(score)
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expertations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)