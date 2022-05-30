import random
import os
from pkgutil import iter_modules
from telnetlib import LOGOUT

from words import words
from ascii_hangman import stages, logo

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# print(chosen_word)

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input('Guess a letter: ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print('wrong')

#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# for index in range(len(chosen_word)):
#     if chosen_word[index] == guess:
#         display[index] = guess

# print(display)

#TODO-4 - Use a while loop to let the user guess again. THe loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks("_"). Then you can tell the user they;/ve won.

#TODO-5: - Create a variable called 'lives' to keep track of the number of lives left. 
    #Set 'lives' to equal 6.

#TODO-6: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
#TODO-7: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

print(logo)

chosen_word = words[random.randint(0, len(words)+1)]

display = []
for x in range(len(chosen_word)):
    display += '_'

print(f"{' '.join(display)}")

lives = 6
end_of_game = False
guessed_letters = []

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    
    #clearing the input
    os.system("clear") 
    
    if guess in display:
            print("You have already guessed this letter.")
    elif guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
        print(f"{' '.join(display)}")
    else:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        print(f"{lives} lives left")
    
    guessed_letters.append(guess)
    if lives == 0:
        print('You lose!')
        quit()
    
    if "_" not in display:
        end_of_game = True
        print("You win!")




# def has(x):
#     for _ in range(len(x)):
#         if x[_] == '_':
#             return True

# while has(display) == True:
#     guess = input('Guess a letter: ').lower()
#     for index in range(len(chosen_word)):
#         if chosen_word[index] == guess:
#             display[index] = guess
#     print(display)

# print("You guessed everything!")



