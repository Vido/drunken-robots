# -*- coding: utf-8 -*-

from datetime import datetime

from core.basics.base_classes import BaseSurveyor
from core.database.connection import DbWriter
from core.database.connection import DbReader

class BarrelProof(BaseSurveyor):

    def reckon(self):
        qs = self.not_measured_yet()

        for pk, future in qs:
            splited_date = [int(d) for d in future.split('-')]
            date = datetime(*splited_date)
            r = self.extractor.benchmark(date)
            from IPython import embed; embed()
            # TODO

    def not_measured_yet(self):
        dbr = DbReader(self.model)
        query = "SELECT pk, future_date FROM prediction as t WHERE t.pk "\
        " NOT IN (SELECT fk FROM truth);"
        qs = dbr.select(query)
        return qs
