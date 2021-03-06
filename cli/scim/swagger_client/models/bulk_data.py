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

class BulkData(object):
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
        'schemas': 'list[str]',
        'operations': 'list[BulkOperation]'
    }

    attribute_map = {
        'schemas': 'schemas',
        'operations': 'Operations'
    }

    def __init__(self, schemas=None, operations=None):  # noqa: E501
        """BulkData - a model defined in Swagger"""  # noqa: E501
        self._schemas = None
        self._operations = None
        self.discriminator = None
        if schemas is not None:
            self.schemas = schemas
        if operations is not None:
            self.operations = operations

    @property
    def schemas(self):
        """Gets the schemas of this BulkData.  # noqa: E501


        :return: The schemas of this BulkData.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this BulkData.


        :param schemas: The schemas of this BulkData.  # noqa: E501
        :type: list[str]
        """

        self._schemas = schemas

    @property
    def operations(self):
        """Gets the operations of this BulkData.  # noqa: E501


        :return: The operations of this BulkData.  # noqa: E501
        :rtype: list[BulkOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this BulkData.


        :param operations: The operations of this BulkData.  # noqa: E501
        :type: list[BulkOperation]
        """

        self._operations = operations

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
        if issubclass(BulkData, dict):
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
        if not isinstance(other, BulkData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
