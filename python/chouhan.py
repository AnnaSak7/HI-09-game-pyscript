import random

choice = ['丁', '半']

def on_click_chohan(*args, **kwargs):
    rand = random.randint(0, 1)
    if rand == 0:
        pyscript.write('audio', "<audio src='../assets/cho.mp3' type='audio/mp3' autoplay></audio>")
        pyscript.write('result', "<img class='chohanImg' src='../assets/cho.png' alt='cho' style='width: 300px; height:300px' />")
    
    elif rand == 1:
        pyscript.write('audio', "<audio src='../assets/han.mp3' type='audio/mp3' autoplay></audio>")
        
        pyscript.write('result', "<img class='chohanImg' src='../assets/han.png' alt='han' style='width: 300px; height:300px; justify-item: center' />")  
      
    


