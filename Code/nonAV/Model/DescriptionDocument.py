#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import DublinCore
import Model.Assets
from Model import CollectionReference
from Model import CAPS_node

class DescriptionDocument(CAPS_node):
    def __init__(self):
        self.__dublinCore = None
        """@AttributeType Model.DublinCore"""
        self.__assets = None
        """@AttributeType Model.Assets"""
        self.unnamed_CollectionReference_ = None
        # @AssociationType Model.CollectionReference
        self.unnamed_DublinCore_ = None
        # @AssociationType Model.DublinCore
        # @AssociationKind Composition
        self.unnamed_Assets_ = None
        # @AssociationType Model.Assets
        # @AssociationKind Composition

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

