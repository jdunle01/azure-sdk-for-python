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


class MetricBaseline(Model):
    """The baseline results of a specific metric.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. the metric baseline Id.
    :type id: str
    :param type: Required. the resource type of the metric baseline resource.
    :type type: str
    :param metric_name: Required. the name of the metric.
    :type metric_name: str
    :param baselines: Required. the baseline for each time series that was
     queried.
    :type baselines: list[~azure.mgmt.monitor.models.TimeSeriesBaseline]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'metric_name': {'required': True},
        'baselines': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'metric_name': {'key': 'metricName', 'type': 'str'},
        'baselines': {'key': 'baselines', 'type': '[TimeSeriesBaseline]'},
    }

    def __init__(self, *, id: str, type: str, metric_name: str, baselines, **kwargs) -> None:
        super(MetricBaseline, self).__init__(**kwargs)
        self.id = id
        self.type = type
        self.metric_name = metric_name
        self.baselines = baselines
