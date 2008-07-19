from django.conf.urls.defaults import *
from django.contrib import admin
from pastiche import settings

admin.autodiscover()

urlpatterns = patterns('pastiche.dada.views',
	(r'^dada[/]$', 'index'), # [/] for optional trailing /
	(r'^dada/(?P<item>\d+)[/]$', 'detail'),
)

urlpatterns += patterns('',
	(r'^$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'path':'index.html'}),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/(.*)', admin.site.root),
)
