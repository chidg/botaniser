from django.conf.urls import patterns, include, url
from rest_framework import routers
from core import views
from api import views as api_views

from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
    (r'^api/', include(router.urls)),
    (r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^logout/$', api_views.logout_view, name='logout'),
)


urlpatterns += patterns('',
    url(r'^$', views.index, name='index'),
    url(r'species/$', views.SpeciesList.as_view()),
    url(r'^species/(?P<pk>[0-9]+)/$', views.SpeciesDetail.as_view()),
    url(r'reports/$', views.ReportList.as_view()),
    url(r'reports/add$', views.ReportCreate.as_view()),
    url(r'^reports/(?P<pk>[0-9]+)/$', views.ReportDetail.as_view()),
    url(r'^users/$', api_views.UserList.as_view(), name='user-list'),
    url(r'^users/add$', api_views.UserCreate.as_view(), name='user-add'),
    url(r'^users/(?P<pk>[0-9]+)/$', api_views.UserDetail.as_view(), name='user-detail'),
)

urlpatterns += patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)
