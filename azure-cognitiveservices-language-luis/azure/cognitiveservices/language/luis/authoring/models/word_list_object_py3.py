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


class WordListObject(Model):
    """Sublist of items for a Closed list.

    :param canonical_form: The standard form that the list represents.
    :type canonical_form: str
    :param list: List of synonym words.
    :type list: list[str]
    """

    _attribute_map = {
        'canonical_form': {'key': 'canonicalForm', 'type': 'str'},
        'list': {'key': 'list', 'type': '[str]'},
    }

    def __init__(self, *, canonical_form: str=None, list=None, **kwargs) -> None:
        super(WordListObject, self).__init__(**kwargs)
        self.canonical_form = canonical_form
        self.list = list
