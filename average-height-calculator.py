# input heights and split
student_heights = input("Input a list of student heights ").split()
# store heights in a list and convert into integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# initialise total_height to 0 and loop through student_heights list and add each height to the running total
total_height = 0
for height in student_heights:
  total_height += height

# initialise number_of_students to 0 and loop through student_heights list to get the number of items in the list
number_of_students = 0
for student in student_heights:
  number_of_students += 1

# calculate average, round to nearest whole number and print
average_height = round(total_height / number_of_students)
print(average_height)