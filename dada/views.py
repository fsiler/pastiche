from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from pastiche.dada.models import Item, Note, Link, Task, Event


# http://www.djangoproject.com/documentation/serialization/
#from django.core import serializers
#data = serializers.serialize("xml", SomeModel.objects.all())


def merge(left, right):
	"""http://en.literateprograms.org/Merge_sort_(Python)"""
	
	result = []
	i ,j = 0, 0
	while (i < len(left)) and (j < len(right)):
#		print left[i].modified, right[j].modified
		if (left[i].modified <= right[j].modified):
			result.append(left[i])
			i = i + 1
		else:
			result.append(right[j])
			j = j + 1
	result += left[i:]
	result += right[j:]
	return result

def index(request):
#	top_items_stripped = []
	top_items = Item.objects.filter(owner=None, parent=None).order_by('-modified')
	all_items = Item.objects.all()
	# ??? filter(owner__isnull=True)
	#print "top_items_1", len(top_items), top_items
	#for ti in top_items:
	#	try:
	#		if ti.note.item:
	#			print "xxx note", ti
	#		else:
	#			top_items_stripped.append(ti)
	#	except:
	#		pass
	#	try:
	#		if ti.link.item:
	#			print "xxx", ti
	#		else:
	#			top_items_stripped.append(ti)
	#	except:
	#		pass
	#print dir(top_items)
	#
	#top_notes = Note.objects.filter(owner=None).order_by('-modified')
	#top_links = Link.objects.filter(owner=None).order_by('-modified')
	#
	#print "top_items_2", len(top_items), top_items
	#print "top_notes", len(top_notes), top_notes
	#print "top_links", len(top_links), top_links
	#
	#items = merge(top_notes, top_links)
	#print len(items), items
	#
	#items = merge(items, top_items)
	#print len(items), items

	# simple
	return render_to_response('dada/index.html', {'items': top_items, 'all_items': all_items}, context_instance=RequestContext(request))

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
