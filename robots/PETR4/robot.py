import urllib2
from datetime import datetime

from model import Model
from db_api.db_connection import DbWriter

	# Reference:
	# http://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty
	# http://br.financas.yahoo.com/q?s=PETR4.SA

def make_your_magic():
	
	url = "http://download.finance.yahoo.com/d/quotes.csv?s=PETR4.SA&f=sd1o0h0g0l1v0&e=.csv"
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)

	row = response.readlines()[0]
	#print row # DEBUG 
	data = row.split(',')
	# "PETR4.SA","4/19/2013",18.15,18.48,17.95,18.48,38077200

	symbol = data[0]
	date = datetime.strptime(data[1], '"%m/%d/%Y"').strftime('"%Y-%m-%d"')
	open_p = float(data[2])
	high = float(data[3])
	low = float(data[4])
	close = float(data[5])
	volume = float(data[6].rstrip())

	model = Model()
	dbc = DbWriter(model)
	dbc.write(symbol, date, open_p, high, low, close, volume)

#make_your_magic()
