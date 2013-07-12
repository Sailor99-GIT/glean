from django.conf.urls import patterns, url

from gleanevent import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^$', views.gleanCalendar, name="gleancalendar"),
	url(r'^new/$', views.newGlean, name='newglean'),
	url(r'^(?P<glean_id>\d+)/$', views.detailGlean, name='detailglean'),
	url(r'^(?P<glean_id>\d+)/edit/$', views.editGlean, name='editglean'),
	url(r'^(?P<glean_id>\d+)/attending/$', views.confirmLink, name='confirmlink'),
	url(r'^(?P<glean_id>\d+)/notattending/$', views.denyLink, name='denylink'),
)