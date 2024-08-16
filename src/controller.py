# controller
import tkinter as tk
from model import *
from view import *
from constants import *

class ImvimController:
    def __init__(self, master: tk.Tk) -> None:
        # create model and view instances?
        self._imvimModel = ImvimModel()
        self._imvimView = ImvimView()

        # handle key presses 
        master.bind('<KeyPress>', self.handle_keypress)
        ### redraw gui ### <- maybe a view method, may need to make one in controller

    def handle_keypress(self, event: tk.Event) -> None:
        # method to handle all the different functionality from pressing keys
        # references methods in the view
        key_pressed = event.char.lower()

        # pass keys pressed to the thing displaying on the gui
        self._imvimView.display_keypress()


        # so far:
        if key_pressed == UP:
            # move up
            self._imvimModel.move_cursor(UP[0], UP[1])

        elif key_pressed == DOWN:
            # move down
            self._imvimModel.move_cursor(DOWN[0], DOWN[1])

        elif key_pressed == LEFT:
            # move left
            self._imvimModel.move_cursor(LEFT[0], LEFT[1])

        elif key_pressed == RIGHT:
            # move right
            self._imvimModel.move_cursor(RIGHT[0], RIGHT[1])

        # decide others later

        ### redraw gui ### <- maybe a view method, may need to make one in controller

    # updates game state/ position of the cursor although this is done indirectly through modfiying methods
    