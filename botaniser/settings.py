import os

if os.environ['USER'] == 'ubuntu':
	from settings.prod import *
	print 'importing settings.prod in settings.py '
else:
    from settings.dev import *
    print 'importing settings.dev in settings.py '

