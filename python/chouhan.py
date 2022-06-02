import random


choice = ['丁', '半']

def on_click_chohan(*args, **kwargs):
    rand = random.randint(0, 1)
    pyscript.write('modal-content', f"{choice[rand]}")    
    


# computer = random.randint(0, 1)


# if player == computer:
#     print(f'{choice[player]}You \n {choice[computer]} Computer \n \n Draw.')
# elif player == 0 and computer == 2:
#     print(f'{choice[player]}You \n {choice[computer]} Computer \n \n You win!')
# elif player == 1 and computer == 0:
#     print(f"{choice[player]}You \n {choice[computer]} Computer \n \n You win!")
# elif player == 2 and computer == 1:
#     print(f'{choice[player]}You \n  {choice[computer]} Computer \n \nYou win!')
# else:
#     print(f'{choice[player]}You \n {choice[computer]}Computer \n \nYou lose!')