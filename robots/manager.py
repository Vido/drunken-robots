import os
import sys

abs_path = os.path.abspath( __file__ )
basedir = os.path.dirname(abs_path)
sys.path.append(basedir)

MANEGED_ROBOTS = (
	'PETR4',
)

modules = map(__import__, MANEGED_ROBOTS)

#for robot  in MANEGED_ROBOTS:
#	exec('import %s' % robot)

for module in modules:
	print module.__file__
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


