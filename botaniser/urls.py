from django.conf.urls import patterns, include, url
from rest_framework import routers
from core import views

from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'species', views.SpeciesViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'botaniser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^facebook/', include('django_facebook.urls')),
	(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
	(r'^', include(router.urls)),
	(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)


