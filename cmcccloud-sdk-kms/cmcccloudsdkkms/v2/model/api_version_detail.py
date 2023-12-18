# coding: utf-8

import six

from cmcccloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiVersionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'links': 'list[ApiLink]',
        'version': 'str',
        'status': 'str',
        'updated': 'str',
        'min_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'version': 'version',
        'status': 'status',
        'updated': 'updated',
        'min_version': 'min_version'
    }

    def __init__(self, id=None, links=None, version=None, status=None, updated=None, min_version=None):
        """ApiVersionDetail

        The model defined in cmcccloud sdk

        :param id: The param of the ApiVersionDetail
        :type id: str
        :param links: The param of the ApiVersionDetail
        :type links: list[:class:`cmcccloudsdkkms.v2.ApiLink`]
        :param version: The param of the ApiVersionDetail
        :type version: str
        :param status: The param of the ApiVersionDetail
        :type status: str
        :param updated: The param of the ApiVersionDetail
        :type updated: str
        :param min_version: The param of the ApiVersionDetail
        :type min_version: str
        """
        
        

        self._id = None
        self._links = None
        self._version = None
        self._status = None
        self._updated = None
        self._min_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated
        if min_version is not None:
            self.min_version = min_version

    @property
    def id(self):
        """Gets the id of this ApiVersionDetail.

        :return: The id of this ApiVersionDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiVersionDetail.

        :param id: The id of this ApiVersionDetail.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this ApiVersionDetail.

        :return: The links of this ApiVersionDetail.
        :rtype: list[:class:`cmcccloudsdkkms.v2.ApiLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiVersionDetail.

        :param links: The links of this ApiVersionDetail.
        :type links: list[:class:`cmcccloudsdkkms.v2.ApiLink`]
        """
        self._links = links

    @property
    def version(self):
        """Gets the version of this ApiVersionDetail.

        :return: The version of this ApiVersionDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiVersionDetail.

        :param version: The version of this ApiVersionDetail.
        :type version: str
        """
        self._version = version

    @property
    def status(self):
        """Gets the status of this ApiVersionDetail.

        :return: The status of this ApiVersionDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiVersionDetail.

        :param status: The status of this ApiVersionDetail.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ApiVersionDetail.

        :return: The updated of this ApiVersionDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ApiVersionDetail.

        :param updated: The updated of this ApiVersionDetail.
        :type updated: str
        """
        self._updated = updated

    @property
    def min_version(self):
        """Gets the min_version of this ApiVersionDetail.

        :return: The min_version of this ApiVersionDetail.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this ApiVersionDetail.

        :param min_version: The min_version of this ApiVersionDetail.
        :type min_version: str
        """
        self._min_version = min_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiVersionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
