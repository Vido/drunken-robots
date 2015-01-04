# -*- coding: utf-8 -*-

import urllib2
from datetime import datetime

from core.basics.base_classes import BaseRobot

from core.database.connection import DbWriter
from core.database.connection import DbReader

from model import Model

class PETR4(BaseRobot):
    """
    Reference:
    http://code.google.com/p/yahoo-finance-managed/wiki/enumQuoteProperty
    http://br.financas.yahoo.com/q?s=PETR4.SA
    """

    model = Model()

    def do_your_job(self):

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

        dbw = DbWriter(self.model)
        dbw.write(symbol, date, open_p, high, low, close, volume, table='ticker')

    def time_to_work(self):

        now = datetime.now()

        if now.weekday() not in [0, 1, 2, 3, 4]:
            raise Exception("Today it's Saturnday or Sunday")

        template = "SELECT date FROM ticker WHERE date == '{today}'"
        context = { 'today': now.strftime("%Y-%m-%d") }
        query = template.format(**context)

        dbr = DbReader(self.model)
        result = dbr.select(query)

        if result:
            raise Exception("The Robot already fetched the ticker")

        return True

