from tinydb import TinyDB, Query

class Singleton(type):
	'''
	Singleton class borrowed from: 
	https://sourcemaking.com/design_patterns/singleton/python/1
    Define an Instance operation that lets clients access its unique
    instance.
    '''
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class DatabaseHelper(metaclass=Singleton):
	def __init__(self, db_file_path: str):
		self._tinydb = TinyDB(db_file_path)

	'''
	Creates a new table in database given table name.
	Returns None if failed to create table.
	'''
	def createTable(self, name: str):
		try:
			return self._tinydb.table(name)
		except Exception as e:
			return None

	#remove table from database
	def removeTable(self, name: str):
		self._tinydb.purge_table(name)

	#returns list of all table names in database
	def getTables(self):
		return self._tinydb.tables()

	#insert new row values into a table
	def insert(table_name: str, row: dict):
		table = self._tinydb.table(table_name)
		table.insert(row)

	def get(self, table_name, ):
		table = self._tinydb.table(table_name)
