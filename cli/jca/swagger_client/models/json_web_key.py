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

class JsonWebKey(object):
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
        'kid': 'str',
        'kty': 'str',
        'use': 'str',
        'alg': 'str',
        'crv': 'str',
        'exp': 'int',
        'x5c': 'list[str]',
        'n': 'str',
        'e': 'str',
        'x': 'str',
        'y': 'str'
    }

    attribute_map = {
        'kid': 'kid',
        'kty': 'kty',
        'use': 'use',
        'alg': 'alg',
        'crv': 'crv',
        'exp': 'exp',
        'x5c': 'x5c',
        'n': 'n',
        'e': 'e',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, kid=None, kty=None, use=None, alg=None, crv=None, exp=None, x5c=None, n=None, e=None, x=None, y=None):  # noqa: E501
        """JsonWebKey - a model defined in Swagger"""  # noqa: E501
        self._kid = None
        self._kty = None
        self._use = None
        self._alg = None
        self._crv = None
        self._exp = None
        self._x5c = None
        self._n = None
        self._e = None
        self._x = None
        self._y = None
        self.discriminator = None
        self.kid = kid
        self.kty = kty
        self.use = use
        self.alg = alg
        if crv is not None:
            self.crv = crv
        self.exp = exp
        if x5c is not None:
            self.x5c = x5c
        if n is not None:
            self.n = n
        if e is not None:
            self.e = e
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def kid(self):
        """Gets the kid of this JsonWebKey.  # noqa: E501

        The unique identifier for the key.  # noqa: E501

        :return: The kid of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this JsonWebKey.

        The unique identifier for the key.  # noqa: E501

        :param kid: The kid of this JsonWebKey.  # noqa: E501
        :type: str
        """
        if kid is None:
            raise ValueError("Invalid value for `kid`, must not be `None`")  # noqa: E501

        self._kid = kid

    @property
    def kty(self):
        """Gets the kty of this JsonWebKey.  # noqa: E501

        The family of cryptographic algorithms used with the key.  # noqa: E501

        :return: The kty of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this JsonWebKey.

        The family of cryptographic algorithms used with the key.  # noqa: E501

        :param kty: The kty of this JsonWebKey.  # noqa: E501
        :type: str
        """
        if kty is None:
            raise ValueError("Invalid value for `kty`, must not be `None`")  # noqa: E501

        self._kty = kty

    @property
    def use(self):
        """Gets the use of this JsonWebKey.  # noqa: E501

        How the key was meant to be used; sig represents the signature.  # noqa: E501

        :return: The use of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this JsonWebKey.

        How the key was meant to be used; sig represents the signature.  # noqa: E501

        :param use: The use of this JsonWebKey.  # noqa: E501
        :type: str
        """
        if use is None:
            raise ValueError("Invalid value for `use`, must not be `None`")  # noqa: E501

        self._use = use

    @property
    def alg(self):
        """Gets the alg of this JsonWebKey.  # noqa: E501

        The specific cryptographic algorithm used with the key.  # noqa: E501

        :return: The alg of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this JsonWebKey.

        The specific cryptographic algorithm used with the key.  # noqa: E501

        :param alg: The alg of this JsonWebKey.  # noqa: E501
        :type: str
        """
        if alg is None:
            raise ValueError("Invalid value for `alg`, must not be `None`")  # noqa: E501

        self._alg = alg

    @property
    def crv(self):
        """Gets the crv of this JsonWebKey.  # noqa: E501

        The crv member identifies the cryptographic curve used with the key. Values defined by this specification are P-256, P-384 and P-521. Additional crv values MAY be used, provided they are understood by implementations using that Elliptic Curve key. The crv value is case sensitive.  # noqa: E501

        :return: The crv of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._crv

    @crv.setter
    def crv(self, crv):
        """Sets the crv of this JsonWebKey.

        The crv member identifies the cryptographic curve used with the key. Values defined by this specification are P-256, P-384 and P-521. Additional crv values MAY be used, provided they are understood by implementations using that Elliptic Curve key. The crv value is case sensitive.  # noqa: E501

        :param crv: The crv of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._crv = crv

    @property
    def exp(self):
        """Gets the exp of this JsonWebKey.  # noqa: E501

        Contains the token expiration timestamp  # noqa: E501

        :return: The exp of this JsonWebKey.  # noqa: E501
        :rtype: int
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """Sets the exp of this JsonWebKey.

        Contains the token expiration timestamp  # noqa: E501

        :param exp: The exp of this JsonWebKey.  # noqa: E501
        :type: int
        """
        if exp is None:
            raise ValueError("Invalid value for `exp`, must not be `None`")  # noqa: E501

        self._exp = exp

    @property
    def x5c(self):
        """Gets the x5c of this JsonWebKey.  # noqa: E501

        The x.509 certificate chain. The first entry in the array is the certificate to use for token verification; the other certificates can be used to verify this first certificate.  # noqa: E501

        :return: The x5c of this JsonWebKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._x5c

    @x5c.setter
    def x5c(self, x5c):
        """Sets the x5c of this JsonWebKey.

        The x.509 certificate chain. The first entry in the array is the certificate to use for token verification; the other certificates can be used to verify this first certificate.  # noqa: E501

        :param x5c: The x5c of this JsonWebKey.  # noqa: E501
        :type: list[str]
        """

        self._x5c = x5c

    @property
    def n(self):
        """Gets the n of this JsonWebKey.  # noqa: E501

        The modulus for the RSA public key.  # noqa: E501

        :return: The n of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this JsonWebKey.

        The modulus for the RSA public key.  # noqa: E501

        :param n: The n of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._n = n

    @property
    def e(self):
        """Gets the e of this JsonWebKey.  # noqa: E501

        The exponent for the RSA public key.  # noqa: E501

        :return: The e of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """Sets the e of this JsonWebKey.

        The exponent for the RSA public key.  # noqa: E501

        :param e: The e of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._e = e

    @property
    def x(self):
        """Gets the x of this JsonWebKey.  # noqa: E501

        The x member contains the x coordinate for the elliptic curve point. It is represented as the base64url encoding of the coordinate's big endian representation.  # noqa: E501

        :return: The x of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this JsonWebKey.

        The x member contains the x coordinate for the elliptic curve point. It is represented as the base64url encoding of the coordinate's big endian representation.  # noqa: E501

        :param x: The x of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this JsonWebKey.  # noqa: E501

        The y member contains the y coordinate for the elliptic curve point. It is represented as the base64url encoding of the coordinate's big endian representation.  # noqa: E501

        :return: The y of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this JsonWebKey.

        The y member contains the y coordinate for the elliptic curve point. It is represented as the base64url encoding of the coordinate's big endian representation.  # noqa: E501

        :param y: The y of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._y = y

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
        if issubclass(JsonWebKey, dict):
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
        if not isinstance(other, JsonWebKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
