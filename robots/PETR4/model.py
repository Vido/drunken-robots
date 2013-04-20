
class Model():

	DB_FILE = "PETR4.sqlite3"
	
	FIELDS = [
		("symbol", "TEXT"),
		("date", "TEXT"),
		("open", "REAL"),
		("high", "REAL"),
		("low", "REAL"),
		("close", "REAL"),
		("volume", "REAL"),
	]


	def validate(self, *args):

		if len(args) != 7:
			raise Exception("Invalid number of arguments")

		for arg in args[2:]:
			float(arg)

		context = {
			'symbol': args[0],
			'date': args[1],
			'open': args[2],
			'high': args[3],
			'low': args[4],
			'close': args[5],
			'volume': args[6],
		}

		return context
