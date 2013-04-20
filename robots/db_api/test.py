# TODO set encoding

import os
import unittest

from db_connection import DbWriter
from db_connection import DbReader

try:
	os.remove('*.sqlite3')
except OSError as e:
	pass
	

class Model1():
	DB_FILE = 'test1.sqlite3'

	FIELDS = [
		('fieldA', 'TEXT'),
	]

	def validate(self, *args):
		context = {
			'fieldA': args[0]
		}
		return context


class TestDbWriter1(unittest.TestCase):

	db_model = Model1()
	dbc = DbWriter(db_model)
	
	def test_start(self):
		fp = open(self.db_model.DB_FILE, 'r')
		fp.close()
		
	def test_write(self):
		self.dbc.write("'TEST.SA'")
		# TODO: Check inside the sqlite file


class Model3():
	DB_FILE = 'test3.sqlite3'

	FIELDS = [
		('fieldA', 'TEXT'),
		('fieldB', 'TEXT'),
		('fieldC', 'TEXT'),
	]

	def validate(self, *args):
		context = {
			'fieldA': args[0],
			'fieldB': args[1],
			'fieldC': args[2],
		}
		return context



class TestDbWriter3(unittest.TestCase):

	db_model = Model3()
	dbc = DbWriter(db_model)
	
	def test_start(self):
		fp = open(self.db_model.DB_FILE, 'r')
		fp.close()
		
	def test_write(self):
		self.dbc.write("'TEST.SA'", "'FOO'", "'BAR'")
		# TODO: Check inside the sqlite file


class TestDbReader(unittest.TestCase):
	
	db_model = Model3()

	dbcw = DbWriter(db_model)
	dbcr = DbReader(db_model)

	dbcw.write("'TEST.SA'", "'FOO'", "'BAR'")
		
	def test_select(self):
		result = self.dbcr.select("SELECT * FROM ticker;")
		assert len(result) != 0


if __name__ == '__main__':
	unittest.main()
