drunken-robots
==============

It's a little framework to deal with web-crawlers.
It's aimed for stock market crawlers.

--------------------------------------------------------------------------

I believe that it will be made of 4 main modules:

- robots:
    This will handle all the crawlers-sub-modules

- psychics:
    This will use the data that the crawlers gathered.
	Then it will guess something, some number, some date.
        Very deep magic here.

- 'i havent named it yet':
    It evals the guesses and measures the errors.
	Maybe it will plot beautiful graphs.

- core:
	A module to organize the API

--------------------------------------------------------------------------

_You must set PYTHONPATH to drunken-robots path_ 
There is 2 ways:

- Put on your ~/.pythonrc.py:
> import sys
> sys.path.append(/path/to/drunken-robots)

- Put on your ~/.bashrc:
> export PYTHONPATH=$PYTHONPATH:/path/to/drunken-robots

- Put on your c:\autoexec.bat (for Windows):
> set PYTHONPATH=%PYTHONPATH%;C:\PATH\TO\DRUNKEN-ROBOTS

