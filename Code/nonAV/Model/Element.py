#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Element(object):
    def __init__(self):
    # def __init__(self, *args, **kwargs):
    #     if kwargs:
    #         print("KWARGS")
    #     if args:
    #         print("ARGS")
        print("dfdf")
        self.__tag = None
        """@AttributeType string"""
        self.__data = None
        """@AttributeType string"""
        self.__attributes = None
        """@AttributeType OrderedDict
        Contains all the attributes for a given XML element."""


    def get_attributes(self):
        """@ReturnType OrderedDict"""
        pass

    def add_attribute(self, key, value):
        """@ParamType key string
        The name part of the name/value pair
        @ParamType value string
        The value part of the name/value pair.
        @ReturnType void"""
        pass

    def delete_attribute(self, key):
        """@ParamType key string
        @ReturnType void"""
        pass

    def __repr__(self):
        """Returns the XML element as an etree element.
        @ReturnType etElement"""
        pass

    def get_data(self):
        """@ReturnType string"""
        pass

