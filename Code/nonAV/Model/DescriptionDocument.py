#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Model import DublinCore
import Model.Assets
from Model import CollectionReference
from Model import Element
from Model import CAPS_node

class DescriptionDocument(CAPS_node):
    def __init__(self):
        """

        :return:
        """
        super(DescriptionDocument, self).__init__()
        self._dublinCore = None
        self._assets = None

    def _make_xml(self):
        root = Element("DescriptionDocument")
        root.add_child(self.dublinCore)
        root.add_child(self.assets)
        return root

    def _check_required(self):
        missing_fields = []
        if not self.dublinCore:
            missing_fields.append("dublinCore")
        if not self.assets:
            missing_fields.append("assets")
        if len(missing_fields) > 0:
            raise Exception("Missing required metadata fields, '" + "', '".join(missing_fields) + "'.")
        pass

    def validate_attribute(self):
        pass

    @property
    def dublinCore(self):
        return self._dublinCore

    @dublinCore.setter
    def dublinCore(self, value):
        if not isinstance(value, Element):
            raise TypeError("Expected an Element type but received " + str(type(Element)))
        self._dublinCore = value

    @property
    def assets(self):
        return self._assets

    @assets.setter
    def assets(self, value):
        self._assets = value
