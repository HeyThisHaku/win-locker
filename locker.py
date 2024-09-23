from pnp_controller import lock_mouse,lock_keyboard
from tkinter import *
import pyfiglet
from os import walk 
from rich.console import Console
import os
import sys

con = Console()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def show_ui():
    banner = pyfiglet.figlet_format("LOCKED",font="banner3-D")
    con.print(banner,"YOUR KEYBOARD AND MOUSE ARE LOCKED",style="bold red")
    input("")


if __name__ == "__main__":
    lock_mouse()
    lock_keyboard()
    show_ui()