import sys
sys.path.insert(0, '../src')
from DatabaseHelper import DatabaseHelper
from RunTests import SimpleTestSuite

class DatabaseHelperTest:
	USERS_TABLE = "users"

	def setUp(self):
		self.db = DatabaseHelper()
		self.db._tinydb.purge_tables()	#remove any pre-existing tables
		self.table = self.db.createTable(self.USERS_TABLE)
		self.sts = SimpleTestSuite()
		self.testRow = {
			'username': 'AreebaAziz_123',
			'name': 'areeba',
			'age': 21,
			'country': 'CA'
		}

	def testInsertAndGet(self):
		# assert a table was successfully created at setup
		self.sts.assertIsNot(None, self.db.getTables())

		# assert insertion and getting value is successful
		self.db.insert(self.USERS_TABLE, self.testRow)
		valuesActual = self.db.get(self.USERS_TABLE, 'username', 'AreebaAziz_123')
		self.sts.assertEqual(self.testRow, valuesActual)

	def testUpdate(self):
		self.testRow['country'] = 'US'
		self.db.update(self.USERS_TABLE, 'username', 'AreebaAziz_123', 'country', 'US')
		valuesActual = self.db.get(self.USERS_TABLE, 'username', 'AreebaAziz_123')
		self.sts.assertEqual(self.testRow, valuesActual) 

	def runTests(self):
		self.setUp()
		self.testInsertAndGet()
		self.testUpdate()
		self.sts.finishTest()

DatabaseHelperTest().runTests()