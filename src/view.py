# view
import tkinter as tk
from tkinter import *

class ImvimView:
    def display_view(self, root):
        root.mainloop()

    def create_view(self):
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.title("Imvim")


        userTextFrame = Frame(root, background='red', width=500, height=500)
        taskFrame = Frame(root, background='green', width=500, height=500)
        keyPressFrame = Frame(root, background='yellow', width=500, height=500)
        
        userTextFrame.grid(row=0, column=0, padx=5, pady=5)
        taskFrame.grid(row=0, column=1, padx=5, pady=5)
        keyPressFrame.grid(row=1, column=0, padx=5, pady=5)

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


