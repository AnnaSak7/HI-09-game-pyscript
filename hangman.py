from mimetypes import guess_all_extensions
import random

# from ascii_hangman import stages, logo

words = ['sakura', 'kiku', 'ran', 'botan']



chosen_word = words[random.randint(0, 3)]


display = []
for x in range(len(chosen_word)):
    display += '_'

pyscript.write('msg', f'Guess a letter {chosen_word}')

pyscript.write('unknown-letters', f"{' '.join(display)}")

letter_input = Element('letter_input')

def on_click_letter(*args, **kwargs):
    input_value = letter_input.element.value
    pyscript.write('response', f"guessed letter is {input_value}")
    for index in range(len(chosen_word)):
        if chosen_word[index] == input_value:
            display[index] = input_value
    pyscript.write('unknown-letters', f"{' '.join(display)}")

            

# end_of_game = False
# guessed_letters = []

# while not end_of_game:
#     guess = letter_input.element.value
    
#     if guess in chosen_word:
#         for index in range(len(chosen_word)):
#             if chosen_word[index] == guess:
#                 display[index] = guess
        # pyscript.write('unknown-letters', f"{' '.join(display)}")

#     if guess in display:
#            print("You have already guessed this letter.")
#     elif guess in chosen_word:
#         for index in range(len(chosen_word)):
#             if chosen_word[index] == guess:
#                 display[index] = guess
#         print(f"{' '.join(display)}")
#     else:
#         lives-=1
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         print(stages[lives])
#         print(f"{lives} lives left")
    
#     guessed_letters.append(guess)
#     if lives == 0:
#         print('You lose!')
#         quit()
    
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")

