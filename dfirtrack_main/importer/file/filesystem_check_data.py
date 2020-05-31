from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger
import os.path

def check_config(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_reportitem_importer_file_filesystem = False

    # check REPORTITEM_FILESYSTEMPATH for empty string
    if not dfirtrack_config.REPORTITEM_FILESYSTEMPATH:
        messages.error(request, "`REPORTITEM_FILESYSTEMPATH` contains an empty string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_IMPORTER_FILE_FILESYSTEM variable REPORTITEM_FILESYSTEMPATH contains empty string")
        stop_reportitem_importer_file_filesystem = True

    # check REPORTITEM_FILESYSTEMPATH existing directory (check only if REPORTITEM_FILESYSTEMPATH is not an empty string)
    if dfirtrack_config.REPORTITEM_FILESYSTEMPATH:
        if not os.path.isdir(dfirtrack_config.REPORTITEM_FILESYSTEMPATH):
            messages.error(request, "`REPORTITEM_FILESYSTEMPATH` points to a non-existing directory. Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " REPORTITEM_IMPORTER_FILE_FILESYSTEM variable REPORTITEM_FILESYSTEMPATH path does not exist")
            stop_reportitem_importer_file_filesystem = True

    # check REPORTITEM_HEADLINE for empty string
    if not dfirtrack_config.REPORTITEM_HEADLINE:
        messages.error(request, "`REPORTITEM_HEADLINE` contains an empty string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_IMPORTER_FILE_FILESYSTEM variable REPORTITEM_HEADLINE contains empty string")
        stop_reportitem_importer_file_filesystem = True

    # check REPORTITEM_SUBHEADLINE for empty string
    if not dfirtrack_config.REPORTITEM_SUBHEADLINE:
        messages.error(request, "`REPORTITEM_SUBHEADLINE` contains an empty string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_IMPORTER_FILE_FILESYSTEM variable REPORTITEM_SUBHEADLINE contains empty string")
        stop_reportitem_importer_file_filesystem = True

    # check REPORTITEM_DELETE for bool
    if not isinstance(dfirtrack_config.REPORTITEM_DELETE, bool):
        messages.error(request, "`REPORTITEM_DELETE` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_IMPORTER_FILE_FILESYSTEM variable REPORTITEM_DELETE not boolean")
        stop_reportitem_importer_file_filesystem = True

    # create final message and log
    if stop_reportitem_importer_file_filesystem:
        messages.warning(request, "Nothing was changed.")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_IMPORTER_FILE_FILESYSTEM_ENDED_WITH_ERRORS")

    return stop_reportitem_importer_file_filesystem 
