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


class ClosedListModelUpdateObject(Model):
    """Object model for updating a list entity.

    :param sub_lists: The new sublists for the feature.
    :type sub_lists:
     list[~azure.cognitiveservices.language.luis.authoring.models.WordListObject]
    :param name: The new name of the list entity.
    :type name: str
    """

    _attribute_map = {
        'sub_lists': {'key': 'subLists', 'type': '[WordListObject]'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, sub_lists=None, name: str=None, **kwargs) -> None:
        super(ClosedListModelUpdateObject, self).__init__(**kwargs)
        self.sub_lists = sub_lists
        self.name = name
