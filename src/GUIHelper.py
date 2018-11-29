from User import *
from tkinter import *
from Parameters import Parameters

class GUIHelper:
	def __init__(self,title,size):
		self.window=Tk()
		self.color="#dce0e8" #default colors
		self.widgetColor="#dce0e8" #default colors
		self.labelColor='#A9A9A9'
		self.window.title(title)
		self.window.geometry(size)
		self.window.configure(bg=self.color)
	
	def setBackground(self,color):
		self.color=color
		self.window.configure(bg=self.color)

	def setWidgetColor(self,color):
		self.widgetColor=color

	def CreateText(self,x,y,text):
		lbl=Label(self.window, text=text, bg=self.widgetColor)
		lbl.place(x=x, y=y)
	
	def CreateEmptyLabel(self, x, y, width):
		lbl=Label(self.window, width = width, bg=self.labelColor)
		lbl.place(x=x, y=y)

	def CreateButton(self,x,y,text,action):
		btn = Button(self.window, text=text, command= action)
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
		self.CreateText(270,190,"Login")
		self.CreateText(175,221,"Username:")
		username=self.CreateEntry(250,221,20)
		self.CreateText(175,250,"Password:")
		password=self.CreateEntry(250,250,20)
		password.config(show="*")
		self.CreateButton(315,295,"Login",lambda:sessionHelper.signInUser(username.get(),password.get()))
		self.CreateText(175,330,"Don't have an account?")
		self.CreateButton(340,330,"Click here!",lambda:self.createNewUserScreen(sessionHelper)) #createuser does not exist yet
		self.window.mainloop()
	
	def createNewUserScreen(self,sessionHelper):
		self.CreateBox(150,183,40,11)
		self.CreateText(270,190,"Create New User")
		self.CreateText(175,221,"Username")
		username=self.CreateEntry(250,221,20)
		self.CreateText(175,250,"Password")
		password=self.CreateEntry(250,250,20)
		password.config(show="*")
		self.CreateButton(280,295,"Create",lambda:sessionHelper.createUser(username.get(),password.get()))
		self.CreateButton(360,295,"Exit",lambda:self.DestroyWindow(action=self.createLoginScreen(sessionHelper)))

	def DestroyWindow(self,action=print()): #default action is print line
		self.window.destroy()
		action

	def CreateParameter(self, paramName, yval):
		self.CreateText(30, yval, paramName)
		self.CreateEmptyLabel(60, yval, 20)

# CREATE OK BUTTON NEXT TO THE PARAMETER
	def CreateEntryParam(self, y):
		self.CreateEntry(60, y, 20)
	
	def displayUserDashboard(self,sessionHelper):
		parmas=Parameters()
		parmas.pacingModeList()
		self.CreateButton(50,50,"Logout",lambda:sessionHelper.launch())

	def CreateMenu(self,x,y,options: list):
		optionName=StringVar(self.window)
		optionName.set(options[0])
		menu=OptionMenu(self.window,optionName,tuple(options))
		menu.pack()
		menu.place(x=x,y=y)
		return optionName

	def CreatePopUp(self,title,text):
		window=Tk()
		window.title(title)
		window.geometry("400x100")
		window.configure(bg=self.color)
		lbl=Label(window, text=text, bg=self.color)
		lbl.place(x=50, y=25)



	

	