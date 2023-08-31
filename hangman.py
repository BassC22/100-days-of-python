# Import random module
# Import files for art and word list
import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
print(logo)

# Assign random choice from word_list to chosen_word
chosen_word = random.choice(word_list)


#Create blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"

# Initialise end_of_game, livesa and guessed_letters (the latter as an empty list)
end_of_game = False
lives = 6
guessed_letters = []

# While loop to let the user guess again. The loop stops once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while not end_of_game:
  print(f"{' '.join(display)}")
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already correctly guessed {guess}. Please try another letter.")
  else:
    # Add guess to guessed_letters list
    guessed_letters.append(guess)
    print(f"You have tried the following letters: {guessed_letters}")

    
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter


  if guess not in chosen_word:
    print(f"You have guessed {guess}. You lose a life.")
    lives = lives -1
    if lives == 0:
      end_of_game = True
      print(f"You lose. The word was {chosen_word}")
  
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You have won!")

  print(stages[lives])