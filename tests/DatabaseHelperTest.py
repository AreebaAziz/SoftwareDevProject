import sys
sys.path.insert(0, '../src')
from DatabaseHelper import DatabaseHelper
from RunTests import SimpleTestSuite

class DatabaseHelperTest():
	DATABASE_NAME = "testDatabase.json"
	TABLE_NAME = "testTable"

	def setUp(self):
		self.db = DatabaseHelper(self.DATABASE_NAME)
		self.db._tinydb.purge_tables()	#remove any pre-existing tables
		self.table = self.db.createTable(self.TABLE_NAME)
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
		self.db.insert(self.TABLE_NAME, self.testRow)
		valuesActual = self.db.get(self.TABLE_NAME, 'username', 'AreebaAziz_123')
		self.sts.assertEqual(self.testRow, valuesActual)

	def testUpdate(self):
		self.testRow['country'] = 'US'
		self.db.update(self.TABLE_NAME, 'username', 'AreebaAziz_123', 'country', 'US')
		valuesActual = self.db.get(self.TABLE_NAME, 'username', 'AreebaAziz_123')
		self.sts.assertEqual(self.testRow, valuesActual) 

	def runTests(self):
		self.setUp()
		self.testInsertAndGet()
		self.testUpdate()
		self.sts.finishTest()

DatabaseHelperTest().runTests()