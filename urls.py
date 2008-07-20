from django.conf.urls.defaults import *
from django.contrib import admin
from pastiche import settings

admin.autodiscover()

urlpatterns = patterns('pastiche.dada.views',
	(r'^dada[/]$', 'index'), # [/] for optional trailing /
	(r'^dada/(?P<item>\d+)[/]$', 'item'),
	(r'^dada/(?P<note>\d+)[/]$', 'note'),
	(r'^dada/(?P<link>\d+)[/]$', 'link'),
	(r'^dada/(?P<tag>\d+)[/]$', 'tag'),
	(r'^dada/(?P<location>\d+)[/]$', 'location'),
	(r'^dada/(?P<node>\d+)[/]$', 'node'),
	(r'^dada/(?P<task>\d+)[/]$', 'task'),
	(r'^dada/(?P<event>\d+)[/]$', 'event'),
)

urlpatterns += patterns('',
	(r'^$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'path':'index.html'}),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/(.*)', admin.site.root),
)
