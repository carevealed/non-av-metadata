#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Model.DescriptionDocument
from Model import CAPS_node

class CollectionReference(CAPS_node):
    def __init__(self):
        self.__descriptionDocument = None
        """@AttributeType Model.DescriptionDocument"""
        self.__attributes = None
        """@AttributeType OrderedDict"""
        self.unnamed_DescriptionDocument_ = None
        # @AssociationType Model.DescriptionDocument
        # @AssociationKind Composition

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

