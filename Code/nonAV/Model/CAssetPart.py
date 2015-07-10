#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import CInstantiations
from Model import CAssets

class CAssetPart(object):
    def __init__(self):
        self.__cInstantiations = None
        """@AttributeType Model.CInstantiations*"""
        self.unnamed_CAssets_ = None
        # @AssociationType Model.CAssets
        self.unnamed_CInstantiations_ = None
        # @AssociationType Model.CInstantiations
        # @AssociationKind Composition

