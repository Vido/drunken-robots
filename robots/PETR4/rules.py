
import datetime

from db_api.db_connection import DbReader

def should_it_run():

	now = datetime.datetime.now()

	if now.weekday() not in [0, 1, 2, 3, 4]:
		raise Exception("Today it's Saturnday or Sunday")

	dbc = DbReader('PETR4/db')
	template = "SELECT date FROM ticker WHERE date == '{today}'"
	context = { 'today': now.strftime("%Y-%m-%d") }
	query = template.format(**context)
	result = dbc.select(query)

	if result:
		raise Exception("The Robot already fetched the ticker")
	
	return True

