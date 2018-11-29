import sys
sys.path.insert(0, '../src')
from User import *
from RunTests import SimpleTestSuite

class UserTest:
	def setUp(self):
		self.sts = SimpleTestSuite()
		self.userHelper = UserHelper()

	def test_createNewUser(self):
		# first assert if validateUniqueUsername()
		# returns True if the username doesn't exist in DB yet
		username = "areeba"
		password = "1010101"
		self.sts.assertIs(True, self.userHelper.validateUniqueUsername(username))
		
		# now add it into DB, and assert if the function returns false
		user = self.userHelper.createNewUser(username, password)
		self.sts.assertIs(False, self.userHelper.validateUniqueUsername(username))

		# assert User object was created successfully
		self.sts.assertEqual(username, user.username)

		# try getting user directly from database and make sure they match
		user_copy = self.userHelper.getUser(username, password)
		self.sts.assertEqual(user.username, user_copy.username)

		# try getting user with an incorrect password 
		user_copy = self.userHelper.getUser(username, 'incorrect')
		self.sts.assertIs(None, user_copy)

		# try creating a new user with an existing username 
		res = self.userHelper.createNewUser(username, '221')
		self.sts.assertIs(None, res)

	def test_deviceSettings_pacingMode(self):
		# create new user
		username = "areeba_2"
		password = "012039"
		user = self.userHelper.createNewUser(username, password)
		
		# test correct input for pacing mode
		mode = 'AOO'
		res = self.userHelper.setPacingMode(user, mode)
		self.sts.assertIs(True, res)

		# test incorrect input for pacing mode
		res = self.userHelper.setPacingMode(user, 'aaaaaa')
		self.sts.assertIs(False, res)

		# assert pacing mode was saved in database for that user
		user_copy = self.userHelper.getUser(username, password)
		self.sts.assertEqual(mode, user_copy.deviceSettings.pacingMode)

		# save another pacing mode for the same user
		mode = 'VVI'
		self.userHelper.setPacingMode(user, mode)
		user_copy = self.userHelper.getUser(username, password)
		self.sts.assertEqual(mode, user_copy.deviceSettings.pacingMode)
	
	def runTests(self):
		self.setUp()
		self.test_createNewUser()
		self.test_deviceSettings_pacingMode()
		self.sts.finishTest()

UserTest().runTests()