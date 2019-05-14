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


class Prefetch(object):
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
        'computation_time': 'float',
        'created_at': 'datetime',
        'hit_count': 'int',
        'result_size_bytes': 'int',
        'touched_at': 'datetime',
        'ttl': 'int',
        'value': 'dict(str, str)',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'computation_time': 'computation_time',
        'created_at': 'created_at',
        'hit_count': 'hit_count',
        'result_size_bytes': 'result_size_bytes',
        'touched_at': 'touched_at',
        'ttl': 'ttl',
        'value': 'value',
        'can': 'can'
    }

    def __init__(self, computation_time=None, created_at=None, hit_count=None, result_size_bytes=None, touched_at=None, ttl=None, value=None, can=None):  # noqa: E501
        """Prefetch - a model defined in Swagger"""  # noqa: E501
        self._computation_time = None
        self._created_at = None
        self._hit_count = None
        self._result_size_bytes = None
        self._touched_at = None
        self._ttl = None
        self._value = None
        self._can = None
        self.discriminator = None
        if computation_time is not None:
            self.computation_time = computation_time
        if created_at is not None:
            self.created_at = created_at
        if hit_count is not None:
            self.hit_count = hit_count
        if result_size_bytes is not None:
            self.result_size_bytes = result_size_bytes
        if touched_at is not None:
            self.touched_at = touched_at
        if ttl is not None:
            self.ttl = ttl
        if value is not None:
            self.value = value
        if can is not None:
            self.can = can

    @property
    def computation_time(self):
        """Gets the computation_time of this Prefetch.  # noqa: E501

        Number of seconds it took to compute results for prefetch.  # noqa: E501

        :return: The computation_time of this Prefetch.  # noqa: E501
        :rtype: float
        """
        return self._computation_time

    @computation_time.setter
    def computation_time(self, computation_time):
        """Sets the computation_time of this Prefetch.

        Number of seconds it took to compute results for prefetch.  # noqa: E501

        :param computation_time: The computation_time of this Prefetch.  # noqa: E501
        :type: float
        """

        self._computation_time = computation_time

    @property
    def created_at(self):
        """Gets the created_at of this Prefetch.  # noqa: E501

        Time when prefetch was created.  # noqa: E501

        :return: The created_at of this Prefetch.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Prefetch.

        Time when prefetch was created.  # noqa: E501

        :param created_at: The created_at of this Prefetch.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def hit_count(self):
        """Gets the hit_count of this Prefetch.  # noqa: E501

        Number of times prefetch has been accessed.  # noqa: E501

        :return: The hit_count of this Prefetch.  # noqa: E501
        :rtype: int
        """
        return self._hit_count

    @hit_count.setter
    def hit_count(self, hit_count):
        """Sets the hit_count of this Prefetch.

        Number of times prefetch has been accessed.  # noqa: E501

        :param hit_count: The hit_count of this Prefetch.  # noqa: E501
        :type: int
        """

        self._hit_count = hit_count

    @property
    def result_size_bytes(self):
        """Gets the result_size_bytes of this Prefetch.  # noqa: E501

        Size of result.  # noqa: E501

        :return: The result_size_bytes of this Prefetch.  # noqa: E501
        :rtype: int
        """
        return self._result_size_bytes

    @result_size_bytes.setter
    def result_size_bytes(self, result_size_bytes):
        """Sets the result_size_bytes of this Prefetch.

        Size of result.  # noqa: E501

        :param result_size_bytes: The result_size_bytes of this Prefetch.  # noqa: E501
        :type: int
        """

        self._result_size_bytes = result_size_bytes

    @property
    def touched_at(self):
        """Gets the touched_at of this Prefetch.  # noqa: E501

        Time when prefetch was last accessed.  # noqa: E501

        :return: The touched_at of this Prefetch.  # noqa: E501
        :rtype: datetime
        """
        return self._touched_at

    @touched_at.setter
    def touched_at(self, touched_at):
        """Sets the touched_at of this Prefetch.

        Time when prefetch was last accessed.  # noqa: E501

        :param touched_at: The touched_at of this Prefetch.  # noqa: E501
        :type: datetime
        """

        self._touched_at = touched_at

    @property
    def ttl(self):
        """Gets the ttl of this Prefetch.  # noqa: E501

        Number of seconds prefetch will live for.  # noqa: E501

        :return: The ttl of this Prefetch.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Prefetch.

        Number of seconds prefetch will live for.  # noqa: E501

        :param ttl: The ttl of this Prefetch.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def value(self):
        """Gets the value of this Prefetch.  # noqa: E501

        Data associated with the queries stored by prefetching the data  # noqa: E501

        :return: The value of this Prefetch.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Prefetch.

        Data associated with the queries stored by prefetching the data  # noqa: E501

        :param value: The value of this Prefetch.  # noqa: E501
        :type: dict(str, str)
        """

        self._value = value

    @property
    def can(self):
        """Gets the can of this Prefetch.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this Prefetch.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this Prefetch.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this Prefetch.  # noqa: E501
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
        if issubclass(Prefetch, dict):
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
        if not isinstance(other, Prefetch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
