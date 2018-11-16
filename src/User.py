from Singleton import Singleton
from DatabaseHelper import DatabaseHelper

class User:
	def __init__(self, username):
		self.username = username

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
	Returns True if successful, False if username already exists.
	'''
	def createNewUser(self, username: str, password: str):
		if (self.validateUniqueUsername(username)):
			# create new user
			self.db.insert(self.USERS_TABLE, {
				'username': username, 
				'password': password
			})
			return True
		else:
			return False		