#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
import Model.AssetPart
# from Model import DescriptionDocument
from Model import CAPS_node

class Assets(CAPS_node):
    def __init__(self, object_id = None, project_id = None, physical_location = None, color = None, total_parts = None, additional_description = None):
        """@ParamType object_id str
        Unique object identifier to be supplied by the California Preservation Service.
        @ParamType project_id str
        @ParamType physical_location str
        Name of owning institution.
        @ParamType color str
        The color element describes whether the physical object made up of content that is black and white, color, or a mixture
        @ParamType total_parts str
        Describes the object's total number of parts. For example, "1 page" or "3 pages of 3."
        @ParamType additional_description str"""
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
        """@AttributeType Model.AssetPart"""
        self.unnamed_DescriptionDocument_ = None
        # @AssociationType Model.DescriptionDocument
        self.unnamed_Element_ = None
        # @AssociationType Model.Element
        self.unnamed_AssetPart_ = None
        # @AssociationType Model.AssetPart
        # @AssociationKind Composition

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

