#!/usr/bin/env python

import pastiche
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'pastiche.settings'

from datetime import datetime
from dada.models import Event, Link, Location, Note, Tag, Task
from django.contrib.auth.models import User

def empty_table(table):
	for o in table.objects.all():
		o.delete()

#empty_table(Item)
#empty_table(HierarchicalItem)
empty_table(Note)
empty_table(Link)
empty_table(Location)
empty_table(Tag)
#empty_table(Task) # TODO: probably need to delete according to hierarchy
#empty_table(Event)	# TODO: same

u1 = User.objects.get(username='andre')

t1 = Task()
t1.title = 'first task'
t1.user = u1
t1.save()

t2 = Task()
t2.user = u1
t2.parent = t1
t2.title = 'second task'
t2.save()

t3 = Task()
t3.user = u1
t3.parent = t1
t3.title = 'third task'
t3.due = datetime.now()
t3.save()

t4 = Task()
t4.user = u1
t4.parent = t2
t4.title = 'fourth task'
t4.done = True
t4.save()

e1 = Event()
e1.title = 'first event'
e1.user = u1
e1.rating = 4
e1.start = datetime.now()
e1.stop = datetime(2008, 10, 31, 12, 34, 56)
e1.save()

e2 = Event()
e2.title = 'second event'
e2.user = u1
e2.rating = 2
e2.start = datetime.now()
e2.stop = datetime(2008, 10, 31, 12, 34, 56)
e2.save()

e3 = Event()
e3.title = 'first subevent'
e3.user = u1
e3.parent = e2
e3.start = datetime.now()
e3.stop = datetime(2008, 9, 18, 12, 34, 56)
e3.save()

e4 = Event()
e4.title = 'second subevent'
e4.user = u1
e4.parent = e2
e4.start = datetime(2008, 9, 18, 12, 34, 56)
e4.stop = datetime(2008, 10, 31, 12, 34, 56)
e4.save()

l1 = Link()
l1.title = 'first link'
l1.user = u1
l1.private = True
l1.url = 'http://pastiche.info'
l1.item = e3
l1.save()

n1 = Note()
n1.title = 'first note'
n1.user = u1
n1.text = 'pastiche.info is a playground for experiments in technology, philosophy and arts.'
n1.item = l1 # add item to note
n1.save()

n2 = Note()
n2.title = 'second note'
n2.user = u1
n2.text = 'pastiche.info is a playground for experiments in technology, philosophy and arts.'
n2.save()

l2 = Link()
l2.title = 'second link'
l2.user = u1
l2.private = True
l2.url = 'http://pastiche.info'
l2.item = t4
l2.save()
l2.notes.add(n2) # add note to item (after save!)

l3 = Link()
l3.title = 'third link'
l3.user = u1
l3.url = 'http://pastiche.info'
l3.item = t1
l3.save()

l4 = Link()
l4.title = 'fourth link'
l4.user = u1
l4.url = 'http://pastiche.info'
l4.item = t1
l4.save()

n3 = Note()
n3.title = 'third note'
n3.user = u1
n3.text = 'pastiche.info is a playground for experiments in technology, philosophy and arts.'
n3.item = t1
n3.save()

n4 = Note()
n4.title = 'fourth note'
n4.user = u1
n4.text = 'pastiche.info is a playground for experiments in technology, philosophy and arts.'
n4.item = t3
n4.save()

n5 = Note()
n5.title = 'fifth note'
n5.user = u1
n5.text = 'pastiche.info is a playground for experiments in technology, philosophy and arts.'
n5.item = e2
n5.save()

n6 = Note()
n6.title = 'sixth note'
n6.user = u1
n6.text = 'pastiche.info is a playground for experiments in technology, philosophy and arts.'
n6.item = e4
n6.save()

print 'db populated.'

###
#t = SimpleTask()
#t.title = 'first task'
#t.done = False
#t.save()
#n = SimpleNote()
#n.title = 'first note'
#n.text = "just some text for this note."
#n.item = t
#n.save()
##t.notes.add(n)
#n.item
#n.item.title
#t.notes
#t.notes.count()
#t.notes.all()[0].title
