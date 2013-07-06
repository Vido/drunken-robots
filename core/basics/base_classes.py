# -*- coding: utf-8 -*-

from collections import namedtuple
from datetime import datetime

class BaseModel():
    def __init__(self):
        if 'validate' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method validate() is not set')


class BaseRobot():
    model = None

    def __init__(self):
        if not self.model:
            #TODO Custom Exceptions
            raise Exception('Model is not set')

        if 'do_your_job' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method do_your_job() is not set')

        if 'time_to_work' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method time_to_work() is not set')


class BaseExtractor():
    def __init__(self):
        if 'benchmark' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method benchmark() is not set')

    # TODO: Overload __getattr__

    def ship_stuff(self, **kwargs):
        if '*' not in kwargs['meta']:
            QuerySetTuple = namedtuple('QuerySet', tuple(kwargs['meta']))
            print [d for d in kwargs['datum']] # DEBUG
            QuerySet = [QuerySetTuple(*d) for d in kwargs['datum']]
        else:
            QuerySet = list(kwargs['datum'])

        return QuerySet
        
    def is_future(self, some_date):
        now = datetime.now()
        delta = now - some_date
        return delta.total_seconds() < 0
 

class BaseSurveyor():
    def __init__(self, model, extractor):
        self.model = model
        self.extractor = extractor

        if 'not_measured_yet' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method not_measured_yet() is not set')


        if 'reckon' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method reckon() is not set')


class BasePsychic():
    model = None
    extractor = None

    def __init__(self):
        if not self.model:
            #TODO Custom Exceptions
            raise Exception('Model is not set')

        if not self.extractor:
            #TODO Custom Exceptions
            raise Exception('Extractor is not set')

        if not self.surveyor:
            #TODO Custom Exceptions
            raise Exception('Surveyor is not set')

        if 'make_your_magic' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method make_your_magic() is not set')

