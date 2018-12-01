from User import *
from tkinter import *
from Parameters import Parameters

class GUIHelper:
	def __init__(self,title,size):
		self.window=Tk()
		self.color="#dce0e8" #default colors
		self.widgetColor="#dce0e8" #default colors
		self.labelColor='#C0C0C0'
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
		btn = Button(self.window, text=text, command= action, bg=self.widgetColor)
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
		self.CreateText(20, yval, paramName)
		self.CreateEmptyLabel(200, yval, 20)

	def showParam(self, paramlist):
		yval = 60
		for i in range(0, len(paramlist)):
			self.CreateParameter(paramlist[i], yval)
			yval += 35

	def createEntryParam(self,x,y,width, entryID):
		parameter = Parameters()
		entry=Entry(self.window,width=width, bd = 0, textvariable = entryID)
		entry.place(x=x,y=y)
		self.CreateButton(400, y, 'OK', lambda: parameter.checkParamValid(self, entryID, entry.get()))

	def acceptOrRejectParam(self, paramvalue):
		if paramvalue == "error":
			self.CreatePopUp('Error', 'The value you entered is invalid!')
		else:
			# THE PRINT STATEMENT IS A PLACE HOLDER BECAUSE HERE IS WHERE THE FUNCTION CALL FOR SERIAL COMMUNICATION GOES
			# FOR EXAMPLE:
			# self.serialCommunicate(paramvalue)
			print (paramvalue)

	def showEntryParam(self, programmable, possible):
		for i in programmable:
			if i in possible:
				yval = ((possible.index(i)+1)*35)+25
				self.createEntryParam(200, yval, 20, i)
	
	def displayUserDashboard(self,sessionHelper):
		parameter = Parameters()
		self.CreateText(20, 20, 'Please Select a Pacing Mode: ')
		pacingMode_optionName = self.CreateMenu(220, 20, parameter.pacingModeList())
		self.CreateButton(300, 20, 'OK', lambda: parameter.displayParams(self, pacingMode_optionName))

		# self.CreateButton(50,50,"Logout",lambda:sessionHelper.launch())

	def CreateMenu(self, x, y, options):
		optionName=StringVar(self.window)
		optionName.set(options[0])
		menu = OptionMenu(self.window, optionName, *options)
		menu.pack()
		menu.place(x=x,y=y)
		return optionName

	def CreatePopUp(self,title,text):
		window=Tk()
		window.title(title)
		window.geometry("450x100")
		window.configure(bg=self.color)
		lbl=Label(window, text=text, bg=self.color)
<<<<<<< HEAD
		lbl.place(x=30, y=25)


	def displayUserDashboard(self, sessionHelper): 
		self.CreateMenu(20, 20, ['a', 'are', 'de'])
=======
		lbl.place(x=30, y=25)
>>>>>>> Areeba
