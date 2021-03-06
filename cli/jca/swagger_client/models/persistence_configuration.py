# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersistenceConfiguration(object):
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
        'persistence_type': 'str'
    }

    attribute_map = {
        'persistence_type': 'persistenceType'
    }

    def __init__(self, persistence_type=None):  # noqa: E501
        """PersistenceConfiguration - a model defined in Swagger"""  # noqa: E501
        self._persistence_type = None
        self.discriminator = None
        if persistence_type is not None:
            self.persistence_type = persistence_type

    @property
    def persistence_type(self):
        """Gets the persistence_type of this PersistenceConfiguration.  # noqa: E501

        Jans Auth Server persistence type configured.  # noqa: E501

        :return: The persistence_type of this PersistenceConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._persistence_type

    @persistence_type.setter
    def persistence_type(self, persistence_type):
        """Sets the persistence_type of this PersistenceConfiguration.

        Jans Auth Server persistence type configured.  # noqa: E501

        :param persistence_type: The persistence_type of this PersistenceConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["ldap", "couchbase", "sql", "spanner", "hybrid"]  # noqa: E501
        if persistence_type not in allowed_values:
            raise ValueError(
                "Invalid value for `persistence_type` ({0}), must be one of {1}"  # noqa: E501
                .format(persistence_type, allowed_values)
            )

        self._persistence_type = persistence_type

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
        if issubclass(PersistenceConfiguration, dict):
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
        if not isinstance(other, PersistenceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
