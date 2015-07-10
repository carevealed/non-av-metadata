#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
from Model import CInstantiantion
from Model import CNode

class CTechnical(CNode):
	def __make_xml(self):
		pass

	def __init__(self):
		self.__fileFormat = None
		"""@AttributeType Model.Element"""
		self.__imageFormat = None
		"""@AttributeType Model.Element"""
		self.__resolutionWidth = None
		"""@AttributeType Model.Element"""
		self.__resolutionHeight = None
		"""@AttributeType Model.Element"""
		self.__colorSpace = None
		"""@AttributeType Model.Element"""
		self.__chromaSubsampling = None
		"""@AttributeType Model.Element"""
		self.__colorDepth = None
		"""@AttributeType Model.Element"""
		self.__compressionMode = None
		"""@AttributeType Model.Element"""
		self.__additionalTechnicalNotes = None
		"""@AttributeType Model.Element"""
		self.unnamed_CInstantiantion_ = None
		# @AssociationType Model.CInstantiantion

