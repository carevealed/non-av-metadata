#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Model.CDescriptionDocument
from Model.CNode import CNode

class CCollectionReference(CNode):
    def __make_xml(self):
        pass

    def __init__(self):
        self.__descriptionDocument = None
        """@AttributeType Model.CDescriptionDocument"""
        self.__attributes = None
        """@AttributeType OrderedDict"""
        self.unnamed_CDescriptionDocument_ = None
        # @AssociationType Model.CDescriptionDocument
        # @AssociationKind Composition

