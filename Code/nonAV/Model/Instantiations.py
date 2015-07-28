#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Model.AssetPart
from Model import Element
import Model.Instantiation
from Model import CAPS_node

class Instantiations(CAPS_node):
    def __init__(self):
        self.__attributes = None
        """@AttributeType OrderedDict"""
        self.__instantiation = []
        """@AttributeType list
        list of Instantiation Objects"""
        self.unnamed_AssetPart_ = None
        # @AssociationType Model.AssetPart
        self.unnamed_Element_ = None
        # @AssociationType Model.Element
        self.unnamed_Instantiation_ = None
        # @AssociationType Model.Instantiation
        # @AssociationKind Composition

    def add_instantiation(self, new_instantiation):
        """@ParamType new_instantiation Model.Instantiation"""
        pass

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

