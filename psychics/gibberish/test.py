# -*- coding: utf-8 -*-

import os
import sqlite3
import unittest

from core.basics.base_classes import BasePsychic
from core.basics.base_classes import BaseExtractor
from core.database.standard_models import PsychicModel

from surveyor import BarrelProof


class DummyExtractor(BaseExtractor):
    pass 

TEST_DB = 'db_test.sqlite3'

MODEL = PsychicModel()
MODEL.DB_FILE = TEST_DB
EXTRACTOR = DummyExtractor()


class BarrelProofTest(unittest.TestCase):

    surveyor = BarrelProof(MODEL, EXTRACTOR)
    
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
