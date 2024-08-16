# view
import tkinter as tk
from tkinter import *
from constants import KEY_PRESS_FRAME_HEIGHT

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
        userTextFrame = Frame(gameFrame, background='red', height=self.height-KEY_PRESS_FRAME_HEIGHT, width = self.width // 2)
        taskFrame = Frame(gameFrame, background='green', height=self.height-KEY_PRESS_FRAME_HEIGHT, width = self.width // 2)
        keyPressFrame = Frame(root, background='yellow', height=KEY_PRESS_FRAME_HEIGHT, width=self.width)
        
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


