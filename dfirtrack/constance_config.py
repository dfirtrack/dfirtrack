"""
Configuration used in DFIRTrack with django-constance.
"""

CONSTANCE_CONFIG = {
    # used in dfirtrack_main.exporter.spreadsheet.csv
    'SPREAD_SYSTEM_ID': (
        True,
        'Add system ID to spreadsheet export',
        bool,
    ),
    'SPREAD_DNSNAME': (
        True,
        'Add DNS name to spreadsheet export',
        bool,
    ),
    'SPREAD_DOMAIN': (
        True,
        'Add domain to spreadsheet export',
        bool,
    ),
    'SPREAD_SYSTEMSTATUS': (
        True,
        'Add systemstatus to spreadsheet export',
        bool,
    ),
    'SPREAD_ANALYSISSTATUS': (
        False,
        'Add analysisstatus to spreadsheet export',
        bool,
    ),
    'SPREAD_REASON': (
        False,
        'Add reason to spreadsheet export',
        bool,
    ),
    'SPREAD_RECOMMENDATION': (
        False,
        'Add recommendation to spreadsheet export',
        bool,
    ),
    'SPREAD_SYSTEMTYPE': (
        True,
        'Add systemtype to spreadsheet export',
        bool,
    ),
    'SPREAD_IP': (
        True,
        'Add IP to spreadsheet export',
        bool,
    ),
    'SPREAD_OS': (
        False,
        'Add OS to spreadsheet export',
        bool,
    ),
    'SPREAD_COMPANY': (
        False,
        'Add company to spreadsheet export',
        bool,
    ),
    'SPREAD_LOCATION': (
        False,
        'Add location to spreadsheet export',
        bool,
    ),
    'SPREAD_SERVICEPROVIDER': (
        False,
        'Add serviceprovider to spreadsheet export',
        bool,
    ),
    'SPREAD_TAG': (
        True,
        'Add tag to spreadsheet export',
        bool,
    ),
    'SPREAD_CASE': (
        False,
        'Add case to spreadsheet export',
        bool,
    ),
    'SPREAD_SYSTEM_CREATE_TIME': (
        True,
        'Add system create time to spreadsheet export',
        bool,
    ),
    'SPREAD_SYSTEM_MODIFY_TIME': (
        True,
        'Add system modify time to spreadsheet export',
        bool,
    ),
    # used in dfirtrack_main.exporter.spreadsheet.xls
    'SPREAD_WORKSHEET_SYSTEMSTATUS': (
        False,
        'Add additional worksheet to explain systemstatus',
        bool,
    ),
    'SPREAD_WORKSHEET_ANALYSISSTATUS': (
        False,
        'Add additional worksheet to explain analysisstatus',
        bool,
    ),
    'SPREAD_WORKSHEET_REASON': (
        False,
        'Add additional worksheet to explain reason',
        bool,
    ),
    'SPREAD_WORKSHEET_RECOMMENDATION': (
        False,
        'Add additional worksheet to explain recommendation',
        bool,
    ),
    'SPREAD_WORKSHEET_TAG': (
        False,
        'Add additional worksheet to explain tag',
        bool,
    ),
    # used in dfirtrack_artifacts.exporter.spreadsheet.xls
    'ARTIFACTLIST_ARTIFACT_ID': (
        True,
        'Add artifact ID to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_SYSTEM_ID': (
        True,
        'Add system IDto spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_SYSTEM_NAME': (
        True,
        'Add system name to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACTSTATUS': (
        True,
        'Add artifactstatus to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACTTYPE': (
        True,
        'Add artifacttype to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_SOURCE_PATH': (
        True,
        'Add source path to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_STORAGE_PATH': (
        False,
        'Add storage path to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_NOTE': (
        False,
        'Add note to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_MD5': (
        False,
        'Add MD5 to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_SHA1': (
        False,
        'Add SHA1 to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_SHA256': (
        False,
        'Add SHA256 to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_CREATE_TIME': (
        False,
        'Add create time to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_ARTIFACT_MODIFY_TIME': (
        False,
        'Add modify time to spreadsheet export',
        bool,
    ),
    'ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS': (
        True,
        'Add additional worksheet to explain artifactstatus',
        bool,
    ),
    'ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE': (
        True,
        'Add additional worksheet to explain artifacttype',
        bool,
    ),
    'ARTIFACTLIST_CHOICE_ARTIFACTSTATUS': (
        '1',
        'Export only artifacts with this artifactstatus',
        'artifactstatus_field',
    ),
}

"""
TODO:
this needs to be filled by a model query,
does not work at the moment because 'from dfirtrack_artifacts.models import Artifactstatus' is not allowed here or in 'dfirtrack.settings',
nevertheless that is not so relevant because the choices defined here are only shown in admin page,
what is shown in the form is defined in 'dfirtrack_artifacts.config_forms'
"""
# create custom field types
CONSTANCE_ADDITIONAL_FIELDS = {
    # artifactstatus
    'artifactstatus_field': [
        'django.forms.fields.MultipleChoiceField', {
            'widget': 'django.forms.CheckboxSelectMultiple',
            'choices': (
                ('1', 'Needs analysis'),
                ('2', 'Requested from customer'),
                ('3', 'Collecting through EDR'),
                ('4', 'Processing ongoing'),
                ('5', 'Import ongoing'),
                ('6', 'Ready for analysis'),
                ('7', 'Analysis ongoing'),
                ('8', 'Analysis finished'),
                ('9', 'Not available'),
            ),
        },
    ],
}

CONSTANCE_CONFIG_FIELDSETS = {
    'System spreadsheet exporter (CSV, XLS) options': (
        'SPREAD_SYSTEM_ID',
        'SPREAD_DNSNAME',
        'SPREAD_DOMAIN',
        'SPREAD_SYSTEMSTATUS',
        'SPREAD_ANALYSISSTATUS',
        'SPREAD_REASON',
        'SPREAD_RECOMMENDATION',
        'SPREAD_SYSTEMTYPE',
        'SPREAD_IP',
        'SPREAD_OS',
        'SPREAD_COMPANY',
        'SPREAD_LOCATION',
        'SPREAD_SERVICEPROVIDER',
        'SPREAD_TAG',
        'SPREAD_CASE',
        'SPREAD_SYSTEM_CREATE_TIME',
        'SPREAD_SYSTEM_MODIFY_TIME',
    ),
    'System spreadsheet exporter (XLS only) options': (
        'SPREAD_WORKSHEET_SYSTEMSTATUS',
        'SPREAD_WORKSHEET_ANALYSISSTATUS',
        'SPREAD_WORKSHEET_REASON',
        'SPREAD_WORKSHEET_RECOMMENDATION',
        'SPREAD_WORKSHEET_TAG',
    ),
    'Artifact spreadsheet exporter (CSV, XLS) options': (
        'ARTIFACTLIST_CHOICE_ARTIFACTSTATUS',
        'ARTIFACTLIST_ARTIFACT_ID',
        'ARTIFACTLIST_SYSTEM_ID',
        'ARTIFACTLIST_SYSTEM_NAME',
        'ARTIFACTLIST_ARTIFACTSTATUS',
        'ARTIFACTLIST_ARTIFACTTYPE',
        'ARTIFACTLIST_ARTIFACT_SOURCE_PATH',
        'ARTIFACTLIST_ARTIFACT_STORAGE_PATH',
        'ARTIFACTLIST_ARTIFACT_NOTE',
        'ARTIFACTLIST_ARTIFACT_MD5',
        'ARTIFACTLIST_ARTIFACT_SHA1',
        'ARTIFACTLIST_ARTIFACT_SHA256',
        'ARTIFACTLIST_ARTIFACT_CREATE_TIME',
        'ARTIFACTLIST_ARTIFACT_MODIFY_TIME',
    ),
    'Artifact spreadsheet exporter (XLS only) options': (
        'ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS',
        'ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE',
    ),
}
