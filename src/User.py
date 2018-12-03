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
			return user