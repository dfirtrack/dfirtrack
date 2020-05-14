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
# choose optional worksheets with notes --> works only if corresponding attribute above is activated (XLS only)
SPREAD_WORKSHEET_SYSTEMSTATUS = False
SPREAD_WORKSHEET_REASON = False
SPREAD_WORKSHEET_TAG = False

# IMPORTER

# IMPORT SYSTEMS AND ENTRIES VIA GIRAF API (dfirtrack_main.importer.api.giraf)
## add an url for giraf (e. g. 'https://giraf.testing.vm')
GIRAF_URL = ''
## add an user for giraf api
GIRAF_USER = ''
## add a password for giraf api user
GIRAF_PASS = ''

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
