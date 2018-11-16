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
		self.sts.assertIs(self.userHelper.validateUniqueUsername(username), True)
		
		# now add it into DB, and assert if the function returns false
		self.userHelper.createNewUser(username, "1010128")
		self.sts.assertIs(self.userHelper.validateUniqueUsername(username), False)
	
	def runTests(self):
		self.setUp()
		self.test_createNewUser()
		self.sts.finishTest()

UserTest().runTests()