# -*- coding: utf-8 -*-

import os
import unittest

from connection import DbWriter
from connection import DbReader

try:
    os.remove('*.sqlite3')
except OSError as e:
    pass


class Model1():

    DB_FILE = 'test1.sqlite3'
    SCHEMA = {
        'table_test': [
            ('fieldA', 'TEXT'),
        ]
    }

    def validate(self, *args, **which_table):

        which_table['table']
        
        context = {
            'fieldA': args[0]
        }

        return context


class TestDbWriter1(unittest.TestCase):

    db_model = Model1()
    dbc = DbWriter(db_model)

    def test_start(self):
        fp = open(self.db_model.DB_FILE, 'r')
        fp.close()

    def test_write(self):
        self.dbc.write("'TEST.SA'", table='table_test')
        # TODO: Check inside the sqlite file


class Model3():

    DB_FILE = 'test3.sqlite3'
    SCHEMA = {
        'table_test': [
            ('fieldA', 'TEXT'),
            ('fieldB', 'TEXT'),
            ('fieldC', 'TEXT'),
        ]
    }

    def validate(self, *args, **which_table):

        which_table['table']

        context = {
            'fieldA': args[0],
            'fieldB': args[1],
            'fieldC': args[2],
        }

        return context


class TestDbWriter3(unittest.TestCase):

    db_model = Model3()
    dbc = DbWriter(db_model)

    def test_start(self):
        fp = open(self.db_model.DB_FILE, 'r')
        fp.close()

    def test_write(self):
        self.dbc.write("'TEST.SA'", "'FOO'", "'BAR'", table='table_test')
        # TODO: Check inside the sqlite file


class TestDbReader(unittest.TestCase):

    db_model = Model3()

    dbcw = DbWriter(db_model)
    dbcw.write("'TEST.SA'", "'FOO'", "'BAR'", table='table_test')

    def test_select(self):
        dbcr = DbReader(self.db_model)
        result = dbcr.select("SELECT * FROM table_test ;")
        assert len(result) != 0


if __name__ == '__main__':
    unittest.main()
