#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
from Model import CTechnical
from Model import CInstantiations
from Model import CNode

class CInstantiantion(CNode):
	def __make_xml(self):
		pass

	def __init__(self):
		self.__fileName = None
		"""@AttributeType Model.Element"""
		self.__fileSize = None
		"""@AttributeType Model.Element"""
		self.__checksum = None
		"""@AttributeType Model.Element"""
		self.__deritiveFrom = None
		"""@AttributeType Model.Element"""
		self.__technical = None
		"""@AttributeType Model.CTechnical"""
		self.__attributes = None
		"""@AttributeType OrderedDict"""
		self.unnamed_CInstantiations_ = None
		# @AssociationType Model.CInstantiations
		self.unnamed_CTechnical_ = None
		# @AssociationType Model.CTechnical
		# @AssociationKind Composition

