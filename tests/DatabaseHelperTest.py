import sys
sys.path.insert(0, '../src')
from DatabaseHelper import DatabaseHelper
from SimpleTest import SimpleTest

class DatabaseHelperTest():
	def setUp(self):
		self.db = DatabaseHelper("testDatabase.json")
		self.db._tinydb.purge_tables()	#remove any pre-existing tables
		self.table_name = "testTable"
		self.table = self.db.createTable(self.table_name)
		self.st = SimpleTest()

	def testDatabaseHelper(self):
		# assert a table was successfully created at setup
		st.assertIs(self.db.getTables(), None)

		# assert insertion and getting value is successful
		values = {
			'name': 'areeba',
			'age': 21,
			'country': 'CA'
		}
		self.db.insert(self.table_name, values)
		valuesActual = self.db.get(self.table_name, 'name', 'areeba')
		assert values == valuesActual

	def runTests(self):
		self.setUp()
		self.testDatabaseHelper()

DatabaseHelperTest().runTests()