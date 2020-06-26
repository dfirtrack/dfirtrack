"""
Configuration used in DFIRTrack with django-constance.
"""

CONSTANCE_CONFIG = {
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
}
