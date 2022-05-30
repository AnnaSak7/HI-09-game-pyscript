import random
import os
from pkgutil import iter_modules
from telnetlib import LOGOUT


password = 'shinobi'

my_input_field = Element('my-input-field')

def on_click(*args, **kwargs):
    input_value = my_input_field.element.value
    message = f"You said: {input_value}"
    pyscript.write('my-output', message)

