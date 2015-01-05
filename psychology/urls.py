from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
                       url(r'^home/', include('manage_clients.urls',
                                              namespace='home',
                                              app_name='manage_clients')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^treenav/', include('treenav.urls')),
                       )
