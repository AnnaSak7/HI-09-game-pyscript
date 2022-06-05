from mimetypes import guess_all_extensions
import random

# from ascii_hangman import stages, logo

words = ['sakura', 'kiku', 'botan', 'tsubaki', 'fuji', 'ume']
kanji = ['桜','菊','牡丹', '椿', '藤', '梅']

hints = ['Cherry blossom', 'Chrysanthemum', 'Paeonia suffruticosa', 'Camellia', 'Wisteria floribunda', 'Plum blossom']

index = random.randint(0, 3)
chosen_word = words[index]

display = []
for x in range(len(chosen_word)):
    display += '_'


pyscript.write('unknown-letters', f"{' '.join(display)}")
pyscript.write('hint', f"Hint: {hints[index]}")
letter_input = Element('letter_input')

def on_click_letter(*args, **kwargs):
    input_value = letter_input.element.value
    for index in range(len(chosen_word)):
        if chosen_word[index] == input_value.lower():
            display[index] = input_value.lower()
    pyscript.write('unknown-letters', f"{' '.join(display)}")
    # pyscript.write('key', f"{chosen_word} & {' '.join(display)}You did it! Change shinobi.html to sakura.html in the url.")
    letter_input.element.value = ""
    
    correct = ''.join(display)
    if correct == chosen_word:
        print('you did it')
        pyscript.write('hint', "")
        pyscript.write('key', f"<div class='modal-hana'><div class='modal-hana-content'><p>{kanji[words.index(chosen_word)]}</p><p id='modal-hana-content'>You did it! Click <strong style='color: orange'>HERE!</strong></p></div>")


    
    

