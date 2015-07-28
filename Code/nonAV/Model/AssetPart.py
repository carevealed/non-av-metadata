#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Model import Assets
# from Model import Instantiations
from Model import CAPS_node

class AssetPart(CAPS_node):
    def __init__(self):
        super(AssetPart, self).__init__()
        self.__instantiations = None
        """@AttributeType []
        List of Instantiations Objects"""
        self.unnamed_Assets_ = None
        # @AssociationType Model.Assets
        self.unnamed_Instantiations_ = None
        # @AssociationType Model.Instantiations
        # @AssociationKind Composition

    def add_instantiations(self, new_instantiations):
        """@ParamType new_instantiations Model.Instantiations"""
        pass

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

