import random


choice = ['丁', '半']

def on_click_chohan(*args, **kwargs):
    rand = random.randint(0, 1)
    pyscript.write('modal-content', f"{choice[rand]}")    
    


