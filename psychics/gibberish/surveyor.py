# -*- coding: utf-8 -*-

from core.basics.base_classes import BaseSurveyor
from core.database.connection import DbWriter
from core.database.connection import DbReader

class BarrelProof(BaseSurveyor):

    def reckon(self):
        dbr = DbReader(self.model)
        qs = self.extractor.latest()
        # do stuff
