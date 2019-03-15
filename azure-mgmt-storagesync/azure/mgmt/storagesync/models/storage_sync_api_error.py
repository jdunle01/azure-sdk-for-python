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


class StorageSyncApiError(Model):
    """Error type.

    :param code: Error code of the given entry.
    :type code: str
    :param message: Error message of the given entry.
    :type message: str
    :param target: Target of the given error entry.
    :type target: str
    :param details: Error details of the given entry.
    :type details: ~azure.mgmt.storagesync.models.StorageSyncErrorDetails
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': 'StorageSyncErrorDetails'},
    }

    def __init__(self, **kwargs):
        super(StorageSyncApiError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
