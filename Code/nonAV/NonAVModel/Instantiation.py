#!/usr/bin/python
# -*- coding: UTF-8 -*-
from NonAVModel import Element
from NonAVModel import Technical
from NonAVModel import Instantiations
from NonAVModel import CAPS_node

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
        self._fileSizeUnit = None
        self._checksum = None
        self._checksumType = None
        self._derivedFrom = None
        self._technical = None
        self._generation = None


        if fileName:
            self.fileName = fileName

        if md5:
            self.checksum = md5
        if generation:
            self.generation = generation

    def _make_xml(self):
        root = Element("Instantiation")

        root.add_child(Element(tag="fileName", data=self.fileName))
        root.add_child(Element(tag="fileSize", data=self.fileSize, attributes={"unit": self.fileSizeUnit}))
        root.add_child(Element(tag="checksum", data=self.checksum, attributes={"type": self.checksumType}))
        root.add_child(Element(tag="derivedFrom", data=self.derivedFrom))

        root.add_child(self.technical)

        root.add_attribute("generation", self.generation)

        return root

    def check_required_data(self):
        missing_attributes = []
        missing_fields = []
        if not self.generation:
            missing_attributes.append("generation")
        if not self.fileName:
            missing_fields.append("fileName")
        if not self.fileSize:
            missing_fields.append("fileSize")
        if not self.fileSizeUnit:
            missing_attributes.append("fileSize unit")
        if not self.checksum:
            missing_fields.append("checksum")
        if not self.checksumType:
            missing_attributes.append("checksum type")
        if not self.derivedFrom:
            missing_fields.append("derivedFrom")

        return self.error_report(missing_fields=missing_fields, missing_attributes=missing_attributes)
        # if len(missing_attributes) > 0:
        #     raise Exception("Missing required metadata attributes, '" + "', '".join(missing_attributes) + "'.")
        # if len(missing_fields) > 0:
        #     raise Exception("Missing required metadata fields, '" + "', '".join(missing_fields) + "'.")

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
    def fileSizeUnit(self):
        return self._fileSizeUnit

    @fileSizeUnit.setter
    def fileSizeUnit(self, value):
        self._fileSizeUnit = value


    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        self._checksum = value

    @property
    def derivedFrom(self):
        return self._derivedFrom

    @derivedFrom.setter
    def derivedFrom(self, value):
        self._derivedFrom = value

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
    def derivedFrom(self):
        return self._derivedFrom

    @derivedFrom.setter
    def derivedFrom(self, value):
        self._derivedFrom = value

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
