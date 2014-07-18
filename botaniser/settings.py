import os

if os.environ['USER'] == 'ubuntu':
	import settings.prod
	print 'importing settings.prod in settings.py '
else:
    import settings.dev
    print 'importing settings.dev in settings.py '

