# -*- coding: utf-8 -*-


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
        pass


class BaseSurveyor():
    def __init__(self, model, extractor):
        self.model = model
        self.extractor = extractor

        if 'not_measured_yet' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method not_measured_yet() is not set')


        if 'reckon' not in dir(self):
            #TODO Custom Exceptions
            raise Exception('Method make_your_magic() is not set')


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

