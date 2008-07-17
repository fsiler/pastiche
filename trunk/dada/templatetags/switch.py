#-*- coding: utf-8 -*-
# Copyright (C) 2008 Alfaiati - Tecnologia sob medida
#
#   Author: Gabriel Falcão <gabriel.falcao@alfaiati.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import md5
# Deprecated since release 2.5. Use the hashlib module instead.
# http://www.python.org/doc/current/lib/module-md5.html

from django import template
register = template.Library()


class SwitchNode(template.Node):
	def __init__(self, var1, nodelist_true, nodelist_false):
		self.comparison_base = template.Variable(var1)
		self.nodelist_true = nodelist_true
		self.nodelist_false = nodelist_false
		self.varname = var1
		
	def __repr__(self):
		return "<SwitchNode>"

	def render(self, context):
		try:
			val1 = self.comparison_base.resolve(context)
			bhash = "__%s__" % md5.new(self.varname).hexdigest()
			context[bhash] =  val1
		except template.VariableDoesNotExist:
			raise template.TemplateSyntaxError("Could not resolve variable %r in current context" % \
									  self.comparison_base.var)
		ok = False
		for node in self.nodelist_true:
			if isinstance(node, CaseNode):
				node.set_source(bhash)
				if node.get_bool(context):
					ok = True
		if ok:
			return self.nodelist_true.render(context)
		else:
			return self.nodelist_false.render(context)

@register.tag    
def switch(parser, token):
	"""
	Create a context to use case-like coditional
	template rendering.

	For example::

		{% switch person.name %}
			{% case 'John Doe' %}
				Hi! My name is John, the master!
			{% endcase %}
			{% case 'Mary Jane' %}
				Hello! My name is Mary. Nice to meet you!
			{% endcase %}            
		{% default %}
			Oh my God! I have no name!
		{% endswitch %}
	"""
	
	bits = list(token.split_contents())
	if len(bits) != 2:
		raise template.TemplateSyntaxError, "%r takes one argument" % bits[0]
	end_tag = 'end' + bits[0]
	nodelist_true = parser.parse(('default', end_tag,))
	token = parser.next_token()
	if token.contents == 'default':
		nodelist_false = parser.parse((end_tag,))
		parser.delete_first_token()
	else:
		nodelist_false = NodeList()
	return SwitchNode(bits[1], nodelist_true, nodelist_false)


class CaseNode(template.Node):
	def __init__(self, var, nodelist):
		self.var = template.Variable(var)
		self.nodelist = nodelist
		
	def __repr__(self):
		return "<CaseNode>"
	
	def set_source(self, var):
		""" Sets the varname to lookup in
		context and make the comparisons"""
		self.base_comparison = var
		
	def get_bool(self, context):
		try:
			val = self.var.resolve(context)
		except template.VariableDoesNotExist:
			val = None
			
		base_comparison = getattr(self, "base_comparison", None)
		if not base_comparison:
			raise LookupError("Could not find base_comparison. "
							  "Ensure to use {% case %} node "
							  "within a {% switch %} node")
		if context.get(self.base_comparison, None) == val:
			return True
		else:
			return False
		
	def render(self, context):
		if self.get_bool(context):
			return self.nodelist.render(context)
		else:
			return template.NodeList().render(context)


@register.tag    
def case(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 2:
		raise TemplateSyntaxError, "%r takes one argument" % bits[0]
	end_tag = 'end' + bits[0]
	nodelist_true = parser.parse(('else', end_tag))
	token = parser.next_token()
	if token.contents == 'else':
		nodelist_false = parser.parse((end_tag,))
		parser.delete_first_token()
	else:
		nodelist_false = template.NodeList()
	return CaseNode(bits[1], nodelist_true)
