# TODO set encoding

import sqlite3

class DbTickerClass():

	def __init__(self, model):
		""" This should save the last state for database file """
			
		try:
			fp = open(model.DB_FILE, 'r')
			fp.close()

		except IOError:

			template = "CREATE TABLE ticker ("

			for field in model.FIELDS[:-1]:
				template += "%s %s," % (field)
	
			template += "%s %s" % (model.FIELDS[-1])
			template += ");"

			context = {}

			self.connection = sqlite3.connect(model.DB_FILE)
			query = template.format(**context)
			self.raw_query(query)
			self.connection.close()

		self.model = model


class DbWriter(DbTickerClass):

	def raw_query(self, query):
		""" Send write-queries the database """
		cursor = self.connection.cursor()
		cursor.execute(query)
		self.connection.commit()


	def write(self, *args):

		model_template = "INSERT INTO ticker ({columns}) VALUES ({values});"
		columns = ""
		values = ""
 
		for field in self.model.FIELDS[:-1]:
			columns += "%s, " % field[0]
			values += "{%s}, " % field[0]
	
		columns += "%s" % self.model.FIELDS[-1][0]
		values += "{%s}" % self.model.FIELDS[-1][0]
			
		model_context = {
			'columns': columns,
			'values': values,
		}

		query_template = model_template.format(**model_context)
		query_context = self.model.validate(*args)
		query = query_template.format(**query_context)
		
		self.connection = sqlite3.connect(self.model.DB_FILE)
		self.raw_query(query)
		self.connection.close()


class DbReader(DbTickerClass):
	def raw_query(self, query):
		""" Send read-queries the database """
		cursor = self.connection.cursor()
		cursor.execute(query)
		return cursor.fetchall()

	def select(self, query):
		self.connection = sqlite3.connect(self.model.DB_FILE)
		result = self.raw_query(query)
		self.connection.close()
		return result
