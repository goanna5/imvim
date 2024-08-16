# view
import tkinter as tk
from tkinter import *
from constants import KEY_PRESS_FRAME_HEIGHT

class TextGrid(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.row_size = 60
        self.col_size = 25
        self.width = width
        self.height = height
        self.cell_width = self.width // self.row_size
        self.cell_height = self.height // self.col_size

        # TEST
        self.print_line_nums()
        self.print_line("Hello,", 1)
        self.print_line("World!", 2)

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


    def print_char(self, char: str, x: int, y: int, color="white") -> None:
        midpoint = self.get_pixel_coords(y, x)
        self.create_text(midpoint, text=char, anchor=CENTER, fill=color, font="Consolas")

    def print_line(self, line: str, row_num: int) -> None:
        for i, char in enumerate(line):
            self.print_char(char, i+4, row_num)


class ImvimView:
    def display_view(self, root):
        root.mainloop()

    def create_view(self):
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.title("Imvim")

        self.height = root.winfo_screenheight()
        self.width = root.winfo_screenwidth()

        gameFrame = Frame(root, height=self.height-KEY_PRESS_FRAME_HEIGHT, width=self.width)
        userTextFrame = TextGrid(gameFrame, self.width // 2, self.height-KEY_PRESS_FRAME_HEIGHT, background='#333333')
        taskFrame = TextGrid(gameFrame, self.width // 2, self.height-KEY_PRESS_FRAME_HEIGHT, background='#333333')
        keyPressFrame = Frame(root, background='#333333', height=KEY_PRESS_FRAME_HEIGHT, width=self.width)
        
        '''
        userTextFrame.grid(row=0, column=0, padx=5, pady=5)
        taskFrame.grid(row=0, column=1, padx=5, pady=5)
        keyPressFrame.grid(row=1, column=0, padx=5, pady=5)
        '''

        gameFrame.pack(side=TOP, fill=BOTH)
        userTextFrame.pack(side=LEFT, fill=BOTH)
        taskFrame.pack(side=RIGHT, fill=BOTH)
        keyPressFrame.pack(side=BOTTOM, fill=BOTH)

        return root
    
    def redraw(self, model):
        # model is a ImvimModel
        pass


    def update_cursor(self):
        pass

    def update_view(self):
        pass


def main():
    view = ImvimView()
    root = view.create_view()
    view.display_view(root)

if __name__ == "__main__":
    main()


