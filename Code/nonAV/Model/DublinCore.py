#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
import Model.DescriptionDocument
from Model import CAPS_node

class DublinCore(CAPS_node):
    def __init__(self):
        self.__title = []
        """@AttributeType list
        List of Model.Element objects"""
        self.__creator = []
        """@AttributeType list
        List of Model.Element objects"""
        self.__subject = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__description = None
        """@AttributeType Model.Element"""
        self.__publisher = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__contributor = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__date = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__type = None
        """@AttributeType Model.Element"""
        self.__format = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__identifier = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__source = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__language = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__relation = None
        """@AttributeType Model.Element"""
        self.__coverage = []
        """@AttributeType list
        List of Model.Element objects."""
        self.__rights = None
        """@AttributeType Model.Element"""
        self.unnamed_DescriptionDocument_ = None
        # @AssociationType Model.DescriptionDocument
        self.unnamed_Element_ = None
        # @AssociationType Model.Element

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

