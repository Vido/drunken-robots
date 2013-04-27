import random
from datetime import datetime, timedelta

from core.basics.base_classes import BasePsychic
from core.database.standard_models import PsychicModel
from core.database.connection import DbWriter
from extractor import OilMiner

class Gibberish(BasePsychic):

    model = PsychicModel()
    model.DB_FILE = 'gibberish.sqlite3'
    extractor = OilMiner()

    def make_your_magic(self):

        dbw = DbWriter(self.model)

        best_prices = self.extractor.last5days_high()
        worse_prices = self.extractor.last5days_high()

        lower = min([wp[1] for wp in worse_prices])
        upper = max([ bp[1] for bp in best_prices])

        future_price = random.uniform(lower, upper)
        future_date = datetime.now() + timedelta(days=1)

        str_future = future_date.strftime("'%Y-%m-%d'")

        dbw.write(str_future, "'PETR4'", future_price, table='prediction')

#g = Gibberish()
#g.make_your_magic()
