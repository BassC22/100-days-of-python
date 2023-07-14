# take in user input for student_scores then split into list of numbers
student_scores = input("Input a list of student scores ").split()
# convert into integers by using for loop to iterate over each number
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# initialise high_score to 0
high_score = 0
# for loop to loop through each score and compare it to the previous score. If it is greater than the last, it is assigned to high_score
for score in student_scores:
    if score > high_score:
        high_score = score
# print out message
print(f"The highest score in the class is: {high_score}")