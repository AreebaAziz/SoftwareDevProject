from User import UserHelper
from GUIHelper import GUIHelper

class SessionHelper:
	def launch(self):
		if hasattr(self,"gui"):
			self.gui.DestroyWindow()
			print("bye")
		self.gui = GUIHelper("Login Window","700x600")
		self.userHelper = UserHelper()
		self.user = None
		self.gui.createLoginScreen(self)

	def signInUser(self, username: str, password: str):
		if self.userHelper.getUser(username,password)!=None:
			self.gui.DestroyWindow() #need this to create new window with new size and title
			self.gui=GUIHelper("Programmable Paramters","700x600")
			self.gui.displayUserDashboard(self) #displays parameters page
		else:
			self.gui.CreatePopUp("Error!","Cannot login. Create a new user or try again.")
		

	def createUser(self,username: str, password: str):
		if self.userHelper.createNewUser(username,password)!=None:
			self.gui.CreatePopUp("Success","Successfully created new user.")
			self.gui.DestroyWindow(action=self.gui.createLoginScreen(self))
		else:
			self.gui.CreatePopUp("Error!","Cannot create user. Username may already exist or 10 users already created.")
		
	def createUser(self, username: str, password: str):
		self.user = self.userHelper.createNewUser(username, password)
		 
	