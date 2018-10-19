import pickle
from tkinter import *

background="#dce0e8"
windowbg="#e8ecf2"

window=Tk()
window.title("Software 3KO4")
window.geometry("500x500")
window.configure(bg=background)

loginbg=Label(window,height=10,width=40,bg=windowbg,borderwidth=2,relief="ridge")
loginbg.place(relx=0.3,rely=0.35)

exuser=Label(window,text="Existing User Login",bg=windowbg)
exuser.config(font=("Segoe UI", 13))
exuser.place(relx=0.44,rely=0.37)

lbl = Label(window, text="Username:",bg=windowbg)
lbl.place(relx=0.35,rely=0.45)

username=Entry(window,width=20)
username.place(relx=0.5,rely=0.45)

lbl1=Label(window,text="Password:",bg=windowbg)
lbl1.place(relx=0.35,rely=0.5)

password=Entry(window,width=20)
password.place(relx=0.5,rely=0.5)

login = Button(window, text="Login")
login.place(relx=0.45,rely=0.55)

window.mainloop()