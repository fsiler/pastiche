from django.db import models
from django.contrib import admin
import datetime

#TODO: move admin stuff to admin.py, see below


class Item(models.Model):
	title = models.CharField(max_length=128)
#	parents = models.ManyToManyField(Item, related_name='children')
	rating = models.IntegerField()
#	user_id = Field(Integer)
	user_id = models.CharField(max_length=128)
	date = models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.title


class Comment(models.Model):
	date = models.DateField(auto_now=True)
	text = models.TextField(null=True, blank=True)
	item = models.ForeignKey(Item, related_name='comments')

	def __unicode__(self):
		return "%s: %s (%s)" % (self.item, self.text, self.date)


class Tag(models.Model):
	name = models.CharField(max_length=128)
	items = models.ManyToManyField(Item, related_name='tags')

	def __unicode__(self):
		return self.name


class Task(Item):
	done = models.BooleanField()
	due = models.DateField(null=True, blank=True)
#	repeat = ?

	def __unicode__(self):
		return self.title


class Link(Item):
	uri = models.CharField(max_length=1024)

	def __unicode__(self):
		return self.title


# admin.py

# A proposal convention:
# Specifying all admin options in a file called admin.py, and import it in the __init__.py file
# of your application module to do the registering during the initialization.

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1


class TagInline(admin.StackedInline):
	model = Tag
	extra = 1


class ItemOptions(admin.ModelAdmin):
	model = Item
	inlines = [CommentInline, TagInline]


admin.site.register(Item, ItemOptions)
admin.site.register(Comment, CommentInline)
admin.site.register(Tag, TagInline)
admin.site.register(Task)
admin.site.register(Link)


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
