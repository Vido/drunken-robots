# -*- coding: utf-8 -*-

from core.basics.base_classes import BaseModel

class PsychicModel(BaseModel):

    DB_FILE = ""

    SCHEMA = {
        'prediction': [
            ("", "pk INTEGER PRIMARY KEY AUTOINCREMENT"),
            ("", "present_date DATETIME " \
                 " DEFAULT (DATETIME('now', 'localtime'))"),
            ("future_date", "DATETIME"),
            ("symbol", "TEXT"),
            ("price", "REAL"),
        ],

        'truth': [
            ("fk", "INTEGER UNIQUE"),
            ("price", "REAL"),
            ("error", "REAL"),
            ("", "FOREIGN KEY(fk) REFERENCES prediction(pk)"),
        ],
    }


    def validate(self, *args, **which_table):

        if which_table['table'] == 'prediction':
            if len(args) != 3:
                raise Exception("Invalid number of arguments")

            #TODO: check the future_date
            float(args[2])

            context = {
                'future_date': args[0],
                'symbol': args[1],
                'price': args[2],
            }

        elif which_table['table'] == 'truth':

            if len(args) != 3:
                raise Exception("Invalid number of arguments")

            #TODO: check the FK
            float(args[1])
            float(args[2])

            context = {
                'fk': args[0],
                'price': args[1],
                'error': args[2],
            }

        else:
            message = "Invalid table=%s argument" % which_table['table']
            raise Exception(message)

        return context


class CandlestickModel(BaseModel):

    DB_FILE = ""

    SCHEMA = {
        'candle': [
            ("symbol", "TEXT"),
            ("date", "TEXT"),
            ("open", "REAL"),
            ("high", "REAL"),
            ("low", "REAL"),
            ("close", "REAL"),
            ("volume", "REAL"),
        ]
    }

    def validate(self, *args, **which_table):

        if which_table['table'] == 'candle':
            if len(args) != 7:
                raise Exception("Invalid number of arguments")

            for arg in args[2:]:
                float(arg)

            context = {
                'symbol': args[0],
                'date': args[1],
                'open': args[2],
                'high': args[3],
                'low': args[4],
                'close': args[5],
                'volume': args[6],
            }

        else:
            message = "Invalid table=%s argument" % which_table['table']
            raise Exception(message)

        return context
