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


class IncidentInfo(Model):
    """Describes related incident information for the bookmark.

    All required parameters must be populated in order to send to Azure.

    :param incident_id: Required. Incident Id
    :type incident_id: str
    :param severity: Required. The severity of the incident. Possible values
     include: 'Critical', 'High', 'Medium', 'Low', 'Informational'
    :type severity: str or ~azure.mgmt.securityinsight.models.CaseSeverity
    :param title: Required. The title of the incident
    :type title: str
    :param relation_name: Required. Relation Name
    :type relation_name: str
    """

    _validation = {
        'incident_id': {'required': True},
        'severity': {'required': True},
        'title': {'required': True},
        'relation_name': {'required': True},
    }

    _attribute_map = {
        'incident_id': {'key': 'incidentId', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'relation_name': {'key': 'relationName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IncidentInfo, self).__init__(**kwargs)
        self.incident_id = kwargs.get('incident_id', None)
        self.severity = kwargs.get('severity', None)
        self.title = kwargs.get('title', None)
        self.relation_name = kwargs.get('relation_name', None)
