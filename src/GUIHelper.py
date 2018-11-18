from tkinter import *
class GUIHelper:
    def __init__(self,window,color):
        self.window=window
        self.color=color
    
    def CreateText(self,x,y,text):
        lbl=Label(self.window, text=text, bg=self.color)
        lbl.place(x=x, y=y)