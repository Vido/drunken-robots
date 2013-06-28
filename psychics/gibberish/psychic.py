import random
from datetime import datetime, timedelta

from core.basics.base_classes import BasePsychic
from core.database.standard_models import PsychicModel
from core.database.connection import DbWriter

from extractor import OilMiner
from surveyor import BarrelProof

class Gibberish(BasePsychic):

    model = PsychicModel()
    model.DB_FILE = 'gibberish.sqlite3'
    extractor = OilMiner()
    surveyor = BarrelProof(model, extractor)

    def make_your_magic(self):

        dbw = DbWriter(self.model)

        best_prices = self.extractor.last5days_high()
        worse_prices = self.extractor.last5days_high()

        lower = min([wp[1] for wp in worse_prices['datum']])
        upper = max([ bp[1] for bp in best_prices['datum']])

        future_price = random.uniform(lower, upper)
        future_date = datetime.now() + timedelta(days=1)

        str_future = future_date.strftime("'%Y-%m-%d'")

        dbw.write(str_future, "'PETR4'", future_price, table='prediction')


#g = Gibberish()
#g.surveyor.reckon()
