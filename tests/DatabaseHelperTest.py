import sys
sys.path.insert(0, '../src')

import unittest
from DatabaseHelper import DatabaseHelper

class DatabaseHelperTest(unittest.TestCase):
	def setUp(self):
		self.db = DatabaseHelper("testDatabase.json")

	#assert if DatabaseHelper class is a singleton
	def testDBSingleton(self):
		db = DatabaseHelper()
		self.assertTrue(db is self.db)

	#test table creation and deletion
	def testTables(self):
		#create table
		table_name = "testTable"
		table = self.db.createTable(table_name)
		
		#assert table was successfully created
		self.assertTrue(table is not None)
		self.assertTrue(table_name in self.db.getTables())

		#delete table
		self.db.removeTable(table_name)
		self.assertFalse(table_name in self.db.getTables())

	#test table insert function
	def testInsert(self):
		#create table
		table_name = "testTable"
		table = self.db.createTable(table_name)

		#insert values
		values = {
			'name': 'areeba',
			'age': 20,
			'country': 'CA'
		}
		self.db.insert(table_name, values)

		#search for values
		

if __name__ == "__main__":
    unittest.main()