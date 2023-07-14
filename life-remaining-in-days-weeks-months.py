# take user's age as input
age = input("What is your current age? ")

# calculate current age in days, weeks and months by converting to integer and multiplying
age_in_days = int(age) * 365
age_in_weeks = int(age) * 52
age_in_months = int(age) * 12

# calculate expected age (90) in days, weeks and months
ninety_in_days = 90 * 365
ninety_in_weeks = 90 * 52
ninety_in_months = 90 * 12

# subtract current age from expected age in days, weeks and months
time_left_in_days = ninety_in_days - age_in_days
time_left_in_weeks = ninety_in_weeks - age_in_weeks
time_left_in_months = ninety_in_months - age_in_months

# create f-string to display message
print(f"You have {time_left_in_days} days, {time_left_in_weeks} weeks, and {time_left_in_months} months left.")
