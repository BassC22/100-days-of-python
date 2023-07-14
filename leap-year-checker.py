# take in user input for year
year = int(input("Which year do you want to check? "))

# use if-else statements to determine if year is leap
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    else:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
else:
    print("Not leap year.")


