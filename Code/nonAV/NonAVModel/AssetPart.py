#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from Model import Assets
# from Model import Instantiations
from NonAVModel import CAPS_node
from NonAVModel import Element


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

    def check_required_data(self):
        missing_fields = []
        missing_attributes = []
        if not self.instantiations:
            missing_fields.append("instantiations")

        return self.error_report(missing_fields=missing_fields, missing_attributes=missing_attributes)


    def validate_attribute(self):
        pass

    @property
    def instantiations(self):
        return self._instantiations

    @instantiations.setter
    def instantiations(self, value):
        self._instantiations = value
