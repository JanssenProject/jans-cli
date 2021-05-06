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

class BulkOperation(object):
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
        'method': 'str',
        'bulk_id': 'str',
        'path': 'str',
        'data': 'object',
        'location': 'str',
        'response': 'object',
        'status': 'str'
    }

    attribute_map = {
        'method': 'method',
        'bulk_id': 'bulkId',
        'path': 'path',
        'data': 'data',
        'location': 'location',
        'response': 'response',
        'status': 'status'
    }

    def __init__(self, method=None, bulk_id=None, path=None, data=None, location=None, response=None, status=None):  # noqa: E501
        """BulkOperation - a model defined in Swagger"""  # noqa: E501
        self._method = None
        self._bulk_id = None
        self._path = None
        self._data = None
        self._location = None
        self._response = None
        self._status = None
        self.discriminator = None
        if method is not None:
            self.method = method
        if bulk_id is not None:
            self.bulk_id = bulk_id
        if path is not None:
            self.path = path
        if data is not None:
            self.data = data
        if location is not None:
            self.location = location
        if response is not None:
            self.response = response
        if status is not None:
            self.status = status

    @property
    def method(self):
        """Gets the method of this BulkOperation.  # noqa: E501


        :return: The method of this BulkOperation.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this BulkOperation.


        :param method: The method of this BulkOperation.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def bulk_id(self):
        """Gets the bulk_id of this BulkOperation.  # noqa: E501

        Used to bind the id generated for a created resource (via POST) to a named variable for later reuse   # noqa: E501

        :return: The bulk_id of this BulkOperation.  # noqa: E501
        :rtype: str
        """
        return self._bulk_id

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        """Sets the bulk_id of this BulkOperation.

        Used to bind the id generated for a created resource (via POST) to a named variable for later reuse   # noqa: E501

        :param bulk_id: The bulk_id of this BulkOperation.  # noqa: E501
        :type: str
        """

        self._bulk_id = bulk_id

    @property
    def path(self):
        """Gets the path of this BulkOperation.  # noqa: E501

        Path of the endpoint the operation uses relative to the server root, eg. /Users  # noqa: E501

        :return: The path of this BulkOperation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BulkOperation.

        Path of the endpoint the operation uses relative to the server root, eg. /Users  # noqa: E501

        :param path: The path of this BulkOperation.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def data(self):
        """Gets the data of this BulkOperation.  # noqa: E501

        Payload associated to this operation  # noqa: E501

        :return: The data of this BulkOperation.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BulkOperation.

        Payload associated to this operation  # noqa: E501

        :param data: The data of this BulkOperation.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def location(self):
        """Gets the location of this BulkOperation.  # noqa: E501

        Used in responses of POST operations  # noqa: E501

        :return: The location of this BulkOperation.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BulkOperation.

        Used in responses of POST operations  # noqa: E501

        :param location: The location of this BulkOperation.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def response(self):
        """Gets the response of this BulkOperation.  # noqa: E501


        :return: The response of this BulkOperation.  # noqa: E501
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this BulkOperation.


        :param response: The response of this BulkOperation.  # noqa: E501
        :type: object
        """

        self._response = response

    @property
    def status(self):
        """Gets the status of this BulkOperation.  # noqa: E501


        :return: The status of this BulkOperation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkOperation.


        :param status: The status of this BulkOperation.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(BulkOperation, dict):
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
        if not isinstance(other, BulkOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other