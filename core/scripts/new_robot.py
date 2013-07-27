# -*- coding: utf-8 -*-

import os
import sys

init_template = \
    'from robot import {name}\n' \
    '\n'

model_template = \
    '# -*- coding: utf-8 -*-\n' \
    '\n' \
    'from core.basics.base_classes import BaseModel\n' \
    '\n' \
    '\n' \
    'class Model(BaseModel):\n' \
    '\n' \
    '    def validate(self):\n' \
    '        pass\n' \
    '\n'

robot_template = \
    '# -*- coding: utf-8 -*-\n' \
    '\n' \
    'from core.basics.base_classes import BaseRobot\n' \
    '\n' \
    'from model import Model\n' \
    '\n' \
    '\n' \
    'class {name}(BaseRobot):\n' \
    '\n' \
    '    model = Model()\n' \
    '\n' \
    '\n' \
    '    def do_your_job(self):\n' \
    '        print "Hello World.",\n' \
    '\n' \
    '\n' \
    '    def time_to_work(self):\n' \
    '        return True\n' \
    '\n'


if __name__ == '__main__':
 
    name = sys.argv[-1]
    os.mkdir(name)
    os.chdir(name)

    robot_context = { 'name': name }
    model_context = {}
   
    with open('robot.py', 'w') as fp:
        rendered = robot_template.format(**robot_context)
        fp.write(rendered)

    with open('__init__.py', 'w') as fp:
        rendered = init_template.format(**robot_context)
        fp.write(rendered)

    with open('model.py', 'w') as fp:
        rendered = model_template.format(**model_context)
        fp.write(rendered)

