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

        if not handle_back_and_del(key_pressed, self._imvimModel) and not arrow_to_char(key_pressed, self._imvimModel) \
            and not char_to_arrow(key_pressed, self._imvimModel) and not handle_spacebar(key_pressed, self._imvimModel):
            # if none of the keys are detcted, insert char (will need to change later when we add more stuff)
            self._imvimModel.insert_char_at_cursor(event.char)
        

        #TESTING
        #print("player text: " + str(self._imvimModel.get_player_text()))

        # pass keys pressed to the thing displaying on the gui
        #self._imvimView.display_keypress()

        

        ### redraw gui ### <- maybe a view method, may need to make one in controller
        self._imvimView.redraw(self._imvimModel)

    # updates game state/ position of the cursor although this is done indirectly through modfiying methods
    
def main():
    root = tk.Tk()
    ImvimController(root)

if __name__ == "__main__":
    main()