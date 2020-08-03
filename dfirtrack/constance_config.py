"""
Configuration used in DFIRTrack with django-constance.
"""

CONSTANCE_CONFIG = {
    # used in dfirtrack_main.exporter.spreadsheet.csv and dfirtrack_main.exporter.spreadsheet.xls
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
    # used in `dfirtrack_main.exporter.markdown`
    'MARKDOWN_PATH': (
        '',
        'Path for the markdown documentation export',
        str,
    ),
    'MARKDOWN_SORTING': (
        'systemsorted',
        'Choose sorting for system markdown export',
        'markdown_sorting_field',
    ),
    # used in `dfirtrack_main.importer.file.csv_config_based` and `dfirtrack_main.importer.file.csv_form_based`
    'CSV_SKIP_EXISTING_SYSTEM': (
        True,
        'Skip existing systems',
        bool,
    ),
    'CSV_COLUMN_SYSTEM': (
        1,
        'Number of the column in the CSV file that contains the system name',
        int,
    ),
    'CSV_HEADLINE': (
        True,
        'CSV file contains a headline row',
        bool,
    ),
    'CSV_CHOICE_IP': (
        False,
        'CSV file contains IP addresses',
        bool,
    ),
    'CSV_REMOVE_IP': (
        False,
        'Remove / overwrite existing IP addresses for already existing systems',
        bool,
    ),
    'CSV_COLUMN_IP': (
        2,
        'Number of the column in the CSV file that contains the IP addresses',
        int,
    ),
    'CSV_REMOVE_CASE': (
        False,
        'Remove / overwrite existing cases for already existing systems',
        bool,
    ),
    'CSV_REMOVE_COMPANY': (
        False,
        'Remove / overwrite existing companies for already existing systems',
        bool,
    ),
    'CSV_REMOVE_TAG': (
        False,
        'Remove / overwrite existing tags for already existing systems',
        bool,
    ),
    'CSV_DEFAULT_SYSTEMSTATUS': (
        '2',
        'Set systemstatus',
        'systemstatus_field',
    ),
    'CSV_DEFAULT_ANALYSISSTATUS': (
        '1',
        'Set analysisstatus',
        'analysisstatus_field',
    ),
    'CSV_DEFAULT_REASON': (
        '',
        'Set reason',
        'reason_field',
    ),
    'CSV_DEFAULT_DOMAIN': (
        '',
        'Set domain',
        'domain_field',
    ),
    'CSV_DEFAULT_DNSNAME': (
        '',
        'Set dnsname',
        'dnsname_field',
    ),
    'CSV_DEFAULT_SYSTEMTYPE': (
        '',
        'Set systemtype',
        'systemtype_field',
    ),
    'CSV_DEFAULT_OS': (
        '',
        'Set OS',
        'os_field',
    ),
    'CSV_DEFAULT_LOCATION': (
        '',
        'Set location',
        'location_field',
    ),
    'CSV_DEFAULT_SERVICEPROVIDER': (
        '',
        'Set serviceprovider',
        'serviceprovider_field',
    ),
}

"""
TODO:
this needs to be filled by a model query,
does not work at the moment because e. g. 'from dfirtrack_artifacts.models import Artifactstatus' is not allowed here or in 'dfirtrack.settings',
nevertheless that is not so relevant because the choices defined here are only statically shown in admin page,
what is shown in the form is dynamically generated in 'dfirtrack_artifacts.config_forms',
server restart might be necessary after changing values
"""
# create custom field types / lists
CONSTANCE_ADDITIONAL_FIELDS = {
    # artifactstatus - multiple choice
    # TODO: find a way for dynamically setting values
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
    # systemstatus - single choice
    # TODO: find a way for dynamically setting values
    'systemstatus_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('1', 'Clean'),
                ('2', 'Unknown'),
                ('3', 'Analysis ongoing'),
                ('4', 'Compromised'),
                ('5', 'Remediation done'),
                ('6', 'Reinstalled'),
                ('7', 'Removed'),
                ('8', 'Not analyzed'),
            ),
        },
    ],
    # analysisstatus - single choice
    # TODO: find a way for dynamically setting values
    'analysisstatus_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('1', 'Needs analysis'),
                ('2', 'Ready for analysis'),
                ('3', 'Ongoing analysis'),
                ('4', 'Nothing to do'),
                ('5', 'Main analysis finished'),
            ),
        },
    ],
    # reason - single choice
    # TODO: find a way for dynamically setting values
    'reason_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # domain - single choice
    # TODO: find a way for dynamically setting values
    'domain_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # dnsname - single choice
    # TODO: find a way for dynamically setting values
    'dnsname_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # systemtype - single choice
    # TODO: find a way for dynamically setting values
    'systemtype_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # os - single choice
    # TODO: find a way for dynamically setting values
    'os_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # location - single choice
    # TODO: find a way for dynamically setting values
    'location_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # serviceprovider - single choice
    # TODO: find a way for dynamically setting values
    'serviceprovider_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('', 'None selected'),
            ),
            'required': False,
        },
    ],
    # markdown sorting for system markdown exporter - single choice
    'markdown_sorting_field': [
        'django.forms.fields.ChoiceField', {
            'widget': 'django.forms.RadioSelect',
            'choices': (
                ('domainsorted', 'Sorted by domain'),
                ('systemsorted', 'Sorted by system'),
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
    'System markdown exporter options': (
        'MARKDOWN_PATH',
        'MARKDOWN_SORTING',
    ),
    'System file importer (CSV) options': (
        'CSV_SKIP_EXISTING_SYSTEM',
        'CSV_COLUMN_SYSTEM',
        'CSV_HEADLINE',
        'CSV_CHOICE_IP',
        'CSV_REMOVE_IP',
        'CSV_COLUMN_IP',
        'CSV_REMOVE_CASE',
        'CSV_REMOVE_COMPANY',
        'CSV_REMOVE_TAG',
        'CSV_DEFAULT_SYSTEMSTATUS',
        'CSV_DEFAULT_ANALYSISSTATUS',
        'CSV_DEFAULT_REASON',
        'CSV_DEFAULT_DOMAIN',
        'CSV_DEFAULT_DNSNAME',
        'CSV_DEFAULT_SYSTEMTYPE',
        'CSV_DEFAULT_OS',
        'CSV_DEFAULT_LOCATION',
        'CSV_DEFAULT_SERVICEPROVIDER',
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
