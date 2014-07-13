from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'botaniser.settings')

from dj_static import Cling


application = Cling(get_wsgi_application())
