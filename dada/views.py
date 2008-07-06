from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from pastiche.dada.models import Item, HierarchicalItem, Note, Link, Tag, Task, Event


def index(request):
	items = Item.objects.all() #.order_by('-dpro')
	tasks = Task.objects.all()
	events = Event.objects.all()

	# simple
	return render_to_response('dada/index.html', {'items': items, 'tasks': tasks, 'events':events})

	## complicated
	#t = loader.get_template('dada/index.html')
	#c = Context({
	#	'items': items,
	#})
	#return HttpResponse(t.render(c))
