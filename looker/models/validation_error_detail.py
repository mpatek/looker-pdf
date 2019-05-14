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


class ValidationErrorDetail(object):
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
        'field': 'str',
        'code': 'str',
        'message': 'str',
        'documentation_url': 'str'
    }

    attribute_map = {
        'field': 'field',
        'code': 'code',
        'message': 'message',
        'documentation_url': 'documentation_url'
    }

    def __init__(self, field=None, code=None, message=None, documentation_url=None):  # noqa: E501
        """ValidationErrorDetail - a model defined in Swagger"""  # noqa: E501
        self._field = None
        self._code = None
        self._message = None
        self._documentation_url = None
        self.discriminator = None
        if field is not None:
            self.field = field
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        self.documentation_url = documentation_url

    @property
    def field(self):
        """Gets the field of this ValidationErrorDetail.  # noqa: E501

        Field with error  # noqa: E501

        :return: The field of this ValidationErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ValidationErrorDetail.

        Field with error  # noqa: E501

        :param field: The field of this ValidationErrorDetail.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def code(self):
        """Gets the code of this ValidationErrorDetail.  # noqa: E501

        Error code  # noqa: E501

        :return: The code of this ValidationErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ValidationErrorDetail.

        Error code  # noqa: E501

        :param code: The code of this ValidationErrorDetail.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this ValidationErrorDetail.  # noqa: E501

        Error info message  # noqa: E501

        :return: The message of this ValidationErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationErrorDetail.

        Error info message  # noqa: E501

        :param message: The message of this ValidationErrorDetail.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def documentation_url(self):
        """Gets the documentation_url of this ValidationErrorDetail.  # noqa: E501

        Documentation link  # noqa: E501

        :return: The documentation_url of this ValidationErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this ValidationErrorDetail.

        Documentation link  # noqa: E501

        :param documentation_url: The documentation_url of this ValidationErrorDetail.  # noqa: E501
        :type: str
        """
        if documentation_url is None:
            raise ValueError("Invalid value for `documentation_url`, must not be `None`")  # noqa: E501

        self._documentation_url = documentation_url

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
        if issubclass(ValidationErrorDetail, dict):
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
        if not isinstance(other, ValidationErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
