#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
import Model.CAssetPart
from Model import CDescriptionDocument
from Model.CNode import CNode

class CAssets(CNode):
    def __make_xml(self):
        pass

    def __init__(self):
        self.__objectID = None
        """@AttributeType Model.Element"""
        self.__projectID = None
        """@AttributeType Model.Element"""
        self.__physicalLocation = None
        """@AttributeType Model.Element"""
        self.__dimensionsHeight = None
        """@AttributeType Model.Element"""
        self.__dimensionsWidth = None
        """@AttributeType Model.Element"""
        self.__color = None
        """@AttributeType Model.Element"""
        self.__hasParts = None
        """@AttributeType Model.Element"""
        self.__additionalDescription = None
        """@AttributeType Model.Element"""
        self.__assetPart = None
        """@AttributeType Model.CAssetPart"""
        self.unnamed_CDescriptionDocument_ = None
        # @AssociationType Model.CDescriptionDocument
        self.unnamed_CAssetPart_ = None
        # @AssociationType Model.CAssetPart
        # @AssociationKind Composition

