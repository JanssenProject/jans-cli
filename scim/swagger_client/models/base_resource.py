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

class BaseResource(object):
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
        'id': 'str',
        'meta': 'Meta'
    }

    attribute_map = {
        'schemas': 'schemas',
        'id': 'id',
        'meta': 'meta'
    }

    def __init__(self, schemas=None, id=None, meta=None):  # noqa: E501
        """BaseResource - a model defined in Swagger"""  # noqa: E501
        self._schemas = None
        self._id = None
        self._meta = None
        self.discriminator = None
        if schemas is not None:
            self.schemas = schemas
        if id is not None:
            self.id = id
        if meta is not None:
            self.meta = meta

    @property
    def schemas(self):
        """Gets the schemas of this BaseResource.  # noqa: E501

        URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure  # noqa: E501

        :return: The schemas of this BaseResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this BaseResource.

        URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure  # noqa: E501

        :param schemas: The schemas of this BaseResource.  # noqa: E501
        :type: list[str]
        """

        self._schemas = schemas

    @property
    def id(self):
        """Gets the id of this BaseResource.  # noqa: E501

        A unique identifier for a SCIM resource. See section 3.1 of RFC 7643  # noqa: E501

        :return: The id of this BaseResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseResource.

        A unique identifier for a SCIM resource. See section 3.1 of RFC 7643  # noqa: E501

        :param id: The id of this BaseResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def meta(self):
        """Gets the meta of this BaseResource.  # noqa: E501


        :return: The meta of this BaseResource.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this BaseResource.


        :param meta: The meta of this BaseResource.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

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
        if issubclass(BaseResource, dict):
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
        if not isinstance(other, BaseResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
