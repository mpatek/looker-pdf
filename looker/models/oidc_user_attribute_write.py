# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@looker.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class OIDCUserAttributeWrite(object):
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
        'name': 'str',
        'required': 'bool',
        'user_attribute_ids': 'list[int]',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'name': 'name',
        'required': 'required',
        'user_attribute_ids': 'user_attribute_ids',
        'can': 'can'
    }

    def __init__(self, name=None, required=None, user_attribute_ids=None, can=None):  # noqa: E501
        """OIDCUserAttributeWrite - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._required = None
        self._user_attribute_ids = None
        self._can = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if user_attribute_ids is not None:
            self.user_attribute_ids = user_attribute_ids
        if can is not None:
            self.can = can

    @property
    def name(self):
        """Gets the name of this OIDCUserAttributeWrite.  # noqa: E501

        Name of User Attribute in OIDC  # noqa: E501

        :return: The name of this OIDCUserAttributeWrite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OIDCUserAttributeWrite.

        Name of User Attribute in OIDC  # noqa: E501

        :param name: The name of this OIDCUserAttributeWrite.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this OIDCUserAttributeWrite.  # noqa: E501

        Required to be in OIDC assertion for login to be allowed to succeed  # noqa: E501

        :return: The required of this OIDCUserAttributeWrite.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this OIDCUserAttributeWrite.

        Required to be in OIDC assertion for login to be allowed to succeed  # noqa: E501

        :param required: The required of this OIDCUserAttributeWrite.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def user_attribute_ids(self):
        """Gets the user_attribute_ids of this OIDCUserAttributeWrite.  # noqa: E501

        Looker User Attribute Ids  # noqa: E501

        :return: The user_attribute_ids of this OIDCUserAttributeWrite.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_attribute_ids

    @user_attribute_ids.setter
    def user_attribute_ids(self, user_attribute_ids):
        """Sets the user_attribute_ids of this OIDCUserAttributeWrite.

        Looker User Attribute Ids  # noqa: E501

        :param user_attribute_ids: The user_attribute_ids of this OIDCUserAttributeWrite.  # noqa: E501
        :type: list[int]
        """

        self._user_attribute_ids = user_attribute_ids

    @property
    def can(self):
        """Gets the can of this OIDCUserAttributeWrite.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this OIDCUserAttributeWrite.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this OIDCUserAttributeWrite.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this OIDCUserAttributeWrite.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

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
        if issubclass(OIDCUserAttributeWrite, dict):
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
        if not isinstance(other, OIDCUserAttributeWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
