rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# import random module
import random

# assign game images to list corresponding with choices
game_images = [rock, paper, scissors]

# take in user input as integer
user_choice = int(input("What do you choose? Enter 0 for Rock, 1 for Paper or 2 for for Scissors:\n"))
# check that user input is 0, 1 or 2 before checking any other conditions, and print error message if applicable
if user_choice < 0 or user_choice >= 3:
  print("You typed an invalid number, you lose")
else:
  # print corresponding image from list
  print(game_images[user_choice])
  # generate random number between 0 and 2 as computer_choice
  computer_choice = random.randint(0, 2)
  print("Computer chose")
  #print corresponding image from list
  print(game_images[computer_choice])

  # check for conditions and print relevant message
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")