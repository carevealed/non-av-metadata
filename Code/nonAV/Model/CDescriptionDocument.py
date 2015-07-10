#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import CDublinCore
import Model.CAssets
from Model import CCollectionReference
from Model.CNode import CNode

class CDescriptionDocument(CNode):
    def __make_xml(self):
        pass

    def __init__(self):
        self.__dublinCore = None
        """@AttributeType Model.CDublinCore"""
        self.__assets = None
        """@AttributeType Model.CAssets"""
        self.unnamed_CCollectionReference_ = None
        # @AssociationType Model.CCollectionReference
        self.unnamed_CDublinCore_ = None
        # @AssociationType Model.CDublinCore
        # @AssociationKind Composition
        self.unnamed_CAssets_ = None
        # @AssociationType Model.CAssets
        # @AssociationKind Composition

