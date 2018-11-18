import sys
sys.path.insert(0,'../src')
from tkinter import *
from GUIHelper import GUIHelper
programparams=Tk()
programparams.title("Programmable Paramaters")
programparams.geometry("680x690")
background="#dce0e8"
programparams.configure(bg=background)

window=GUIHelper(programparams,background)

window.CreateText(100,100,'sup')
programparams.mainloop()
