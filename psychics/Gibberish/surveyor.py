# -*- coding: utf-8 -*-

from datetime import datetime

from core.basics.base_classes import BaseSurveyor
from core.database.connection import DbWriter
from core.database.connection import DbReader

class BarrelProof(BaseSurveyor):

    def reckon(self):
        qs = self.not_measured_yet()
        dbw = DbWriter(self.model)

        for pk, future, price in qs:
            splited_date = [int(d) for d in future.split('-')]
            date = datetime(*splited_date)
            rs = self.extractor.benchmark(date)
            value = rs[0][5]
            #TODO extractor could retrun a list of dict
            dbw.write(pk, value, value-price, table='truth')
            #from IPython import embed; embed()


    def not_measured_yet(self):
        dbr = DbReader(self.model)
        query = "SELECT pk, future_date, price FROM prediction"\
            " as t WHERE t.pk NOT IN (SELECT fk FROM truth);"
        qs = dbr.select(query)
        return qs
