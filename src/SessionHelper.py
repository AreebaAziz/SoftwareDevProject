from User import UserHelper
from GUIHelper import GUIHelper
from DeviceCommunication import DeviceCommunication

class SessionHelper:
	def launch(self):
		if hasattr(self,"gui"):
			self.gui.DestroyWindow()
			print("bye")
		self.gui = GUIHelper("Login Window","700x600")
		self.userHelper = UserHelper()
		self.user = None
		self.device = DeviceCommunication()
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

	def connectToDevice(self):
		# returns True if successful, false if not
		if (not self.device.connected):
			if (self.device.connectToDevice()):
				self.gui.CreateText(500, 130, "Success!")
			else:
				self.gui.CreateText(500, 130, "Failed. ")

	'''
		Use this function when a button "Send Data to Device" is clicked
		so all parameter data, including pacing mode, can be sent to the 
		device at once. 
		Receives a dict (allParamData) that is in format: 
		['param_name': param_value,
			'param_name2: param_value2']
	'''
	def sendAllDataToDevice(self, parameterObject):
		text = ""
		if (self.device.connected):
			if (parameterObject.pacingMode is None):
				text = 	"Select a pacing mode first.   "
			else:
				data = parameterObject.getCurrentParamData()
				if (self.device.sendAllDataToDevice(data, True)):
					text = "Success!                                  "
				else:
					text = "Failed to send data to device."
		else:
			text = "Device not connected.         "

		self.gui.CreateText(500, 180, text)

	'''
		Call this function when the user clicks a "Display Egram Graph".
		This will receive data from the device and plot it realtime.
	'''
	def plotEgramData(self):
		if (not self.device.plotEgramData()):
			self.gui.CreateText(500, 230, "Failed to plot graph.")
		else:
			self.gui.CreateText(500, 230, "                                  ")