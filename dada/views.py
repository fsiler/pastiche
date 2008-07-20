from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from pastiche.dada.models import Item, Note, Link, Task, Event


def index(request):
	top_items = Item.objects.filter(parent=None)
#	top_items = Item.objects.filter(dependent=False)
	items = Item.objects.all()
	tasks = Task.objects.all()
	events = Event.objects.all()
	notes = Note.objects.all()#filter(item=None)
	links = Link.objects.all()#filter(item=None)

	# simple
	return render_to_response('dada/index.html', {'top_items': top_items, 'items': items, 'tasks': tasks, 'events': events, 'notes': notes, 'links': links}, context_instance=RequestContext(request))

	## complicated
	#t = loader.get_template('dada/index.html')
	#c = Context({
	#	'items': items,
	#})
	#return HttpResponse(t.render(c))



# decorator: http://www.djangosnippets.org/snippets/821/

def render_to(template):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter

    Parameters:

     - template: template name to use
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer

#Decorator, written for views simplification. Will render dict, returned by view, as context for template, using RequestContext. Additionally you can override template, returning two-tuple (context's dict and template name) instead of just dict.
#
#Usage:
#
#@render_to('my/template.html')
#def my_view(request, param):
#    if param == 'something':
#        return {'data': 'some_data'}
#    else:
#        return {'data': 'some_other_data'}, 'another/template.html'
