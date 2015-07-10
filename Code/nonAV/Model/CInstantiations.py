#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Model.CAssetPart
from Model import CInstantiantion
from Model.CNode import CNode

class CInstantiations(CNode):
    def __make_xml(self):
        pass

    def __init__(self):
        self.__attributes = None
        """@AttributeType OrderedDict"""
        self.__instantiation = None
        """@AttributeType CInstantiation*"""
        self.unnamed_CAssetPart_ = None
        # @AssociationType Model.CAssetPart
        self.unnamed_CInstantiantion_ = None
        # @AssociationType Model.CInstantiantion
        # @AssociationKind Composition

