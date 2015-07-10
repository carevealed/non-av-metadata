#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
import Model.CDescriptionDocument
from Model.CNode import CNode

class CDublinCore(CNode):
    def __make_xml(self):
        pass

    def __init__(self):
        self.__title = None
        """@AttributeType Model.Element*"""
        self.__creator = None
        """@AttributeType Model.Element*"""
        self.__subject = None
        """@AttributeType Model.Element*"""
        self.__description = None
        """@AttributeType Model.Element"""
        self.__publisher = None
        """@AttributeType Model.Element*"""
        self.__contributor = None
        """@AttributeType Model.Element*"""
        self.__date = None
        """@AttributeType Model.Element*"""
        self.__type = None
        """@AttributeType Model.Element"""
        self.__format = None
        """@AttributeType Model.Element*"""
        self.__identifier = None
        """@AttributeType Model.Element*"""
        self.__source = None
        """@AttributeType Model.Element*"""
        self.__language = None
        """@AttributeType Model.Element*"""
        self.__relation = None
        """@AttributeType Model.Element"""
        self.__coverage = None
        """@AttributeType Model.Element*"""
        self.__rights = None
        """@AttributeType Model.Element"""
        self.unnamed_CDescriptionDocument_ = None
        # @AssociationType Model.CDescriptionDocument

