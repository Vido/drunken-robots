# TODO set encoding

import sqlite3

class DbTickerClass():

	db_file = ''

	def __init__(self, db_file):
		""" This should save the last state for database file """
		
		extension = '.sqlite3'
		db_file = db_file + extension
	
		try:
			fp = open(db_file, 'r')
			fp.close()

		except IOError:
			template = \
				"CREATE TABLE ticker (" \
					"symbol TEXT," \
					"date TEXT," \
					"open REAL," \
					"high REAL," \
					"low REAL," \
					"close REAL," \
					"volume REAL" \
				");" \

			context = {}

			self.connection = sqlite3.connect(db_file)
			query = template.format(**context)
			self.raw_query(query)
			self.connection.close()

		self.db_file = db_file


class DbWriter(DbTickerClass):

	def raw_query(self, query):
		""" Send write-queries the database """
		cursor = self.connection.cursor()
		cursor.execute(query)
		self.connection.commit()


	def write(self, symbol, date, open_p, high, low, close, volume):
		
		template = \
			"INSERT INTO ticker " \
				"(symbol, date, open, high, low, close, volume) " \
			"VALUES ('{symbol_t}', {date}, {open_p}, {high}," \
				" {low}, {close}, {volume})"

		context = {
			 'symbol_t': symbol,
			 'date': date,
			 'open_p': open_p,
			 'high': high,
			 'low': low,
			 'close': close,
			 'volume': volume,
		}

		query = template.format(**context)
		
		self.connection = sqlite3.connect(self.db_file)
		self.raw_query(query)
		self.connection.close()


class DbReader(DbTickerClass):

	def raw_query(self, query):
		""" Send read-queries the database """
		cursor = self.connection.cursor()
		cursor.execute(query)
		return cursor.fetchall()

	def select(self, query):
		self.connection = sqlite3.connect(self.db_file)
		result = self.raw_query(query)
		self.connection.close()
		return result

