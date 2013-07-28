#!/usr/bin/env python
# -*-coding: utf-8 -*-

import os
import sys

abs_path = os.path.abspath( __file__ )
basedir = os.path.dirname(abs_path)
sys.path.append(basedir)

MANEGED_ROBOTS = (
    'PETR4',
#    'ITUB4'
)

def run_robots(modules_list):

    robots_list = []

    for module in modules_list:
        try:
            robot_module = __import__(module, globals())
            robot_class = getattr(robot_module, robot_module.__name__)
            robots_list.append(robot_class)
        except Exception as e:
            print "Robot %s has problems:\n %s" % (module, e)
            continue

    for robot_class in robots_list:
        try:
            robot = robot_class()
            robot.time_to_work()
        except Exception as e:
            print "Robot %s skiped:\n %s" % (robot_class.__name__, e)
            continue

        try:
            print "Running %s robot..." % robot_class.__name__,
            robot.do_your_job()
            print " OK."
        except Exception as e:
            print "Robot %s failed! \n %s" % (robot_class.__name__, e)

if __name__ == '__main__':
    
    os.chdir(basedir) 
    
    if len(sys.argv[1:]) == 0:
        modules_list = MANEGED_ROBOTS
    else:
        modules_list = sys.argv[1:]

    run_robots(modules_list)

