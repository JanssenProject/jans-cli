# coding: utf-8

"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResourceTypeSchemaExtensions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'schema': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'schema': 'schema',
        'required': 'required'
    }

    def __init__(self, schema=None, required=None):  # noqa: E501
        """ResourceTypeSchemaExtensions - a model defined in Swagger"""  # noqa: E501
        self._schema = None
        self._required = None
        self.discriminator = None
        if schema is not None:
            self.schema = schema
        if required is not None:
            self.required = required

    @property
    def schema(self):
        """Gets the schema of this ResourceTypeSchemaExtensions.  # noqa: E501


        :return: The schema of this ResourceTypeSchemaExtensions.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ResourceTypeSchemaExtensions.


        :param schema: The schema of this ResourceTypeSchemaExtensions.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def required(self):
        """Gets the required of this ResourceTypeSchemaExtensions.  # noqa: E501


        :return: The required of this ResourceTypeSchemaExtensions.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ResourceTypeSchemaExtensions.


        :param required: The required of this ResourceTypeSchemaExtensions.  # noqa: E501
        :type: bool
        """

        self._required = required

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ResourceTypeSchemaExtensions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceTypeSchemaExtensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
