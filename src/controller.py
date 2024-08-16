# controller
import tkinter as tk

class Controller:
    def __init__(self, master: tk.Tk) -> None:
        # create model and view instances?

        # handle key presses 
        master.bind('<KeyPress>', self.handle_keypress)

    def handle_keypress(self, event: tk.Event) -> None:
        # method to handle all the different functionality from pressing keys
        # references methods in the view
        key_pressed = event.char.lower()

        # so far:
        if key_pressed == 'u':
            # move up
            pass
        elif key_pressed == 'd':
            # move down
            pass
        elif key_pressed == 'l':
            # move left
            pass
        elif key_pressed == 'r':
            # move right
            pass

        # decide others later

    # updates game state/ position of the cursor although this is done indirectly through modfiying methods
    