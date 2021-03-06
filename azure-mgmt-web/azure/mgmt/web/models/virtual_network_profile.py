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


class VirtualNetworkProfile(Model):
    """Specification for using a Virtual Network.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource id of the Virtual Network.
    :type id: str
    :ivar name: Name of the Virtual Network (read-only).
    :vartype name: str
    :ivar type: Resource type of the Virtual Network (read-only).
    :vartype type: str
    :param subnet: Subnet within the Virtual Network.
    :type subnet: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'subnet': {'key': 'subnet', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkProfile, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = None
        self.type = None
        self.subnet = kwargs.get('subnet', None)
