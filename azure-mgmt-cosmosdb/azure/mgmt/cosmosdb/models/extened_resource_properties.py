# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExtenedResourceProperties(Model):
    """The system generated resource properties associated with SQL databases and
    SQL containers.

    :param _rid: A system generated property. A unique identifier.
    :type _rid: str
    :param _ts: A system generated property that denotes the last updated
     timestamp of the resource.
    :type _ts: object
    :param _self: A system generated property. It is the unique addressable
     URI for the resource.
    :type _self: str
    :param _etag: A system generated property representing the resource etag
     required for optimistic concurrency control.
    :type _etag: str
    """

    _attribute_map = {
        '_rid': {'key': '_rid', 'type': 'str'},
        '_ts': {'key': '_ts', 'type': 'object'},
        '_self': {'key': '_self', 'type': 'str'},
        '_etag': {'key': '_etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExtenedResourceProperties, self).__init__(**kwargs)
        self._rid = kwargs.get('_rid', None)
        self._ts = kwargs.get('_ts', None)
        self._self = kwargs.get('_self', None)
        self._etag = kwargs.get('_etag', None)
