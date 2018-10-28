import pickle
from tkinter import *

background="#dce0e8"
windowbg="#e8ecf2"

window=Tk()
window.title("Software 3KO4")
#window.geometry("500x500")
window.configure(bg=background)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

loginbg=Label(window,height=10,width=40,bg=windowbg,borderwidth=2,relief="ridge")
loginbg.grid(rowspan=4,columnspan=4)
#loginbg.grid_columnconfigure(0,weight=1)
#loginbg.grid_rowconfigure(0,weight=1)

exuser=Label(window,text="Existing User Login",bg=windowbg)
exuser.config(font=("Segoe UI", 13))
exuser.grid(row=0,column=1,sticky='nsew')
'''
lbl = Label(window, text="Username:",bg=windowbg)
lbl.place(relx=0.35,rely=0.45)

username=Entry(window,width=20)
username.place(relx=0.5,rely=0.45)

lbl1=Label(window,text="Password:",bg=windowbg)
lbl1.place(relx=0.35,rely=0.5)

password=Entry(window,width=20)
password.place(relx=0.5,rely=0.5)

lblQuestion=Label(window, text="Don't have an account?", bg=windowbg)
lblQuestion.place(relx=0.35,rely=0.61)

bttnClick=Button(window, text="Click here!", bg=windowbg)
bttnClick.place(relx= 0.63, rely=0.6)

login = Button(window, text="Login")
login.place(relx=0.5,rely=0.55)
'''
window.mainloop()