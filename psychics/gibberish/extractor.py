import sqlite3

from core.basics.base_classes import BaseExtractor

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
        return self.ship_stuff(meta=('date', 'high'), datum=tuples)

    def last5days_low(self):
        query = "SELECT date, low FROM ticker ORDER BY date DESC LIMIT 5;"
        self.cursor.execute(query)
        tuples = self.cursor.fetchall()
        return self.ship_stuff(meta=('date', 'low'), datum=tuples)

    def latest(self):
        query = "SELECT * FROM ticker ORDER BY date DESC LIMIT 1;"
        self.cursor.execute(query)
        tuples = self.cursor.fetchall()
        return tuples

    def benchmark(self, date):
        assert not self.is_future(date)
        str_date = date.strftime('%Y-%m-%d')
        query = "SELECT * FROM ticker WHERE date = %s ;" % str_date
        self.cursor.execute(query)
        qs = self.cursor.fetchall()
        assert len(qs) == 1
        return qs

# quick tstest
#om = OilMiner();
#a = om.last5days_high(
#a = om.latest()
#print a

