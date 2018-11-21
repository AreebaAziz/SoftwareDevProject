from Singleton import Singleton
from DatabaseHelper import DatabaseHelper
from DeviceSettings import DeviceSettings

class User:
	def __init__(self, username):
		self.username = username
		self.deviceSettings = DeviceSettings()

class UserHelper(metaclass=Singleton):
	USERS_TABLE = "users"

	def __init__(self):
		self.db = DatabaseHelper()

	def validateUniqueUsername(self, username: str):
		if self.db.get(self.USERS_TABLE, 'username', username) is None:
			return True
		else:
			return False

	'''
	Creates new User if username is unique.
	Returns object User if successful, None if username already exists.
	'''
	def createNewUser(self, username: str, password: str):
		if (self.validateUniqueUsername(username)):
			# create new user
			self.db.insert(self.USERS_TABLE, {
				'username': username, 
				'password': password
			})
			return User(username)
		else:
			return None

	'''
	Returns User object if login info is correct, 
	otherwise returns None. 
	'''
	def getUser(self, username: str, password: str):
		user_raw = self.db.get(self.USERS_TABLE, 'username', username)
		if user_raw is None or user_raw['password'] != password:
			return None
		else:
			# serialize it into User object
			user = User(user_raw['username'])
			if 'pacingMode' in user_raw:
				self.setPacingMode(user, user_raw['pacingMode'])
			return user

	'''
	Sets the pacing mode for the user and saves it into database
	'''
	def setPacingMode(self, user: User, pacingMode: str):
		if (user == None):
			return False
		if (user.deviceSettings.setPacingMode(pacingMode)):
			# success - save into database
			self.db.update(self.USERS_TABLE, 'username', user.username,
				'pacingMode', pacingMode)
			return True
		else:
			return False