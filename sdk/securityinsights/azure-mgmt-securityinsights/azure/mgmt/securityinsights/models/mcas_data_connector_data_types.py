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

from .alerts_data_type_of_data_connector import AlertsDataTypeOfDataConnector


class MCASDataConnectorDataTypes(AlertsDataTypeOfDataConnector):
    """The available data types for MCAS (Microsoft Cloud App Security) data
    connector.

    :param alerts: Alerts data type connection.
    :type alerts:
     ~azure.mgmt.securityinsight.models.DataConnectorDataTypeCommon
    :param discovery_logs: Discovery log data type connection.
    :type discovery_logs:
     ~azure.mgmt.securityinsight.models.DataConnectorDataTypeCommon
    """

    _attribute_map = {
        'alerts': {'key': 'alerts', 'type': 'DataConnectorDataTypeCommon'},
        'discovery_logs': {'key': 'discoveryLogs', 'type': 'DataConnectorDataTypeCommon'},
    }

    def __init__(self, **kwargs):
        super(MCASDataConnectorDataTypes, self).__init__(**kwargs)
        self.discovery_logs = kwargs.get('discovery_logs', None)
