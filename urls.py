from django.conf.urls.defaults import *
from django.contrib import admin
from pastiche import settings

urlpatterns = patterns('pastiche.dada.views',
	(r'^/$', 'dada.index'),	#TODO: not working
	(r'^dada/$', 'index'),
	(r'^dada/(?P<item>\d+)/$', 'detail'),
)

urlpatterns += patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	(r'^admin/(.*)', admin.site.root),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
