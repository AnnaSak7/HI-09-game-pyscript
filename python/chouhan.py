import random

computer = random.randint(0, 1)

choice = [cho, han]

if player == computer:
    print(f'{choice[player]}You \n {choice[computer]} Computer \n \n Draw.')
elif player == 0 and computer == 2:
    print(f'{choice[player]}You \n {choice[computer]} Computer \n \n You win!')
elif player == 1 and computer == 0:
    print(f"{choice[player]}You \n {choice[computer]} Computer \n \n You win!")
elif player == 2 and computer == 1:
    print(f'{choice[player]}You \n  {choice[computer]} Computer \n \nYou win!')
else:
    print(f'{choice[player]}You \n {choice[computer]}Computer \n \nYou lose!')