#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import Element
from Model import Technical
from Model import Instantiations
from Model import CAPS_node

class Instantiation(CAPS_node):
    def __init__(self, fileName=None, md5=None, generation=None):
        """
        :param str fileName":   Specifies the name of the given file
        :param str md5":        Checksum hash in md5 format

        _fileName (str):        Specifies the name of the given file
        _fileSize (str):        The size of the digital file as a decimal or a whole number only. Qualified by a file size unit attribute
        _checksum (str):
        _deritiveFrom (str):    Refers to the source of instantiation. This will be designated by Physical Object for preservation master(s). For the access file(s), this will specify the file name it was derived from.

        _technical (Technical):
        _attributes (OrderedDict):

        """

        super(Instantiation, self).__init__()
        self._fileName = None
        self._fileSize = None
        self._checksum = None
        self._checksumType = None
        self._deritiveFrom = None
        self._technical = None
        self._generation = None


        if fileName:
            self.fileName = fileName

        if md5:
            self.checksum = md5
        if generation:
            self.generation = generation

    def _make_xml(self):
        root = etElement(tag="Instantiation")
        if self.fileName:
            root.add_child(Element(tag="fileName", data=self.fileName))
        if self.fileSize:
            root.add_child(Element(tag="fileSize", data=self.fileSize))
        if self.checksum:
            if self.checksumType:
                root.add_child(Element(tag="checksum", data=self.checksum, attributes={"type": self.checksumType}))
            else:
                raise Exception("checksum element is used but is missing a type attribute.")
        if self.deritiveFrom:
            root.add_child(Element(tag="deritiveFrom", data=self.deritiveFrom))
        if self.technical:
            root.add_child(Element(tag="Technical", data=self.technical))
        if self.generation:
            root.add_attribute("generation", self.generation)
        return root.xml

    def _check_required(self):
        pass

    def validate_attribute(self):
        pass

    @property
    def fileName(self):
        return self._fileName

    @fileName.setter
    def fileName(self, value):
        self._fileName = value

    @property
    def fileSize(self):
        return self._fileSize

    @fileSize.setter
    def fileSize(self, value):
        self._fileSize = value

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        self._checksum = value

    @property
    def deritiveFrom(self):
        return self._deritiveFrom

    @deritiveFrom.setter
    def deritiveFrom(self, value):
        self._deritiveFrom = value

    @property
    def technical(self):
        return self._technical

    @technical.setter
    def technical(self, value):
        self._technical = value

    @property
    def attributes(self):
        return self._generation

    @attributes.setter
    def attributes(self, value):
        self._generation = value

    @property
    def fileName(self):
        return self._fileName

    @fileName.setter
    def fileName(self, value):
        self._fileName = value

    @property
    def fileSize(self):
        return self._fileSize

    @fileSize.setter
    def fileSize(self, value):
        self._fileSize = value

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        self._checksum = value
    @property
    def checksumType(self):
        return self._checksumType

    @checksumType.setter
    def checksumType(self, value):
        self._checksumType = value

    @property
    def deritiveFrom(self):
        return self._deritiveFrom

    @deritiveFrom.setter
    def deritiveFrom(self, value):
        self._deritiveFrom = value

    @property
    def technical(self):
        return self._technical

    @technical.setter
    def technical(self, value):
        self._technical = value

    @property
    def generation(self):
        return self._generation

    @generation.setter
    def generation(self, value):
        self._generation = value
