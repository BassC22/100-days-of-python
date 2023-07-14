# set up range to check numbers up to 100 inclusive
for number in range(1, 101):
    # check if number divisible by both 3 and 5 first as priority and print FizzBuzz if true
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    # check if number divisible by 3 and print Fizz if true
    elif number %3 == 0:
        print("Fizz")
    # check if number divisible by 5 and print Buzz if true
    elif number %5 == 0:
        print("Buzz")
    # print all other numbers as actual numbers
    else:
        print(number)