import sqlite3

class BaseExtractor():
    pass

class OilMiner(BaseExtractor):

    connection = sqlite3.connect(
        # TODO Remove the absolute path
        "/home/overlord/Documents/drunken-robots/robots/PETR4/PETR4.sqlite3"
    )

    cursor = connection.cursor()

    def last5days_high(self):
        query = "SELECT date, high FROM ticker ORDER BY date DESC LIMIT 5;"
        self.cursor.execute(query)
        tuples = self.cursor.fetchall()
        return tuples

    def last5days_low(self):
        query = "SELECT date, high FROM ticker ORDER BY date DESC LIMIT 5;"
        self.cursor.execute(query)
        tuples = self.cursor.fetchall()
        return tuples

# quick test
#om = OilMiner();
#a = om.last5days_high()
#print a

