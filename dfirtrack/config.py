#############################
#                           #
#   DFIRTrack config file   #
#                           #
#############################


# IMPORTER

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
