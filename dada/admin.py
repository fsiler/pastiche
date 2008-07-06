#!/usr/bin/env python

# A proposal convention:
# Specifying all admin options in a file called admin.py, and import it in the __init__.py file
# of your application module to do the registering during the initialization.

from django.contrib import admin
from pastiche.dada.models import Item, HierarchicalItem, Note, Link, Location, Tag, Task, Event


class NoteInline(admin.StackedInline):
	model = Note
	extra = 1


class LinkInline(admin.StackedInline):
	model = Link
	extra = 1


class LocationInline(admin.StackedInline):
	model = Location
	extra = 1


class TagInline(admin.StackedInline):
	model = Tag
	extra = 1


class ItemOptions(admin.ModelAdmin):
	model = Item
	inlines = [NoteInline, LinkInline, LocationInline]


admin.site.register(Item, ItemOptions)
admin.site.register(HierarchicalItem)
admin.site.register(Note)
admin.site.register(Link)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Event)
