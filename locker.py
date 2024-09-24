from pnp_controller import lock_mouse,lock_keyboard
from tkinter import *
import pyfiglet
import os
import sys

text = """
 ##::::::::'#######:::'######::'##:::'##:'########:'########::
 ##:::::::'##.... ##:'##... ##: ##::'##:: ##.....:: ##.... ##:
 ##::::::: ##:::: ##: ##:::..:: ##:'##::: ##::::::: ##:::: ##:
 ##::::::: ##:::: ##: ##::::::: #####:::: ######::: ##:::: ##:
 ##::::::: ##:::: ##: ##::::::: ##. ##::: ##...:::: ##:::: ##:
 ##::::::: ##:::: ##: ##::: ##: ##:. ##:: ##::::::: ##:::: ##:
 ########:. #######::. ######:: ##::. ##: ########: ########::
........:::.......::::......:::..::::..::........::........:::
 YOUR KEYBOARD AND MOUSE ARE LOCKED
"""

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def show_ui():
    print(text)
    input("Press enter for close this prompt, Tools Credit by Haku, Maintain w/ NA")


if __name__ == "__main__":
    lock_keyboard()
    lock_mouse()
    show_ui()