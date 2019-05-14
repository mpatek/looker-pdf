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


class ContentMetaGroupUser(object):
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
        'id': 'str',
        'content_metadata_id': 'str',
        'permission_type': 'str',
        'group_id': 'int',
        'user_id': 'int',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'content_metadata_id': 'content_metadata_id',
        'permission_type': 'permission_type',
        'group_id': 'group_id',
        'user_id': 'user_id',
        'can': 'can'
    }

    def __init__(self, id=None, content_metadata_id=None, permission_type=None, group_id=None, user_id=None, can=None):  # noqa: E501
        """ContentMetaGroupUser - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._content_metadata_id = None
        self._permission_type = None
        self._group_id = None
        self._user_id = None
        self._can = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if content_metadata_id is not None:
            self.content_metadata_id = content_metadata_id
        if permission_type is not None:
            self.permission_type = permission_type
        if group_id is not None:
            self.group_id = group_id
        if user_id is not None:
            self.user_id = user_id
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this ContentMetaGroupUser.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this ContentMetaGroupUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentMetaGroupUser.

        Unique Id  # noqa: E501

        :param id: The id of this ContentMetaGroupUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def content_metadata_id(self):
        """Gets the content_metadata_id of this ContentMetaGroupUser.  # noqa: E501

        Id of associated Content Metadata  # noqa: E501

        :return: The content_metadata_id of this ContentMetaGroupUser.  # noqa: E501
        :rtype: str
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """Sets the content_metadata_id of this ContentMetaGroupUser.

        Id of associated Content Metadata  # noqa: E501

        :param content_metadata_id: The content_metadata_id of this ContentMetaGroupUser.  # noqa: E501
        :type: str
        """

        self._content_metadata_id = content_metadata_id

    @property
    def permission_type(self):
        """Gets the permission_type of this ContentMetaGroupUser.  # noqa: E501

        Type of permission: \"view\" or \"edit\"  # noqa: E501

        :return: The permission_type of this ContentMetaGroupUser.  # noqa: E501
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this ContentMetaGroupUser.

        Type of permission: \"view\" or \"edit\"  # noqa: E501

        :param permission_type: The permission_type of this ContentMetaGroupUser.  # noqa: E501
        :type: str
        """

        self._permission_type = permission_type

    @property
    def group_id(self):
        """Gets the group_id of this ContentMetaGroupUser.  # noqa: E501

        ID of associated group  # noqa: E501

        :return: The group_id of this ContentMetaGroupUser.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ContentMetaGroupUser.

        ID of associated group  # noqa: E501

        :param group_id: The group_id of this ContentMetaGroupUser.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def user_id(self):
        """Gets the user_id of this ContentMetaGroupUser.  # noqa: E501

        ID of associated user  # noqa: E501

        :return: The user_id of this ContentMetaGroupUser.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ContentMetaGroupUser.

        ID of associated user  # noqa: E501

        :param user_id: The user_id of this ContentMetaGroupUser.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def can(self):
        """Gets the can of this ContentMetaGroupUser.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this ContentMetaGroupUser.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this ContentMetaGroupUser.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this ContentMetaGroupUser.  # noqa: E501
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
        if issubclass(ContentMetaGroupUser, dict):
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
        if not isinstance(other, ContentMetaGroupUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
