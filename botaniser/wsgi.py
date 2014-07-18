"""
WSGI config for botaniser project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application
import os

if os.environ['USER'] == 'ubuntu':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")

application = get_wsgi_application()
