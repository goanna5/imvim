# controller
import tkinter as tk
from model import *
from view import *
from constants import *
from features import *

class ImvimController:
    def __init__(self, master: tk.Tk) -> None:
        # create model and view instances?
        self._imvimModel = ImvimModel()
        self._imvimView = ImvimView()

        self._imvimView.create_view(master)
        # TEST TEST TEST
        self._imvimView.test_redraw()

        # handle key presses 
        master.bind('<KeyPress>', self.handle_keypress)
        ### redraw gui ### <- maybe a view method, may need to make one in controller
        self._imvimView.display_view(master, self._imvimModel)

    def handle_keypress(self, event: tk.Event) -> None:
        # method to handle all the different functionality from pressing keys
        # references methods in the view
        key_pressed = event.keysym
        print(key_pressed)

        handle_back_and_del(key_pressed, self._imvimModel)

        #TESTING
        #self._imvimModel.player_text = ["abcdefg", "hijklmno"]
        #print(self._imvimModel.get_line_length(1))

        # pass keys pressed to the thing displaying on the gui
        #self._imvimView.display_keypress()

        # TEST
        self._imvimModel.insert_char_at_cursor(event.char)

        ### redraw gui ### <- maybe a view method, may need to make one in controller
        self._imvimVgit iew.redraw(self._imvimModel)

    # updates game state/ position of the cursor although this is done indirectly through modfiying methods
    
def main():
    root = tk.Tk()
    ImvimController(root)

if __name__ == "__main__":
    main()