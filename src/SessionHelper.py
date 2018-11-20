from User import UserHelper
from GUIHelper import GUIHelper

class SessionHelper:
	def launch(self):
		self.gui = GUIHelper("Login Window","700x600")
		self.gui.createLoginScreen(self)
		self.userHelper = UserHelper()
		self.user = None

	def signInUser(self, username: str, password: str):
		'''
		self.user = UserHelper.createNewUser(username, password) #should not be create user if signing in
		self.gui.displayUserDashboard(self)
		'''
		pass

	def createUser(self):
		pass
		 
	def setUserPacingMode(self):
		pass
		

