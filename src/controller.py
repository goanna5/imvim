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
        self._imvimWindow = master

        self._imvimView.create_view(master)
        # TEST TEST TEST
        #self._imvimView.initial_redraw()
        self._imvimView.draw_new_level(self._imvimModel)

        # handle key presses 
        master.bind('<KeyPress>', self.handle_keypress)
        ### redraw gui ### <- maybe a view method, may need to make one in controller
        self._imvimView.display_view(master)

    def handle_keypress(self, event: tk.Event) -> None:
        # method to handle all the different functionality from pressing keys
        # references methods in the view
        prior_cursor = self._imvimModel.get_cursor_coords()
        key_pressed = event.keysym
        print(key_pressed)

        # We should probably make this not as gross eventually vv
        if not handle_back_and_del(key_pressed, self._imvimModel) and not char_to_arrow(key_pressed, self._imvimModel) \
            and not handle_spacebar(key_pressed, self._imvimModel) and not handle_tab(key_pressed, self._imvimModel) \
            and not handle_enter(key_pressed, self._imvimModel) and not handle_numbers(key_pressed, self._imvimModel) \
            and not convert_space(key_pressed, self._imvimModel) and not regular_char_to_char(key_pressed, self._imvimModel) \
            and not regular_char_to_char(key_pressed, self._imvimModel) and not handle_force_quit(key_pressed, self._imvimWindow):
            # if none of the keys are detcted, insert char (will need to change later when we add more stuff)
            self._imvimModel.insert_char_at_cursor(event.char)
        

        #TESTING
        #print("player text: " + str(self._imvimModel.get_player_text()))

        # pass keys pressed to the thing displaying on the gui
        #self._imvimView.display_keypress()
        self._imvimModel.set_historical_keypress(key_pressed)
        print(self._imvimModel.get_historical_keypress())

        
        # DETERMINE IF LEVEL IS BEATEN
        if self._imvimModel.is_level_beaten():
            # level has been beaten

            # TEST TEST 
            """ TEST TEST """
            self._imvimModel.start_next_level()
            self._imvimView.draw_new_level(self._imvimModel)
            for i in range(10):
                self._imvimModel.set_historical_keypress(" ")

            print("new level started")
            #self._imvimModel.player_text = ["I win the level teehee"]

        ### redraw gui ### <- maybe a view method, may need to make one in controller
        if self._imvimModel.need_to_redraw:
            # redraw the entire text area
            # print("redrawing whole thing")
            # self._imvimView.userTextFrame.redraw_text_area(self._imvimModel.get_cursor_coords()[1], self._imvimModel.get_player_text())
            self._imvimView.userTextFrame.redraw_text_area(0, self._imvimModel.get_player_text(), self._imvimModel.get_cursor_coords())
        self._imvimView.redraw(self._imvimModel, prior_cursor)

    # updates game state/ position of the cursor although this is done indirectly through modfiying methods
    
def main():
    root = tk.Tk()
    ImvimController(root)

if __name__ == "__main__":
    main()
