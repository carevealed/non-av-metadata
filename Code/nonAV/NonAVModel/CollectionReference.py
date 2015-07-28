#!/usr/bin/python
# -*- coding: UTF-8 -*-
import NonAVModel.DescriptionDocument
from NonAVModel import CAPS_node
from  NonAVModel import Element

class CollectionReference(CAPS_node):
    def __init__(self, collectionSource=None, projectSource=None):
        super(CollectionReference, self).__init__()
        self._descriptionDocument = NonAVModel.DescriptionDocument()
        self._collectionSource = None
        self._projectSource = None

        if collectionSource:
            self.collectionSource = collectionSource
        if projectSource:
            self.projectSource = projectSource

    def _make_xml(self):
        root = Element(tag="CollectionReference")
        root.add_attribute("collectionSource", self.collectionSource)
        root.add_attribute("projectSource", self.projectSource)
        root.add_attribute("xmlns", "http://calpreservation.org/projects/audiovisual-preservation/dcscheme.html")
        root.add_attribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.add_attribute("xsi:schemaLocation", "http://calpreservation.org/projects/audiovisual-preservation/dcscheme.html http://calpreservation.org/projects/audiovisual-preservation/CAVPPDC.xsd")

        root.add_child(self.descriptionDocument)
        return root

    def _check_required(self):
        missing_attributes = []
        missing_fields = []

        if not self.collectionSource:
            missing_attributes.append("collectionSource")
        if not self.projectSource:
            missing_attributes.append("projectSource")

        if not self.descriptionDocument:
            missing_fields.append("DescriptionDocument")

        if len(missing_attributes) > 0:
            raise Exception("Missing required metadata attributes, '" + "', '".join(missing_attributes) + "'.")
        if len(missing_fields) > 0:
            raise Exception("Missing required metadata fields, '" + "', '".join(missing_fields) + "'.")
        pass

    def validate_attribute(self):
        pass

    @property
    def descriptionDocument(self):
        return self._descriptionDocument

    @descriptionDocument.setter
    def descriptionDocument(self, value):
        self._descriptionDocument = value

    @property
    def collectionSource(self):
        return self._collectionSource

    @collectionSource.setter
    def collectionSource(self, value):
        self._collectionSource = value

    @property
    def projectSource(self):
        return self._projectSource

    @projectSource.setter
    def projectSource(self, value):
        self._projectSource = value