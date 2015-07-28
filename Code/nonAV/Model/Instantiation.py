#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
from Model import Technical
from Model import Instantiations
from Model import CAPS_node

class Instantiation(CAPS_node):
    def __init__(self, fileName = None, md5 = None):
        """@ParamType fileName str
        @ParamType md5 str"""
        self.__fileName = None
        """@AttributeType Model.Element
        Name of the digital file with the file extension."""
        self.__fileSize = None
        """@AttributeType Model.Element
        The size of the digital file as a decimal or a whole number only. Qualified by a file size unit attribute"""
        self.__checksum = None
        """@AttributeType Model.Element
        Contains the hash value of a checksum verification algorithm. Qualified by a type attribute."""
        self.__deritiveFrom = None
        """@AttributeType Model.Element
        Refers to the source of instantiation. This will be designated by Physical Object for preservation master(s). For the access file(s), this will specify the file name it was derived from."""
        self.__technical = None
        """@AttributeType Model.Technical"""
        self.__attributes = None
        """@AttributeType OrderedDict"""
        self.unnamed_Instantiations_ = None
        # @AssociationType Model.Instantiations
        self.unnamed_Element_ = None
        # @AssociationType Model.Element
        self.unnamed_Technical_ = None
        # @AssociationType Model.Technical
        # @AssociationKind Composition

    def __make_xml(self):
        pass

    def validate_attribute(self):
        pass

