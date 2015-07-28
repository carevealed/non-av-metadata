#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Model.AssetPart
from Model import Element
import Model.Instantiation
from Model import CAPS_node

class Instantiations(CAPS_node):
    def __init__(self):
        """
        _relationship (str):
        _instantiation (list):
        """
        self._relationship = None
        self._instantiation = []
        """@AttributeType OrderedDict"""
        """@AttributeType list
        list of Instantiation Objects"""


    def add_instantiation(self, new_instantiation):
        # """@ParamType new_instantiation Model.Instantiation"""
        """
        :param Instantiation new_instantiation:
        """
        assert(isinstance(new_instantiation, Element))
        self._instantiation.append(new_instantiation)
        pass

    def _make_xml(self):
        root = Element("Instantiation", attributes={"relationship":self.relationship})
        for instance in self._instantiation:
            root.add_child(instance)
        return root
        pass

    def _check_required(self):
        missing_fields = []
        missing_attributes = []
        if not self.relationship:
            missing_attributes.append("relationship")
        if not self._instantiation:
            missing_fields.append("instantiation")

        if len(missing_attributes) > 0:
            raise Exception("Missing required metadata attributes, '" + "', '".join(missing_attributes) + "'.")
        if len(missing_fields) > 0:
            raise Exception("Missing required metadata fields, '" + "', '".join(missing_fields) + "'.")


    def validate_attribute(self):
        pass

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        self._relationship = value