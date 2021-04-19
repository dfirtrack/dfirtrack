#############################
#                           #
#   DFIRTrack config file   #
#                           #
#############################

from os.path import expanduser

# MAIN APP SETTINGS

## change path for the log file (default: `$HOME`) (used in `dfirtrack.settings`)
LOGGING_PATH = expanduser('~')

# ARTIFACTS

## folder to store artifacts on DFIRTrack server (used in `dfirtrack_artifacs.models` and `dfirtrack_main.models`)
EVIDENCE_PATH = expanduser('~') + '/dfirtrack_artifact_storage'
