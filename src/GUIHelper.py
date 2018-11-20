from User import *
from tkinter import *

class GUIHelper:
	def __init__(self,title,size):
		window=self.window=Tk()
		self.color="#dce0e8" #default colors
		self.widgetColor="#dce0e8" #default colors
		window.title(title)
		window.geometry(size)
		window.configure(bg=self.color)
	
	def setBackground(self,color):
		self.color=color
		self.window.configure(bg=self.color)

	def setWidgetColor(self,color):
		self.widgetColor=color

	def CreateText(self,x,y,text):
		lbl=Label(self.window, text=text, bg=self.widgetColor)
		lbl.place(x=x, y=y)

	def CreateButton(self,x,y,text,action):
		btn = Button(self.window, text=text, command= lambda: action)
		btn.place(x=x,y=y)

	def CreateEntry(self,x,y,width):
		entry=Entry(self.window,width=width)
		entry.place(x=x,y=y)
		return entry

	def CreateBox(self,x,y,width,height):
		loginbg=Label(self.window,height=height,width=width,bg=self.widgetColor,borderwidth=2,relief="ridge")
		loginbg.place(x=x,y=y)


	def createLoginScreen(self, sessionHelper):
		# display login screen
		self.CreateBox(150,183,40,11)
		self.CreateText(0,0,"test")
		self.CreateText(270,190,"Create New User")
		self.CreateText(175,221,"Username:")
		username=self.CreateEntry(250,221,20)
		self.CreateText(175,250,"Password:")
		password=self.CreateEntry(250,250,20)
		self.CreateButton(315,295,"Login",sessionHelper.signInUser(username.get(),password.get()))
		self.CreateText(175,330,"Don't have an account?")
		self.CreateButton(340,330,"Click here!",sessionHelper.createUser()) #createuser does not exist yet
		self.window.mainloop()

	def createNewUserScreen(self,sessionHelper):
		pass
	'''
	def CreateParameter()


		lbl1 = Label(programparams, text="p_pacingState:", bg=programparamsbg)
        lbl1.place(x=45, y=40)
        lbl1entry = Entry(programparams, width=20)
        lbl1entry.place(x=195, y=38)
        unit1 = Label(programparams, text = "(y_pacingState)", bg=background)
        unit1.place(x=390, y=40)
        bttn1 = Button(programparams, text="OK", width=8, bg=programparamsbg, command=lambda: check1(currentUserId, lbl1entry.get(), programparams, bttn1, param1))
        bttn1.place(x=500, y=41)
	'''
	def CreateMenu(self,x,y,options: list):
		optionName=StringVar(self.window)
		optionName.set(options[0])
		menu=OptionMenu(self.window,optionName,tuple(options))
		menu.pack()
		menu.place(x=x,y=y)


	

	