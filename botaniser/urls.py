from django.conf.urls import patterns, include, url
from rest_framework import routers
from core import views
from api import views as api_views

from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()


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


urlpatterns += patterns('',
    url(r'species/$', views.SpeciesList.as_view()),
    url(r'^species/(?P<pk>[0-9]+)/$', views.SpeciesDetail.as_view()),
    url(r'^users/$', api_views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', api_views.UserDetail.as_view()),
)