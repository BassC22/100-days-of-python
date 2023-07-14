# take in user input for height and weight
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# convert string to float
height = float(height)
weight = float(weight)

# perform bmi calculation
bmi = weight / height ** 2

# convert float into integer to display as whole number
bmi = int(bmi)

#print result by converting integer back to string
print("Your BMI is " + str(bmi))