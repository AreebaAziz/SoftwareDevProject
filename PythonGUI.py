import pickle
from tkinter import *
import os

background="#dce0e8"
existingUserbg="#e8ecf2"
newUserbg = "#e8ecf2"
programparamsbg = "#e8ecf2"

users={} #only run once to create blank dict of users

# WINDOW AFTER LOGGED IN *****************************************************************************************
def onClickLogin(existingUser):
    existingUser.destroy()
    programparams=Tk()
    programparams.title("Programmable Paramaters")
    programparams.geometry("700x690")
    programparams.configure(bg=background)

    #param1
    def param1():
        lbl1 = Label(programparams, text="p_pacingState:", bg=programparamsbg)
        lbl1.place(x=45, y=40)
        lbl1entry = Entry(programparams, width=20)
        lbl1entry.place(x=195, y=38)
        unit1 = Label(programparams, text = "(y_pacingState)", bg=background)
        unit1.place(x=390, y=40)
        bttn1 = Button(programparams, text="OK", width=8, bg=programparamsbg, command=lambda: check1(lbl1entry.get(), programparams, bttn1, param1))
        bttn1.place(x=500, y=41)

    # param2
    def param2():
        lbl2 = Label(programparams, text="p_pacingMode:", bg=programparamsbg)
        lbl2.place(x=45, y=70)
        lbl2entry = Entry(programparams, width=20)
        lbl2entry.place(x=195, y=68)
        unit2 = Label(programparams, text = "(y_pacingMode)", bg=background)
        unit2.place(x=390, y=70)
        bttn2 = Button(programparams, text="OK", width=8, bg=programparamsbg, command=lambda: check2(lbl2entry.get(), programparams, bttn2, param2))
        bttn2.place(x=500, y=71)

    # param3
    def param3():
        lbl3 = Label(programparams, text="p_hysteresis:", bg=programparamsbg)
        lbl3.place(x=45, y=100)
        lbl3entry = Entry(programparams, width=20)
        lbl3entry.place(x=195, y=98)
        unit3 = Label(programparams, text = "(boolean)", bg=background)
        unit3.place(x=390, y=100)
        bttn3 = Button(programparams, text=" OK ", width=8, bg=programparamsbg, command=lambda: check3(lbl3entry.get(), programparams, bttn3, param3))
        bttn3.place(x=500, y=101)

    # param4
    def param4():
        lbl4 = Label(programparams, text="p_hysteresisInterval:", bg=programparamsbg)
        lbl4.place(x=45, y=130)
        lbl4entry = Entry(programparams, width=20)
        lbl4entry.place(x=195, y=128)
        unit4 = Label(programparams, text = "(mSec)", bg=background)
        unit4.place(x=390, y=130)
        bttn4 = Button(programparams, text=" OK ", width=8, bg=programparamsbg, command=lambda: check4(lbl4entry.get(), programparams, bttn4, param4))
        bttn4.place(x=500, y=131)

    # param5
    def param5():
        lbl5 = Label(programparams, text="p_lowrateInterval:", bg=programparamsbg)
        lbl5.place(x=45, y=160)
        lbl5entry = Entry(programparams, width=20)
        lbl5entry.place(x=195, y=158)
        unit5 = Label(programparams, text = "(mSec)", bg=background)
        unit5.place(x=390, y=160)
        bttn5 = Button(programparams, text=" OK ", width=8, bg=programparamsbg, command=lambda: check5(lbl5entry.get(), programparams, bttn5, param5))
        bttn5.place(x=500, y=161)

    # param6
    def param6():
        lbl6 = Label(programparams, text="p_vPaceAmp:", bg=programparamsbg)
        lbl6.place(x=45, y=190)
        lbl6entry = Entry(programparams, width=20)
        lbl6entry.place(x=195, y=188)
        unit6 = Label(programparams, text = "(mv)", bg=background)
        unit6.place(x=390, y=190)
        bttn6 = Button(programparams, text=" OK ", width=8, bg=programparamsbg, command=lambda: check6(lbl6entry.get(), programparams, bttn6, param6))
        bttn6.place(x=500, y=191)

# param7
    def param7():
        lbl7 = Label(programparams, text="p_vPaceWidth:", bg=programparamsbg)
        lbl7.place(x=45, y=220)
        lbl7entry = Entry(programparams, width=20)
        lbl7entry.place(x=195, y=218)
        unit7 = Label(programparams, text = "(mSec)", bg=background)
        unit7.place(x=390, y=220)
        bttn7 = Button(programparams, text=" OK ", width=8, bg=programparamsbg, command=lambda: check7(lbl7entry.get(), programparams, bttn7, param7))
        bttn7.place(x=500, y=221)

# param8
    def param8():
        lbl8 = Label(programparams, text="p_VRP:", bg=programparamsbg)
        lbl8.place(x=45, y=250)
        lbl8entry = Entry(programparams, width=20)
        lbl8entry.place(x=195, y=248)
        unit8 = Label(programparams, text = "(mSec)", bg=background)
        unit8.place(x=390, y=250)
        bttn8 = Button(programparams, text=" OK ", width=8, bg=programparamsbg, command=lambda: check8(lbl8entry.get(), programparams, bttn8, param8))
        bttn8.place(x=500, y=251)        

    param1(), param2(), param3(), param4(), param5(), param6(), param7(), param8()


# ********************************************************************************************
def check1(lbl1entry, programparams, bttn1, param1):
    if(lbl1entry):
        lblval = Label(programparams, text=lbl1entry, bg=programparamsbg, width=20)
        lblval.place(x=198, y=40)
        bttn1.destroy()
        bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param1())
        bttnchange.place(x=500, y=41)

def check2(lbl2entry, programparams, bttn2, param2):
    if(lbl2entry):
        lblval = Label(programparams, text=lbl2entry, bg=programparamsbg, width=20)
        lblval.place(x=198, y=70)
        bttn2.destroy()
        bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param2())
        bttnchange.place(x=500, y=71)

def check3(lbl3entry, programparams, bttn3, param3):
    if(lbl3entry):
        if(lbl3entry == "true" or lbl3entry == "True" or lbl3entry == "false" or lbl3entry == "False"):
            lblval = Label(programparams, text=lbl3entry, bg=programparamsbg, width=20)
            lblval.place(x=198, y=100)
            bttn3.destroy()
            bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param3())
            bttnchange.place(x=500, y=101)
        else:
            error=Tk()
            error.title("Error")
            error.geometry("400x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the parameter you entered is not valid!\nThe value must be a boolean (True or False)", bg=newUserbg)
            messageLbl.place(x=50,y=25)

def check4(lbl4entry, programparams, bttn4, param4):
    if(lbl4entry):
        lbl4val = float(lbl4entry)
        if(lbl4val < 196):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too low!\nThe acceptable range for p_hysteresisInterval is 196mSec to 504mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        elif(lbl4val > 504):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too high!\nThe acceptable range for p_hysteresisInterval is 196mSec to 504mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        else:
            lblval = Label(programparams, text=lbl4val, bg=programparamsbg, width=20)
            lblval.place(x=198, y=130)
            bttn4.destroy()
            bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param4())
            bttnchange.place(x=500, y=131)

def check5(lbl5entry, programparams, bttn5, param5):
    if(lbl5entry):
        lbl5val=float(lbl5entry)
        if(lbl5val < 335):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too low!\nThe acceptable range for p_lowrateInterval is 335mSec to 2008mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        elif(lbl5val > 2008):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too high!\nThe acceptable range for p_lowrateInterval is 335mSec to 2008mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        else:
            lblval = Label(programparams, text=lbl5val, bg=programparamsbg, width=20)
            lblval.place(x=198, y=160)
            bttn5.destroy()
            bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param5())
            bttnchange.place(x=500, y=161)

def check6(lbl6entry, programparams, bttn6, param6):
    if(lbl6entry):
        lbl6val=float(lbl6entry)
        if(lbl6val < 440):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too low!\nThe acceptable range for p_vPaceAmp is 440mSec to 7840mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        elif(lbl6val > 7840):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too high!\nThe acceptable range for p_vPaceAmp is 440mSec to 7840mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        else:
            lblval = Label(programparams, text=lbl6val, bg=programparamsbg, width=20)
            lblval.place(x=198, y=190)
            bttn6.destroy()
            bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param6())
            bttnchange.place(x=500, y=191)

def check7(lbl7entry, programparams, bttn7, param7):
    if(lbl7entry):
        lbl7val=float(lbl7entry)
        if(lbl7val < 0.1):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too low!\nThe acceptable range for p_vPaceWidth is 0.1mSec to 1.9mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        elif(lbl7val > 1.9):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too high!\nThe acceptable range for p_vPaceWidth is 0.1mSec to 1.9mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        else:
            lblval = Label(programparams, text=lbl7val, bg=programparamsbg, width=20)
            lblval.place(x=198, y=220)
            bttn7.destroy()
            bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param7())
            bttnchange.place(x=500, y=221)

def check8(lbl8entry, programparams, bttn8, param8):
    if(lbl8entry):
        lbl8val=float(lbl8entry)
        if(lbl8val < 142):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too low!\nThe acceptable range for p_VRP is 142mSec to 508mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        elif(lbl8val > 508):
            error=Tk()
            error.title("Error")
            error.geometry("650x100")
            error.configure(bg=background)
            messageLbl=Label(error,text="Error: the value you entered is too high!\nThe acceptable range for p_VRP is 142mSec to 508mSec.", bg=newUserbg)
            messageLbl.place(x=50,y=25)
        else:
            lblval = Label(programparams, text=lbl8val, bg=programparamsbg, width=20)
            lblval.place(x=198, y=250)
            bttn8.destroy()
            bttnchange = Button(programparams, text="Change", width=8, bg=programparamsbg, command= lambda: param8())
            bttnchange.place(x=500, y=251)
        

    
def logInCheck(window,username,password):
    success=False
    if(os.path.exists('user_data')==False): #no user_data file
        message="No local user data found. Create a new user."
    elif(os.stat('user_data').st_size==0): #empty user data file
        message="No local user data found. Create a new user."
    else: #searching user_data
        file=open('user_data','rb')
        users=pickle.load(file)
        print(users)
        for userId, userData in users.items():
            if(userData['username']==username):
                if(userData['password']==password): #login successful
                    success=True
        message="Incorrect username or password." #will only get here if username and password not found
    if(success):
        onClickLogin(window)
    else:
        loingFailed=Tk()
        loingFailed.title("Login Failed")
        loingFailed.geometry("400x100")
        loingFailed.configure(bg=background)
   
        messageLbl=Label(loingFailed,text=message,bg=newUserbg)
        messageLbl.place(x=50,y=25)

        okButton=Button(loingFailed, text="  OK  ", bg=newUserbg, command= lambda:closeTwoWindows(window,loingFailed))
        okButton.place(x=100,y=60)
    
# INITIAL WINDOW WITH LOGIN******************************************************************************************
def main():
    existingUser=Tk()
    existingUser.title("Existing User Log In")
    existingUser.geometry("700x600")
    existingUser.configure(bg=background)

    loginbg=Label(existingUser,height=12,width=40,bg=existingUserbg,borderwidth=2,relief="ridge")
    loginbg.place(x=150,y=183)

    exuser=Label(existingUser,text="Existing User Login",bg=existingUserbg)
    exuser.config(font=("Segoe UI", 13))
    exuser.place(x=270,y=190)

    lbl = Label(existingUser, text="Username:",bg=existingUserbg)
    lbl.place(x=175,y=221)

    username=Entry(existingUser,width=20)
    username.place(x=250,y=221)

    lbl1=Label(existingUser,text="Password:",bg=existingUserbg)
    lbl1.place(x=175,y=250)

    password=Entry(existingUser,width=20)
    password.place(x=250,y=250)

    login = Button(existingUser, text="Login", command= lambda: logInCheck(existingUser,username.get(),password.get()))
    login.place(x=315,y=295)

    lblQuestion=Label(existingUser, text="Don't have an account?", bg=existingUserbg)
    lblQuestion.place(x=175,y=330)
    submitButton=Button(existingUser, text="Click here!", bg=existingUserbg, command= lambda: onClickClickHere(existingUser))
    submitButton.place(x=340, y=330)
    existingUser.mainloop()
#********************************************************************************************************************
# CREATE NEW USER HERE
def onClickCreate(newUser,username,password):
    userStatus=Tk()
    userStatus.title("User Status")
    userStatus.geometry("400x100")
    userStatus.configure(bg=background)

    #creates file if doesn't exist
    if(os.path.exists('user_data')==False):
        #print("creating file")
        file=open('user_data','w')
        file.close()
    
    #file exist, but empty 
    if(os.stat('user_data').st_size==0):
        #print("users empty")
        users={}
        users[0]={}
        users[0]['username']=username
        users[0]['password']=password
        message="Successfully created new user."
    else:
        file=open('user_data','rb')
        users=pickle.load(file)
        #print(users)
        i=len(users)
        print(i)
    
        if(i>=10):
            message="Cannot create new user. Maximum number of users already created."

        elif(i<10):
            users[i]={}
            #print(username)
            #print(password)
            users[i]['username']=username
            users[i]['password']=password
            message="Successfully created new user."
        else:
            message="Something went wrong. User not created."
 
    file.close()

    #writing user data file
    file=open('user_data','wb')
    pickle.dump(users,file)
    file.close()

    messageLbl=Label(userStatus,text=message,bg=newUserbg)
    messageLbl.place(x=50,y=25)

    okButton=Button(userStatus, text="  OK  ", bg=newUserbg, command= lambda:closeTwoWindows(newUser,userStatus))
    okButton.place(x=100,y=60)

#********************************************************************************************************************
def onClickClickHere(existingUser):
    existingUser.destroy()
    newUser=Tk()
    newUser.title("Create New User")
    newUser.geometry("700x600")
    newUser.configure(bg=background)

    createbg=Label(newUser,height=11,width=40,bg=newUserbg,borderwidth=2,relief="ridge")
    createbg.place(x=150,y=183)

    newuser=Label(newUser,text="Create New User",bg=newUserbg)
    newuser.config(font=("Segoe UI", 13))
    newuser.place(x=270,y=190)

    lblname = Label(newUser, text="Username:",bg=newUserbg)
    lblname.place(x=175,y=221)

    name=Entry(newUser,width=20)
    name.place(x=250,y=221)

    lblpass=Label(newUser,text="Password:",bg=newUserbg)
    lblpass.place(x=175,y=250)

    passwordnew=Entry(newUser,width=20)
    passwordnew.place(x=250,y=250)

    create = Button(newUser, text="Create", bg=newUserbg, command= lambda:onClickCreate(newUser,name.get(),passwordnew.get()))
    create.place(x=280, y = 295)

    exitbttn = Button(newUser, text="Exit", bg=newUserbg,command=lambda:toMain(newUser))
    exitbttn.place(x=360, y=295)

def toMain(window):
    window.destroy()
    main()

def closeTwoWindows(w1,w2):
    w1.destroy()
    w2.destroy()
    main()

main()
