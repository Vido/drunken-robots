# -*- coding: utf-8 -*-

import sqlite3


class DbBaseClass():

    def __init__(self, model):
        """ This should save the last state for database file """

        try:
            fp = open(model.DB_FILE, 'r')
            fp.close()
            # TODO: If someone creates a db, and then make a 'drop table',
            # it won't work as expected

        except IOError:

            for table in model.SCHEMA.keys():

                template = "CREATE TABLE %s (" % table

                # Gets all fields but the last
                for field in model.SCHEMA[table][:-1]:
                    template += "%s %s," % (field)

                # This is needed for the comma syntax issue
                template += "%s %s" % (model.SCHEMA[table][-1])
                template += ");"

                context = {}
                query = template.format(**context)

                self.connection = sqlite3.connect(model.DB_FILE)
                self.raw_query(query)
                self.connection.close()

        self.model = model


class DbWriter(DbBaseClass):

    def raw_query(self, query):
        """ Send write-queries the database """
        cursor = self.connection.cursor()
        #print query # DEBUG
        cursor.execute(query)
        self.connection.commit()

    def write(self, *args, **which_table):

        table = which_table['table']

        model_template = "INSERT INTO " \
            "%s ({columns}) VALUES ({values});" % table

        columns = ""
        values = ""

        # Filters tuples like ("", "FOREIGN KEY(fk) REFERENCES table(pk))
        fields = [field for field in self.model.SCHEMA[table] if field[0]]

        for field in fields[:-1]:
            columns += "%s, " % field[0]
            values += "{%s}, " % field[0]

        columns += "%s" % fields[-1][0]
        values += "{%s}" % fields[-1][0]

        model_context = {
            'columns': columns,
            'values': values,
        }

        query_template = model_template.format(**model_context)
        query_context = self.model.validate(*args, table=table)
        query = query_template.format(**query_context)

        self.connection = sqlite3.connect(self.model.DB_FILE)
        #print query # DEBUG
        self.raw_query(query)
        self.connection.close()


class DbReader(DbBaseClass):
    def raw_query(self, query):
        """ Send read-queries the database """
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def select(self, query):
        self.connection = sqlite3.connect(self.model.DB_FILE)
        #print query # DEBUG
        result = self.raw_query(query)
        self.connection.close()
        return result
