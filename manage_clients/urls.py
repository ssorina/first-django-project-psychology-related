from django.conf.urls import patterns, url

from manage_clients import views

urlpatterns = patterns('',
                       url(r'^$', views.homepage, name='home'),
                       url(r'^get_name/$', views.get_name, name='get-name'),
                       url(r'^thanks/$', views.thanks, name='thanks'),
                       url(r'^(?P<title_id>\d+)/$', views.single_entry,
                           name='single_entry'),
                       url(r'^upload/$', views.opinion_upload,
                           name='upload'),
#                       url(r'^upload/?P(<psychopinion.id>)/$', views.opinion_upload,
#                           name='upload redirect'),
                       url(r'^psychologist/$', views.psychologist_page,
                           name='psychologist'),
                       url(r'^psychologist/(?P<name_id>\d+)/$',
                           views.psychologist_special,
                           name='psychologist_special'),
                       url(r'^patient/$', views.patient,
                           name='patient'),
                       url(r'^patient/(?P<name_id>\d+)/$', views.patient_experience,
                           name='patient_experience'),
                       )
