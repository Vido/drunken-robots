#!/usr/bin/env python
# -*-coding: utf-8 -*-

import os
import sys

abs_path = os.path.abspath( __file__ )
basedir = os.path.dirname(abs_path)
sys.path.append(basedir)


MANEGED_PSYCHICS = (
    'Gibberish',
)

def run_psychics(modules_list):

    psychics_list = []

    for module in modules_list:
        try:
            psychic_module = __import__(module, globals())
            psychic_class = getattr(psychic_module, psychic_module.__name__)
            psychics_list.append(psychic_class)
        except Exception as e:
            print "Psychic %s has problems:\n %s" % (module, e)
            continue

    for psychic_class in psychics_list:

        try:
            psychic = psychic_class()
            print "Running %s psychic..." % psychic_module.__name__,
            psychic.make_your_magic()
            print " OK."
        except Exception as e:
            raise
            print "Psychic %s failed! \n %s" % (psychic_module.__name__, e)

if __name__ == '__main__':

    os.chdir(basedir)

    if len(sys.argv[1:]) == 0:
        modules_list = MANEGED_PSYCHICS
    else:
        modules_list = sys.argv[1:]

    run_psychics(modules_list)

