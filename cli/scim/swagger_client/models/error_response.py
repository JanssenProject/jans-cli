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

class ErrorResponse(object):
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
        'status': 'str',
        'scim_type': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'schemas': 'schemas',
        'status': 'status',
        'scim_type': 'scimType',
        'detail': 'detail'
    }

    def __init__(self, schemas=None, status=None, scim_type=None, detail=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._schemas = None
        self._status = None
        self._scim_type = None
        self._detail = None
        self.discriminator = None
        if schemas is not None:
            self.schemas = schemas
        self.status = status
        if scim_type is not None:
            self.scim_type = scim_type
        if detail is not None:
            self.detail = detail

    @property
    def schemas(self):
        """Gets the schemas of this ErrorResponse.  # noqa: E501


        :return: The schemas of this ErrorResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this ErrorResponse.


        :param schemas: The schemas of this ErrorResponse.  # noqa: E501
        :type: list[str]
        """

        self._schemas = schemas

    @property
    def status(self):
        """Gets the status of this ErrorResponse.  # noqa: E501

        HTTP status code as string  # noqa: E501

        :return: The status of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ErrorResponse.

        HTTP status code as string  # noqa: E501

        :param status: The status of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def scim_type(self):
        """Gets the scim_type of this ErrorResponse.  # noqa: E501

        A detail error keyword. See table 9 of RFC 7644  # noqa: E501

        :return: The scim_type of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._scim_type

    @scim_type.setter
    def scim_type(self, scim_type):
        """Sets the scim_type of this ErrorResponse.

        A detail error keyword. See table 9 of RFC 7644  # noqa: E501

        :param scim_type: The scim_type of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._scim_type = scim_type

    @property
    def detail(self):
        """Gets the detail of this ErrorResponse.  # noqa: E501

        A detailed human-readable message of the error  # noqa: E501

        :return: The detail of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorResponse.

        A detailed human-readable message of the error  # noqa: E501

        :param detail: The detail of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._detail = detail

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
        if issubclass(ErrorResponse, dict):
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
        if not isinstance(other, ErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
