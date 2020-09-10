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
