# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should
# contain student names for keys and their grades for values. The final version of the student_
# grades dictionary will be checked.


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}

for student in student_scores:
    if 100 >= student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif 90 >= student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif 80 >= student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    elif 70 >= student_scores[student]:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
