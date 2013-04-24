# -*- coding: utf-8 -*-


class Model():

    DB_FILE = "PETR4/PETR4.sqlite3"

    SCHEMA = {
        'ticker': [
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

        if which_table['table'] == 'ticker':
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
