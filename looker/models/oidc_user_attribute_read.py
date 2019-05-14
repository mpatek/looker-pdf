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
from looker.models.user_attribute import UserAttribute  # noqa: F401,E501


class OIDCUserAttributeRead(object):
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
        'user_attributes': 'list[UserAttribute]'
    }

    attribute_map = {
        'name': 'name',
        'required': 'required',
        'user_attributes': 'user_attributes'
    }

    def __init__(self, name=None, required=None, user_attributes=None):  # noqa: E501
        """OIDCUserAttributeRead - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._required = None
        self._user_attributes = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if user_attributes is not None:
            self.user_attributes = user_attributes

    @property
    def name(self):
        """Gets the name of this OIDCUserAttributeRead.  # noqa: E501

        Name of User Attribute in OIDC  # noqa: E501

        :return: The name of this OIDCUserAttributeRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OIDCUserAttributeRead.

        Name of User Attribute in OIDC  # noqa: E501

        :param name: The name of this OIDCUserAttributeRead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this OIDCUserAttributeRead.  # noqa: E501

        Required to be in OIDC assertion for login to be allowed to succeed  # noqa: E501

        :return: The required of this OIDCUserAttributeRead.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this OIDCUserAttributeRead.

        Required to be in OIDC assertion for login to be allowed to succeed  # noqa: E501

        :param required: The required of this OIDCUserAttributeRead.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def user_attributes(self):
        """Gets the user_attributes of this OIDCUserAttributeRead.  # noqa: E501

        Looker User Attributes  # noqa: E501

        :return: The user_attributes of this OIDCUserAttributeRead.  # noqa: E501
        :rtype: list[UserAttribute]
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes):
        """Sets the user_attributes of this OIDCUserAttributeRead.

        Looker User Attributes  # noqa: E501

        :param user_attributes: The user_attributes of this OIDCUserAttributeRead.  # noqa: E501
        :type: list[UserAttribute]
        """

        self._user_attributes = user_attributes

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
        if issubclass(OIDCUserAttributeRead, dict):
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
        if not isinstance(other, OIDCUserAttributeRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
