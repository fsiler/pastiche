from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from pastiche.dada.models import Item, Comment, Tag, Task, Link

def index(request):
	items = Item.objects.all() #.order_by('-dpro')

	# simple
	return render_to_response('dada/index.html', {'items': items})

	# complicated
	t = loader.get_template('dada/index.html')
	c = Context({
		'items': items,
	})
	return HttpResponse(t.render(c))
