from User import *

class GUIHelper:
	def createLoginScreen(self, sessionHelper):
		# display login screen
		# if button pressed:
		sessionHelper.buttonClick(
			'signup', {'username': username,
				'password': password})

	def displayUserDashboard(self):
		pass