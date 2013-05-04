# -*- coding: utf-8 -*-

from core.basics.base_classes import BaseSurveyor
from core.database.connection import DbWriter
from core.database.connection import DbReader

class BarrelProof(BaseSurveyor):

    def reckon(self):
        pass

    def not_measured_yet(self):
        dbr = DbReader(self.model)
        query = "SELECT * FROM prediction as t WHERE t.pk "\
        " NOT IN (SELECT fk FROM truth);"
        qs = dbr.select(query)
        #print qs
        return qs
