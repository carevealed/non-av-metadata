#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class CNode(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def __make_xml(self):
		pass

	@classmethod
	def get_xml(self):
		pass

	@classmethod
	def __repr__(self):
		pass

	@classmethod
	def validate_tag(self):
		pass

	@classmethod
	def validate_attribute(self):
		pass

