# import random module
import random

# assign letters/numbers/symbols to lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# take user input as integer to specify how many characters are required
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# initialise empty list
chosen_letters = []
# for loop iterates for the number of times specified by input
for i in range(nr_letters):
  # random.choice picks random letters and appends each character to the list
  chosen_letters.append(random.choice(letters))

# repeat actions for symbols
chosen_symbols = []
for i in range(nr_symbols):
  chosen_symbols.append(random.choice(symbols))

# repeat actions for numbers
chosen_numbers = []
for i in range(nr_numbers):
  chosen_numbers.append(random.choice(numbers))
    
# concatenate chosen_letters, chosen_symbols and chosen_letters into one password list
password = chosen_letters + chosen_symbols + chosen_numbers
# use random.shuffle function to shuffle characters in list
random.shuffle(password)
# use join function to join list items into a single string
joined_password = ''.join(password)
# print message
print(f"Your password is {joined_password}")