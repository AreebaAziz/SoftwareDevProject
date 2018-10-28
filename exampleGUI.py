from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="This should be centered")
        label.grid(row=1, column=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = Tk()
    Example(root).grid(sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()