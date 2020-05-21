#############################
#                           #
#   DFIRTrack config file   #
#                           #
#############################

from os.path import expanduser

# SETTINGS

# MAIN APP SETTINGS (dfirtrack.settings)
## change path for the log file (default: `$HOME`)
LOGGING_PATH = expanduser('~')
## change path for the markdown documentation
MARKDOWN_PATH = ''

# decide whether the system name should be editable or not in system form to avoid accidentally corruption (admin can edit it either way)
SYSTEM_NAME_EDITABLE = False

# ARTIFACTS
EVIDENCE_PATH = expanduser('~') + '/dfirtrack_artifact_storage'

# EXPORTER

# SPREADSHEET (CSV and XLS)
# choose optional system attributes to export to spreadsheet
SPREAD_SYSTEM_ID = True
SPREAD_DNSNAME = True
SPREAD_DOMAIN = True
SPREAD_SYSTEMSTATUS = True
SPREAD_ANALYSISSTATUS = False
SPREAD_REASON = False
SPREAD_RECOMMENDATION = False
SPREAD_SYSTEMTYPE = True
SPREAD_IP = True
SPREAD_OS = False
SPREAD_COMPANY = False
SPREAD_LOCATION = False
SPREAD_SERVICEPROVIDER = False
SPREAD_TAG = True
SPREAD_CASE = False
SPREAD_SYSTEM_CREATE_TIME = True
SPREAD_SYSTEM_MODIFY_TIME = True

# IMPORTER

# IMPORT SYSTEMS AND ENTRIES VIA GIRAF API (dfirtrack_main.importer.api.giraf)
## add an url for giraf (e. g. 'https://giraf.testing.vm')
GIRAF_URL = ''
## add an user for giraf api
GIRAF_USER = ''
## add a password for giraf api user
GIRAF_PASS = ''

# IMPORT SYSTEMS FROM CLIENT CSV FILE (dfirtrack_main.importer.file.csv.system)
## CSV contains a headline (True) or not (False)
CSV_HEADLINE = True
## skip (True) or not (False) systems, that already exist
CSV_SKIP_EXISTING_SYSTEM = True
## column of system rather system_name (numerical value starting with 0 [zero] for first column)
CSV_COLUMN_SYSTEM = 0
## 'Systemstatus' should be set (True) or not (False) during import
CSV_CHOICE_SYSTEMSTATUS = True
## 'Systemstatus' for imported systems (choose from 'Clean', 'Unknown', 'Analysis ongoing', 'Compromised', 'Remediation done', 'Reinstalled', 'Removed', 'Not analyzed' or your custom values)
CSV_DEFAULT_SYSTEMSTATUS = 'Unknown'
## 'Analysisstatus' should be set (True) or not (False) during import
CSV_CHOICE_ANALYSISSTATUS = True
## 'Analysisstatus' for imported systems (choose from 'Needs analysis', 'Ready for analysis', 'Ongoing analysis', 'Nothing to do', 'Main analysis finished' or your custom values)
CSV_DEFAULT_ANALYSISSTATUS = 'Needs analysis'
## 'Reason' should be set (True) or not (False) during import
CSV_CHOICE_REASON = False
## 'Reason' (ID) for imported systems (IMPORTANT: Reason has to be created manually beforehand!)
CSV_DEFAULT_REASON = 1
## 'IP' should be set (True) or not (False) during import
CSV_CHOICE_IP = True
## column of ip address (numerical value starting with 0 [zero] for first column)
CSV_COLUMN_IP = 1
## 'Domain' should be set (True) or not (False) during import
CSV_CHOICE_DOMAIN = False
## 'Domain' (ID) for imported systems (IMPORTANT: Domain has to be created manually beforehand!)
CSV_DEFAULT_DOMAIN = 1
## 'Dnsname' should be set (True) or not (False) during import
CSV_CHOICE_DNSNAME = False
## 'Dnsname' (ID) for imported systems (IMPORTANT: Dnsname has to be created manually beforehand!)
CSV_DEFAULT_DNSNAME = 1
## 'Systemtype' should be set (True) or not (False) during import
CSV_CHOICE_SYSTEMTYPE = False
## 'Systemtype' (ID) for imported systems (IMPORTANT: Systemtype has to be created manually beforehand!)
CSV_DEFAULT_SYSTEMTYPE = 1
## 'OS' should be set (True) or not (False) during import
CSV_CHOICE_OS = False
## 'OS' (ID) for imported systems (IMPORTANT: OS has to be created manually beforehand!)
CSV_DEFAULT_OS = 1
## 'Location' should be set (True) or not (False) during import
CSV_CHOICE_LOCATION = False
## 'Location' (ID) for imported systems (IMPORTANT: Location has to be created manually beforehand!)
CSV_DEFAULT_LOCATION = 1
## 'Serviceprovider' should be set (True) or not (False) during import
CSV_CHOICE_SERVICEPROVIDER = False
## 'Serviceprovider' (ID) for imported systems (IMPORTANT: Serviceprovider has to be created manually beforehand!)
CSV_DEFAULT_SERVICEPROVIDER = 1

# IMPORT SYSTEMS WITH TAGS FROM CLIENT CSV FILE (dfirtrack_main.importer.file.csv.systems_tags)
## add a list of strings representing the relevant tags you want to automatically import
TAGLIST = []
## add a string used as prefix for clearly identifying previously automatically imported tags (e. g. "AUTO" leads to "AUTO_TAG")
TAGPREFIX = ''
## add a headline for the systems to import by tags
SYSTEMTAG_HEADLINE = ''
## add a subheadline for the systems to import by tags
SYSTEMTAG_SUBHEADLINE = ''


# IMPORT REPORTITEMS FROM SERVER FILESYSTEM (dfirtrack_main.importer.file.filesystem.reportitems)
## add a server path (without trailing slash!) where reportitems (preferably in markdown syntax) are stored as <system_name>.md (lowercase!)
REPORTITEMS_FILESYSTEMPATH = ''
## add a headline for the reportitems to import
REPORTITEMS_HEADLINE = ''
## add a subheadline for the reportitems to import
REPORTITEMS_SUBHEADLINE = ''
## if 'True' the reportitem will be deleted from DFIRTrack if it disappears from the filesystem, change to 'False' to change this behaviour
REPORTITEMS_DELETE = True
