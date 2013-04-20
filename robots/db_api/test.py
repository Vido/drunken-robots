# TODO set encoding

import os
import unittest

from db_connection import DbWriter, DbReader

try:
	os.remove('test.sqlite3')
except OSError as e:
	pass
	

class TestDbWriter(unittest.TestCase):

	db_file = 'test'
	dbc = DbWriter(db_file)
	
	def test_start(self):
		fp = open(self.dbc.db_file, 'r')
		fp.close()
		
	def test_write(self):

		self.dbc.write(
			'TEST.SA',
			"'2013-04-19'",
			'1',
			'1.1',
			'0.9',
			'1',
			'50')

class TestDbReader(unittest.TestCase):
	db_file = 'test'
	dbc = DbReader(db_file)
	
	def test_select(self):
		self.dbc.select("SELECT * FROM ticker;")


if __name__ == '__main__':
	unittest.main()
