# -*- coding: utf-8 -*-

import os
import sqlite3
import unittest

from core.basics.base_classes import BasePsychic
from core.basics.base_classes import BaseExtractor
from core.database.standard_models import PsychicModel

from surveyor import BarrelProof

TEST_DB = 'db_test.sqlite3'

class DummyExtractor(BaseExtractor):
    def benchmark(self):
        pass 

class SmartExtractor(BaseExtractor):

    conn = sqlite3.connect(TEST_DB)

    def benchmark(self, date):
        assert not self.is_future(date)
        cur = self.conn.cursor()
        str_date = date.strftime('%Y-%m-%d')
        query = "SELECT * FROM ticker WHERE date == '%s' ;" % str_date
        cur.execute(query) 
        qs = cur.fetchall()
        # return qs #  OLD
        return self.ship_stuff(meta=('pk', 'foo', 'bar'), datum=qs) #  NEW

MODEL = PsychicModel()
MODEL.DB_FILE = TEST_DB 

class BarrelProofTest(unittest.TestCase):

    surveyor = BarrelProof(MODEL, DummyExtractor())
    
    def test_not_measured_yet(self):
   
        qs = self.surveyor.not_measured_yet()
        assert len(qs) == 2

        conn = sqlite3.connect(TEST_DB)
        cur = conn.cursor()
        query = "INSERT INTO truth VALUES(2, 20.10, 0.54)"
        cur.execute(query)
        conn.commit()
        
        qs = self.surveyor.not_measured_yet()
        assert len(qs) == 1

    def test_reckon(self):
        self.surveyor = BarrelProof(MODEL, SmartExtractor())
        self.surveyor.reckon()

        conn = sqlite3.connect(TEST_DB)
        cur = conn.cursor()
        # Because fk == 2 is already on the table
        query = "SELECT * FROM truth WHERE fk != 2;"
        cur.execute(query)
        qs = cur.fetchall()
        assert qs == [(1, 20.09, 0.4292878186)]
 
if __name__ == '__main__':

    # Remove (rm -rf) old database
    try:
        os.remove(TEST_DB)
    except OSError:
        pass

    script = open('dump.sql', 'r').read()
    conn = sqlite3.connect(TEST_DB)
    cur = conn.cursor()
    cur.executescript(script)
    cur.close()
    conn.close()

    unittest.main()
