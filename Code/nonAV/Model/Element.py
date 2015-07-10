#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Element(object):
	def Element(self, *args, **kwargs):
		pass

	def get_attributes(self):
		"""@ReturnType OrderedDict"""
		pass

	def add_attribute(self, key, value):
		"""@ParamType key string
		The name part of the name/value pair
		@ParamType value string
		The value part of the name/value pair.
		@ReturnType void"""
		pass

	def delete_attribute(self, key):
		"""@ParamType key string
		@ReturnType void"""
		pass

	def __repr__(self):
		"""Returns the XML element as an etree element.
		@ReturnType etElement"""
		pass

	def get_data(self):
		"""@ReturnType string"""
		pass

	def __init__(self):
		self.__tag = None
		"""@AttributeType string"""
		self.__data = None
		"""@AttributeType string"""
		self.__attributes = None
		"""@AttributeType OrderedDict
		Contains all the attributes for a given XML element."""

