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

class StatResponseItem(object):
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
        'month': 'int',
        'monthly_active_users': 'int',
        'token_count_per_granttype': 'dict(str, TokenMapObject)'
    }

    attribute_map = {
        'month': 'month',
        'monthly_active_users': 'monthly_active_users',
        'token_count_per_granttype': 'token_count_per_granttype'
    }

    def __init__(self, month=None, monthly_active_users=0, token_count_per_granttype=None):  # noqa: E501
        """StatResponseItem - a model defined in Swagger"""  # noqa: E501
        self._month = None
        self._monthly_active_users = None
        self._token_count_per_granttype = None
        self.discriminator = None
        if month is not None:
            self.month = month
        if monthly_active_users is not None:
            self.monthly_active_users = monthly_active_users
        if token_count_per_granttype is not None:
            self.token_count_per_granttype = token_count_per_granttype

    @property
    def month(self):
        """Gets the month of this StatResponseItem.  # noqa: E501


        :return: The month of this StatResponseItem.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this StatResponseItem.


        :param month: The month of this StatResponseItem.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def monthly_active_users(self):
        """Gets the monthly_active_users of this StatResponseItem.  # noqa: E501

        Number of active users  # noqa: E501

        :return: The monthly_active_users of this StatResponseItem.  # noqa: E501
        :rtype: int
        """
        return self._monthly_active_users

    @monthly_active_users.setter
    def monthly_active_users(self, monthly_active_users):
        """Sets the monthly_active_users of this StatResponseItem.

        Number of active users  # noqa: E501

        :param monthly_active_users: The monthly_active_users of this StatResponseItem.  # noqa: E501
        :type: int
        """

        self._monthly_active_users = monthly_active_users

    @property
    def token_count_per_granttype(self):
        """Gets the token_count_per_granttype of this StatResponseItem.  # noqa: E501


        :return: The token_count_per_granttype of this StatResponseItem.  # noqa: E501
        :rtype: dict(str, TokenMapObject)
        """
        return self._token_count_per_granttype

    @token_count_per_granttype.setter
    def token_count_per_granttype(self, token_count_per_granttype):
        """Sets the token_count_per_granttype of this StatResponseItem.


        :param token_count_per_granttype: The token_count_per_granttype of this StatResponseItem.  # noqa: E501
        :type: dict(str, TokenMapObject)
        """

        self._token_count_per_granttype = token_count_per_granttype

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
        if issubclass(StatResponseItem, dict):
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
        if not isinstance(other, StatResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
