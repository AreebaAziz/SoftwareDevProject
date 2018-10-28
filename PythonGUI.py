import pickle
from tkinter import *
import os

background="#dce0e8"
existingUserbg="#e8ecf2"
newUserbg = "#e8ecf2"

users={} #only run once to create blank dict of users

# WINDOW AFTER LOGGED IN *****************************************************************************************
def onClickLogin(existingUser):
    existingUser.destroy()
    userInfo=Tk()
    userInfo.title("User Information")
    userInfo.geometry("700x690")
    userInfo.configure(bg=background)


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

    login = Button(existingUser, text="Login", command= lambda: onClickLogin(existingUser))
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