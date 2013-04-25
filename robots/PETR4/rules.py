# -*- coding: utf-8 -*-

import datetime
from model import Model

from core.database.connection import DbReader

def should_it_run():

    model = Model()
    now = datetime.datetime.now()

    if now.weekday() not in [0, 1, 2, 3, 4]:
        raise Exception("Today it's Saturnday or Sunday")

    dbc = DbReader(model)
    template = "SELECT date FROM ticker WHERE date == '{today}'"
    context = { 'today': now.strftime("%Y-%m-%d") }
    query = template.format(**context)
    result = dbc.select(query)

    if result:
        raise Exception("The Robot already fetched the ticker")
    
    return True

