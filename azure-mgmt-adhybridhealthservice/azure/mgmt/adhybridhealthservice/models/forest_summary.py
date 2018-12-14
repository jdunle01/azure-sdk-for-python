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


class ForestSummary(Model):
    """The forest summary for an ADDS domain.

    :param forest_name: The forest name.
    :type forest_name: str
    :param domain_count: The domain count.
    :type domain_count: int
    :param site_count: The site count.
    :type site_count: int
    :param monitored_dc_count: The number of domain controllers that are
     monitored by Azure Active Directory Connect Health.
    :type monitored_dc_count: int
    :param total_dc_count: The total domain controllers.
    :type total_dc_count: int
    :param domains: The list of domain controller names.
    :type domains: list[str]
    :param sites: The list of site names.
    :type sites: list[str]
    """

    _attribute_map = {
        'forest_name': {'key': 'forestName', 'type': 'str'},
        'domain_count': {'key': 'domainCount', 'type': 'int'},
        'site_count': {'key': 'siteCount', 'type': 'int'},
        'monitored_dc_count': {'key': 'monitoredDcCount', 'type': 'int'},
        'total_dc_count': {'key': 'totalDcCount', 'type': 'int'},
        'domains': {'key': 'domains', 'type': '[str]'},
        'sites': {'key': 'sites', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ForestSummary, self).__init__(**kwargs)
        self.forest_name = kwargs.get('forest_name', None)
        self.domain_count = kwargs.get('domain_count', None)
        self.site_count = kwargs.get('site_count', None)
        self.monitored_dc_count = kwargs.get('monitored_dc_count', None)
        self.total_dc_count = kwargs.get('total_dc_count', None)
        self.domains = kwargs.get('domains', None)
        self.sites = kwargs.get('sites', None)