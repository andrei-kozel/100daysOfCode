# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for num in range(0, len(student_heights)):
    student_heights[num] = int(student_heights[num])
# 🚨 Don't change the code above 👆

# You are going to write a program that calculates the average student height from a List of heights.
# Write your code below this row 👇
sum_height = 0
for student in student_heights:
    sum_height += student

average_height = round(sum_height / len(student_heights))
print(average_height)
