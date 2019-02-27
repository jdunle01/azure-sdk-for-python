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


class PrivateIPAddress(Model):
    """A private IP address bound to the availability group listener.

    :param ip_address: Private IP address bound to the availability group
     listener.
    :type ip_address: str
    :param subnet_resource_id: Subnet used to include private IP.
    :type subnet_resource_id: str
    """

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'subnet_resource_id': {'key': 'subnetResourceId', 'type': 'str'},
    }

    def __init__(self, *, ip_address: str=None, subnet_resource_id: str=None, **kwargs) -> None:
        super(PrivateIPAddress, self).__init__(**kwargs)
        self.ip_address = ip_address
        self.subnet_resource_id = subnet_resource_id
