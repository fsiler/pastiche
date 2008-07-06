from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
	title = models.CharField(max_length=512)
	rating = models.IntegerField(default = 3, null=True, blank=True)
	private = models.BooleanField(default=False)	# TODO: share in groups?
	user = models.ForeignKey(User, related_name='items')
	date = models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.title

#	class Meta:
#		abstract = True

class HierarchicalItem(Item):
#	children = models.ManyToManyField('self', related_name='parents')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

#	class Meta:
#		abstract = True


class Note(Item):
	text = models.TextField(null=True, blank=True)
	item = models.ForeignKey(Item, related_name='notes', null=True, blank=True)
	
	# TODO: __unicode__ seams not to work on TextField
	def __str__(self):
		return self.text


class Link(Item):
	url = models.URLField()
	item = models.ForeignKey(Item, related_name='links', null=True, blank=True)
	
	def __unicode__(self):
		return self.url


# TODO: requires PIL, http://www.pythonware.com/products/pil/
#class Drawing(Item): # scribble
#	image = models.ImageField(null=True, blank=True)
#	item = models.ForeignKey(Item, related_name='drawings', null=True, blank=True)


#TODO: use django-geo
#http://code.google.com/p/django-geo/
class Location(Item):
	latitude = models.FloatField()
	longitude = models.FloatField()
	altitude = models.FloatField()
	item = models.OneToOneField(Item, related_name='location')
	
	def __unicode__(self):
		return "(lat: %f, long: %f, alt: %f)" % self.latitude, self.longitude, self.altitude


##TODO: use django-tagging
#http://code.google.com/p/django-tagging/
class Tag(models.Model):
	name = models.CharField(max_length=128)
	items = models.ManyToManyField(Item, related_name='tags')
	date = models.DateField(auto_now=True)
#from tagging.fields import TagField
# 
#class Post(models.Model):
#	....
#	tags = TagField()
# 
##in your template. For example, object_details
#{% load tagging_tags %}
# 
#{% tags_for_object object as tag_list %}
#
#{% if tag_list %}
#	Tags:
#		{% for tag in tag_list %}
#		{{ tag }}{% if not forloop.last %}, {% endif %}
#		{% endfor %}
# {% endif %}
##


class Task(HierarchicalItem):
	done = models.BooleanField()
	due = models.DateTimeField(null=True, blank=True)
#	repeat = ?


class Event(HierarchicalItem):
	start = models.DateTimeField(verbose_name='from')
	stop = models.DateTimeField(verbose_name='until')




#
#	_tags = ManyToMany('Tag', inverse='items')
#
#	def _get_tags(self):
#		return self._tags
#
#	def _set_tags(self, data):
#		"""Updates the Item's tags, adds missing Tag objects and
#		keeps the relationships in sync.
#
#		@param data Either a comma separated string or a list of strings"""
#		if isinstance(data, basestring):
#			# Turn the data into a list
#			data = data.split(",")
#
#		# Create a normalised list of the new tag names
#		new_tags = [Tag.normalise_tag_name(tag) for tag in data]
#
#		# Create a list of the current tag names
#		old_tags = [t.name for t in self._tags]
#
#		if not old_tags == new_tags:
#			# Create a transaction for this little section
#			trans = session.create_transaction()
#
#			# Clear our old tags
#			self._tags = []
#
#			for tag_name in new_tags:
#				tag_obj = Tag.get_by(_name=tag_name)
#				if not tag_obj:
#					# We need to create this tag in the DB
#					tag_obj = Tag(tag_name)
#				self._tags.append(tag_obj)
#
#			# We're done.  Commit the transaction
#			trans.commit()
#
#	tags = property(_get_tags, _set_tags)
#	
#	def __repr__(self):
##		return '<Item "%s", parents: %s, children: %s>' % (self.title, self.parents, self.children)
#		return '<Item "%s">' % (self.title)
##		return str([v + ': ' + str(getattr(self, v, '-')) for v in vars(self)]) 
#


#class SimpleItem(models.Model):
#	title = models.CharField(max_length=512)
#
#class SimpleTask(SimpleItem):
#	done = models.BooleanField()
#	due = models.DateTimeField(null=True, blank=True)
#
#class SimpleNote(SimpleItem):
#	text = models.TextField(null=True, blank=True)
#	item = models.ForeignKey(SimpleItem, related_name='notes', null=True, blank=True)
