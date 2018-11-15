from Singleton import Singleton
from tinydb import TinyDB, where

class DatabaseHelper(metaclass=Singleton):
	def __init__(self, db_file_path: str):
		self._tinydb = TinyDB(db_file_path)

	#creates new table if it doesn't exist yet, or returns 
	#existing or cached table
	def createTable(self, table_name):
		return self._tinydb.table(table_name)

	#remove table from database
	def removeTable(self, name: str):
		self._tinydb.purge_table(name)

	#returns list of all table names in database
	def getTables(self):
		return self._tinydb.tables()

	#insert new row values into a table
	def insert(self, table_name: str, row: dict):
		self.createTable(table_name).insert(row)

	#get a row of values given table name, and field-value search
	def get(self, table_name: str, field: str, value):
		return self.createTable(table_name).get(where(field) == value)

	#update a field value based on table name
	def update(self, table_name: str, searchField: str, searchValue, updateValue):
		table = self.createTable(table_name)
		table.update({searchField, updateValue}, where(searchField) == searchValue)