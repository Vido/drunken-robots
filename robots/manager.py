# -*- coding: utf-8 -*-

import os
import sys

abs_path = os.path.abspath( __file__ )
basedir = os.path.dirname(abs_path)
sys.path.append(basedir)

MANEGED_ROBOTS = (
    'PETR4',
)

def run_robots(robots_list):

    # modules = map(__import__, robots_list)
    modules = []

    for robot in robots_list:
        try:
            module = __import__(robot, globals())
            modules.append(module)
        except Exception as e:
            print "Robot %s has problems:\n %s" % (robot, e)
            continue

    for module in modules:
        try:
            module.rules.should_it_run()
        except Exception as e:
            print "Robot %s skiped:\n %s" % (module.__name__, e)
            continue

        try:
            print "Running %s robot..." % module.__name__,
            module.robot.make_your_magic()
            print " OK."
        except Exception as e:
            print "Robot %s failed! \n %s" % (module.__name__, e)

if __name__ == '__main__':

    if len(sys.argv[1:]) == 0:
        robots_list = MANEGED_ROBOTS
    else:
        robots_list = sys.argv[1:]

    run_robots(robots_list)

