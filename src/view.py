# view
import tkinter as tk
from tkinter import *
from constants import KEY_PRESS_FRAME_HEIGHT, TEXT_OFFSET

class TextGrid(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.row_size = 60
        self.col_size = 25
        self.width = width
        self.height = height
        self.cell_width = self.width // self.row_size
        self.cell_height = self.height // self.col_size

        self.text_color = "lime"
        self.split_point = None

        # TEST
        self.print_line_nums()
        #self.print_text(["Hello,", "World!"])

    def get_pixel_coords(self, row: int, col: int):
        x = self.cell_width * col + self.cell_width // 2
        y = self.cell_height * row + self.cell_height // 2
        return (x, y)
    
    def print_line_nums(self) -> None:
        for i in range(self.col_size):
            right_digit = (i+1) % 10
            left_digit = (i+1) // 10
            if left_digit:
                self.print_char(str(left_digit), 1, i, color="gray")
            self.print_char(str(right_digit), 2, i, color="gray")

    def draw_cursor(self, cursor_pos) -> None:
        # Note: The cursor does not blink because that would require a timer
        cursor_x, cursor_y = cursor_pos
        x = cursor_x*self.cell_width
        y = cursor_y*self.cell_height
        self.create_line(x,y,x,y+self.cell_height, fill="white", width=3)


    def print_char(self, char: str, x: int, y: int, color: str) -> None:
        if self.split_point == (x-TEXT_OFFSET, y):
            self.text_color = "white"
            color = "white"
        midpoint = self.get_pixel_coords(y, x)
        self.create_text(midpoint, text=char, anchor=CENTER, fill=color, font="Consolas")

    def print_line(self, line: str, row_num: int) -> None:
        for i, char in enumerate(line):
            self.print_char(char, i+TEXT_OFFSET, row_num, self.text_color)

    def print_text(self, text) -> None:
        for i, line in enumerate(text):
            self.print_line(line, i)

    def redraw(self, text, cursor_pos=None, split_point=None) -> None:
        self.split_point = split_point
        self.print_text(text)
        if cursor_pos:
            # draw cursor
            self.draw_cursor(cursor_pos)


"""class UserTextFrame(TextGrid):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width, height, "white", **kwargs)

class TaskTextFrame(TextGrid):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width, height, "lime", **kwargs)"""

class KeyPressFrame(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.capacity = 10
    
    def redraw(self, keys) -> None:
        # keys should be a list of strings
        square_height = 75
        for i in range(self.capacity):
            if i >= len(keys):
                return
            this_key = keys[i]
            cell_width = self.width // self.capacity
            center_x = self.width - i*cell_width - cell_width//2
            center_y = self.height // 2

            y1 = center_y - square_height//2
            y2 = y1 + square_height
            if len(this_key) == 1:
                # single char -> square box
                x1 = center_x - square_height//2
                x2 = x1 + square_height
                self.create_rectangle(x1, y1, x2, y2, fill="white")
            else:
                # multiple chars -> rectangle box
                x1 = center_x - (4*square_height)//5
                x2 = x1 + (8*square_height)//5
                self.create_rectangle(x1, y1, x2, y2, fill="white")
            self.create_text((center_x, center_y), text=this_key, anchor=CENTER, font="Arial")

class ImvimView:
    def display_view(self, root):
        root.mainloop()

    def create_view(self):
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.title("Imvim")

        self.height = root.winfo_screenheight()
        self.width = root.winfo_screenwidth()

        self.gameFrame = Frame(root, height=self.height-KEY_PRESS_FRAME_HEIGHT,
                               width=self.width)
        self.userTextFrame = TextGrid(self.gameFrame, self.width // 2,
                                      self.height-KEY_PRESS_FRAME_HEIGHT,
                                      background='#333333')
        self.taskFrame = TextGrid(self.gameFrame, self.width // 2,
                                  self.height-KEY_PRESS_FRAME_HEIGHT,
                                  background='#333333')
        self.keyPressFrame = KeyPressFrame(root, background='#555555',
                                   height=KEY_PRESS_FRAME_HEIGHT,
                                   width=self.width)
        

        self.gameFrame.pack(side=TOP, fill=BOTH)
        self.userTextFrame.pack(side=LEFT, fill=BOTH)
        self.taskFrame.pack(side=RIGHT, fill=BOTH)
        self.keyPressFrame.pack(side=BOTTOM, fill=BOTH)

        return root
    
    def redraw(self, model):
        # model is a ImvimModel
        cursor_pos = model.get_cursor_coords()
        split_point = model.get_last_correct_char()
        user_text = model.get_player_text()
        self.userTextFrame.redraw(user_text, cursor_pos=cursor_pos, split_point=split_point)

        goal_text = model.get_goal_text()
        self.taskFrame.redraw(goal_text, split_point=split_point)

    def test_redraw(self):
        # DELETE THIS WHOLE METHOD - FOR TESTING PURPOSES ONLY
        cursor_pos = (20, 1)
        split_point = (10,1)
        user_text = ["This is an example of", "what the game could look like."]
        self.userTextFrame.redraw(user_text, cursor_pos=cursor_pos, split_point=split_point)

        goal_text = ["This is an example of", "what the goal output could be."]
        self.taskFrame.redraw(goal_text, split_point=split_point)

        self.keyPressFrame.redraw(["E", "D", "C", "B", "A", "SPACE", "H", "BACK", "SHIFT", "SPACE"])


def main():
    view = ImvimView()
    root = view.create_view()
    # TEST TEST TEST
    view.test_redraw()
    view.display_view(root)

if __name__ == "__main__":
    main()