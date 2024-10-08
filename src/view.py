# view
import tkinter as tk
from tkinter import *
from constants import KEY_PRESS_FRAME_HEIGHT, TEXT_OFFSET

class TextGrid(tk.Canvas):
    def __init__(self, master, width, height, name, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.row_size = 60
        self.col_size = 25
        self.width = width
        self.height = height
        self.cell_width = self.width // self.row_size
        self.cell_height = self.height // self.col_size

        self.name = name

        self.text_colour = "white"
        self.bg_colour = "#333333"
        self.split_point = None

        # TEST
        #self.print_text(["Hello,", "World!"])

    def get_pixel_coords(self, row: int, col: int):
        x = self.cell_width * col + self.cell_width // 2
        y = self.cell_height * row + self.cell_height // 2
        return (x, y)
    
    def print_line_nums(self) -> None:
        for i in range(1, self.col_size):
            right_digit = i % 10
            left_digit = i // 10
            if left_digit:
                self.print_char(str(left_digit), 1, i, color="gray")
            self.print_char(str(right_digit), 2, i, color="gray")

    def draw_cursor(self, cursor_pos) -> None:
        # Note: The cursor does not blink because that would require a timer
        cursor_x, cursor_y = cursor_pos
        x = (cursor_x+TEXT_OFFSET)*self.cell_width
        y = (cursor_y+1)*self.cell_height
        self.create_line(x,y,x,y+self.cell_height, fill="white", width=3)

    def draw_heading(self, level) -> None:
        line = self.name + "_level_" + str(level) + ".txt"
        self.print_line(line, 0)
        x1 = 0
        x2 = self.width
        y = self.cell_height
        self.create_line(x1,y,x2,y, fill="#555555", width=2)

    def redraw_heading(self, level) -> None:
        self.create_rectangle(0,0, self.width, self.cell_height, fill=self.bg_colour)
        line = self.name + "_level_" + str(level) + ".txt"
        self.print_line(line, 0)

    def print_char(self, char: str, x: int, y: int, color: str) -> None:
        """if self.split_point == (x-TEXT_OFFSET, y-1):
            self.text_colour = "white"
            color = "white"""
        midpoint = self.get_pixel_coords(y, x)
        self.create_text(midpoint, text=char, anchor=CENTER, fill=color, font="Consolas")

    def print_line(self, line: str, row_num: int) -> None:
        for i, char in enumerate(line):
            self.print_char(char, i+TEXT_OFFSET, row_num, self.text_colour)

    def print_text(self, text) -> None:
        for i, line in enumerate(text):
            self.print_line(line, i+1)

    def draw(self, text, level, cursor_pos=None) -> None:
        self.create_rectangle(0, 0, self.width, self.height, fill=self.bg_colour)
        self.print_line_nums()
        # self.split_point = split_point
        #self.text_colour = "white"
        self.draw_heading(level)
        self.print_text(text)
        if cursor_pos:
            # draw cursor
            self.draw_cursor(cursor_pos)

    def redraw_line(self, row_num, text) -> None:
        x1 = TEXT_OFFSET*self.cell_width-10
        y1 = (row_num)*self.cell_height
        x2 = self.width
        y2 = (1+row_num)*self.cell_height+2
        self.create_rectangle(x1, y1, x2, y2, fill=self.bg_colour, width=0)
        self.print_line(text, row_num)

    def redraw_text_area(self, min_row, text, cursor_pos) -> None:
        x1 = TEXT_OFFSET*self.cell_width - 1
        y1 = (1+min_row)*self.cell_height
        x2 = self.width
        y2 = self.height
        self.create_rectangle(x1, y1, x2, y2, fill=self.bg_colour, width=0)
        for i in range(min_row, len(text)):
            self.print_line(text[i], i+1)
        self.draw_cursor(cursor_pos)


    def redraw(self, text, prior_cursor=None, cursor_pos=None) -> None:
        # self.split_point = split_point
        if cursor_pos != None:
            # remove cursor from previous position
            if prior_cursor != None:
                #this checks that text is not empty (i.e. terminal is not blank)
                #would be better to just insert the empty string, 
                #however not sure if that would break something else, 
                #so have not yet
                if text:
                    self.redraw_line(prior_cursor[1]+1, text[prior_cursor[1]])
                else:
                    self.redraw_line(prior_cursor[1]+1, "")
            # draw cursor
            if text:
                self.redraw_line(cursor_pos[1]+1, text[cursor_pos[1]])
            else:
                self.redraw_line(cursor_pos[1]+1, "")
            self.draw_cursor(cursor_pos)

    def redraw_num_lines(self, num_lines, text) -> None:
        #Redraw line from first line up to number of lines
        for i in range(1, num_lines + 1):
            self.redraw_line(i, text)

    def draw_success_box(self, last_level) -> None:
        box_width = 600
        box_height = 300
        x1 = (self.width - box_width) // 2
        x2 = (self.width + box_width) // 2
        y1 = (self.height - box_height) // 2
        y2 = (self.height + box_height) // 2
        self.create_rectangle(x1, y1, x2, y2, fill="white", width=5)
        mid_x = self.width // 2
        mid_y = self.height // 2
        self.create_text((mid_x, mid_y-50), text="CONGRATULATIONS!", anchor=CENTER, fill="black", font=("Consolas", 28))
        if last_level:
            self.create_text((mid_x, mid_y+50), text="You completed all the levels :)", anchor=CENTER, fill="black", font=("Consolas", 28))
        else:
            self.create_text((mid_x, mid_y+50), text="Press any key to continue.", anchor=CENTER, fill="black", font=("Consolas", 28))
        



class KeyPressFrame(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.capacity = 10
    
    def clear(self) -> None:
        self.delete('all')
    
    def redraw(self, keys) -> None:
        # keys should be a list of strings
        self.clear()
        square_height = 75
        for i in range(self.capacity):
            if i > 0 and (i >= len(keys) or keys[-i] == " "):
                return
            this_key = keys[-i]
            cell_width = self.width // self.capacity
            center_x = i*cell_width + cell_width//2
            center_y = self.height // 2

            y1 = center_y - square_height//2
            y2 = y1 + square_height
            if i == 0:
                self.create_text((center_x+10, center_y), text="Key History:", anchor=CENTER, font="Arial", fill="white")
                continue
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
            if len(this_key) == 1:
                this_key = this_key.upper()
            self.create_text((center_x, center_y), text=this_key, anchor=CENTER, font="Arial")

    def init_redraw(self) -> None:
        self.create_text(self.width//2, self.height//2, text="Your keypress history will go here, most recent to the left", anchor=CENTER, font=("Arial", 16), fill="white")


class ImvimView:
    def display_view(self, root):
        """self.userTextFrame.draw(model.get_player_text(), model.get_level(), model.get_cursor_coords())
        self.taskFrame.draw(model.get_goal_text(), model.get_level())"""
        root.mainloop()

    def create_view(self, root):
        root.attributes('-fullscreen', True)
        root.title("Imvim")

        self.height = root.winfo_screenheight()
        self.width = root.winfo_screenwidth()

        self.gameFrame = Frame(root, height=self.height-KEY_PRESS_FRAME_HEIGHT,
                               width=self.width)
        self.userTextFrame = TextGrid(self.gameFrame, self.width // 2,
                                      self.height-KEY_PRESS_FRAME_HEIGHT, "user",
                                      background='#333333')
        self.taskFrame = TextGrid(self.gameFrame, self.width // 2,
                                  self.height-KEY_PRESS_FRAME_HEIGHT, "goal",
                                  background='#333333')
        self.keyPressFrame = KeyPressFrame(root, background='#555555',
                                   height=KEY_PRESS_FRAME_HEIGHT,
                                   width=self.width)
        

        self.gameFrame.pack(side=TOP, fill=BOTH)
        self.userTextFrame.pack(side=LEFT, fill=BOTH)
        self.taskFrame.pack(side=RIGHT, fill=BOTH)
        self.keyPressFrame.pack(side=BOTTOM, fill=BOTH)
    
    def redraw(self, model, prior_cursor):
        # model is a ImvimModel
        cursor_pos = model.get_cursor_coords()
        #split_point = model.get_last_correct_char()
        #split_point = (0,0)
        user_text = model.get_player_text()
        print("Player text: ")
        print(user_text)
        self.userTextFrame.redraw(user_text, prior_cursor=prior_cursor, cursor_pos=cursor_pos)

        #goal_text = model.get_goal_text()
        #self.taskFrame.redraw(goal_text, split_point=split_point)
        self.keyPressFrame.redraw(model.get_historical_keypress())

    def redraw_section(self, num_lines, text):
        self.userTextFrame.redraw_num_lines(num_lines, text)

    """def initial_redraw(self):
        # redraws initially
        cursor_pos = (20, 1)
        split_point = (10,1)
        user_text = ["This is an example of", "what the game could look like."]
        self.userTextFrame.redraw(user_text, cursor_pos=cursor_pos, split_point=split_point)

        goal_text = ["This is an example of", "what the goal output could be."]
        self.taskFrame.redraw(goal_text, split_point=split_point)

        self.keyPressFrame.init_redraw()"""

    def draw_new_level(self, model):
        level = model.get_level()
        user_text = model.get_player_text()
        task_text = model.get_goal_text()
        # split_point = model.get_last_correct_char()
        # self.taskFrame.draw(task_text, level, split_point)
        # self.userTextFrame.draw(user_text, level, split_point, model.get_cursor_coords())
        self.taskFrame.draw(task_text, level)
        self.userTextFrame.draw(user_text, level, model.get_cursor_coords())
        self.keyPressFrame.clear()

    def draw_success_message(self, last_level):
        self.userTextFrame.draw_success_box(last_level)