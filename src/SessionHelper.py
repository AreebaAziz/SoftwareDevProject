from User import *

class SessionHelper:
	def launch(self):
		self.gui = GUIHelper()
		self.gui.createLoginScreen(self)
		self.userHelper = UserHelper()
		self.user = None

	def signInUser(self, username: str, password: str):
		self.user = self.UserHelper.createNewUser(params['username'], params['password'])
		self.gui.displayUserDashboard(self)
		
	def setUserPacingMode(self):
		pass
		# if (self.user is not None):
		# 	return self.userHelper.setUserPacingMode(self.user, )
		# else:
		# 	return None

