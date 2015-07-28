#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Model import Assets
# from Model import Instantiations
from Model import CAPS_node
from Model import Element


class AssetPart(CAPS_node):
    def __init__(self, instantiations=None):
        """
        :param Instantations instantiations:
        self._instantiations (list)
        """
        super(AssetPart, self).__init__()
        self._instantiations = None

        if instantiations:
            self.instantiations = instantiations

    def _make_xml(self):
        root = Element("AssetPart")
        root.add_child(self.instantiations)
        return root

    def _check_required(self):
        missing_fields = []
        if not self.instantiations:
            missing_fields.append("instantiations")

        if len(missing_fields) > 0:
            raise Exception("Missing required metadata fields, '" + "', '".join(missing_fields) + "'.")
        pass

    def validate_attribute(self):
        pass

    @property
    def instantiations(self):
        return self._instantiations

    @instantiations.setter
    def instantiations(self, value):
        self._instantiations = value
