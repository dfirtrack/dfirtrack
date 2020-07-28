#############################
#                           #
#   DFIRTrack config file   #
#                           #
#############################

from os.path import expanduser

# MAIN APP SETTINGS

## change path for the log file (default: `$HOME`) (used in `dfirtrack.settings`)
LOGGING_PATH = expanduser('~')
## decide whether the system name should be editable or not in system form to avoid accidentally corruption (admin can edit it either way)
SYSTEM_NAME_EDITABLE = False

# ARTIFACTS

## folder to store artifacts on DFIRTrack server (used in `dfirtrack_artifacs.models` and `dfirtrack_main.models`)
EVIDENCE_PATH = expanduser('~') + '/dfirtrack_artifact_storage'

# IMPORTER - SYSTEMS AND ENTRIES VIA GIRAF API (used in `dfirtrack_main.importer.api.giraf`)

## add an url for giraf (e. g. 'https://giraf.testing.vm')
GIRAF_URL = ''
## add an user for giraf api
GIRAF_USER = ''
## add a password for giraf api user
GIRAF_PASS = ''

# IMPORTER - SYSTEMS FROM CLIENT (FILE UPLOAD) CSV FILE (used in `dfirtrack_main.importer.file.csv.system`)

## CSV contains a headline (True) or not (False)
CSV_HEADLINE = True
## skip (True) or not (False) systems, that already exist
CSV_SKIP_EXISTING_SYSTEM = True

## IP should be set via CSV column (True) or not at all (False) (import via web form not possible for multiple systems)
CSV_CHOICE_IP = True
## remove existing IP addresses for already existing systems (only used if CSV_SKIP_EXISTING_SYSTEM is set to False and CSV_CHOICE_IP is set to True)
CSV_REMOVE_IP = True

## column of system rather system_name (numerical value starting with 0 [zero] for first column)
CSV_COLUMN_SYSTEM = 0
## column of ip address (numerical value starting with 0 [zero] for first column) (only used if CSV_CHOICE_IP is set to True)
CSV_COLUMN_IP = 1

## attributes with fixed values (used if CSV_CHOICE_... is set to True)

## 'Systemstatus' for imported systems (choose from 'Clean', 'Unknown', 'Analysis ongoing', 'Compromised', 'Remediation done', 'Reinstalled', 'Removed', 'Not analyzed' or your custom values)
CSV_DEFAULT_SYSTEMSTATUS = 'Unknown'
## 'Analysisstatus' for imported systems (choose from 'Needs analysis', 'Ready for analysis', 'Ongoing analysis', 'Nothing to do', 'Main analysis finished' or your custom values)
CSV_DEFAULT_ANALYSISSTATUS = 'Needs analysis'
## attributes with chooseable values (choose string for attribute name, non-existing attributes will be created)
CSV_DEFAULT_REASON = ''
CSV_DEFAULT_DOMAIN = ''
CSV_DEFAULT_DNSNAME = ''
CSV_DEFAULT_SYSTEMTYPE = ''
CSV_DEFAULT_OS = ''
CSV_DEFAULT_LOCATION = ''
CSV_DEFAULT_SERVICEPROVIDER = ''
# TODO: remove default values from list
## remove existing companies for already existing systems (only used if CSV_SKIP_EXISTING_SYSTEM is set to False and CSV_CHOICE_CASE is set to True)
CSV_REMOVE_CASE = True
## comma separated list of companies to add for every sytem (non-existing companies will be created)
CSV_DEFAULT_CASE = ['case_1', 'case_2', 'case_3']
## incident for cases from CSV_DEFAULT_CASE should be set to True of False if created
CSV_INCIDENT_CASE = True
## remove existing companies for already existing systems (only used if CSV_SKIP_EXISTING_SYSTEM is set to False and CSV_CHOICE_COMPANY is set to True)
CSV_REMOVE_COMPANY = True
## comma separated list of companies to add for every sytem (non-existing companies will be created)
CSV_DEFAULT_COMPANY = ['company_1', 'company_2', 'company_3']
## remove existing tags for already existing systems (only used if CSV_SKIP_EXISTING_SYSTEM is set to False and CSV_CHOICE_TAG is set to True)
CSV_REMOVE_TAG = True
## comma separated list of tags to add for every sytem (non-existing tags will be created)
CSV_DEFAULT_TAG = ['tag_1', 'tag_2', 'tag_3']
# deprecated, TODO: possibly use regarding tag handling (dfirtrack_main.importer.file.csv.system)
## add a list of strings representing the relevant tags you want to automatically import
#TAGLIST = []
## add a string used as prefix for clearly identifying previously automatically imported tags (e. g. "AUTO" leads to "AUTO_TAG")
#TAGPREFIX = ''

# IMPORTER - REPORTITEMS FROM SERVER FILESYSTEM (used in `dfirtrack_main.importer.file.filesystem.reportitem`)

## add a server path (without trailing slash!) where reportitems (preferably in markdown syntax) are stored as <system_name>.md (lowercase!)
REPORTITEM_FILESYSTEMPATH = ''
## add a headline for the reportitems to import
REPORTITEM_HEADLINE = ''
## add a subheadline for the reportitems to import
REPORTITEM_SUBHEADLINE = ''
## if 'True' the reportitem will be deleted from DFIRTrack if it disappears from the filesystem, change to 'False' to change this behaviour
REPORTITEM_DELETE = True
