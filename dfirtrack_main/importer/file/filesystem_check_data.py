from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger
import os.path

def check_config(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_reportitem_importer_file_filesystem = False

    # check whether REPORTITEM_FILESYSTEMPATH is defined in `dfirtrack.config`
    if dfirtrack_config.REPORTITEM_FILESYSTEMPATH == '':
        messages.error(request, "The variable REPORTITEM_FILESYSTEMPATH seems to be undefined. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_FILESYSTEMPATH_VARIABLE_UNDEFINED")
        stop_reportitem_importer_file_filesystem = True

    # check whether REPORTITEM_FILESYSTEMPATH points to non-existing directory
    if not os.path.isdir(dfirtrack_config.REPORTITEM_FILESYSTEMPATH):
        messages.error(request, "The variable REPORTITEM_FILESYSTEMPATH points to a non-existing directory. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_FILESYSTEM_IMPORTER_WRONG_PATH")
        stop_reportitem_importer_file_filesystem = True

    # check whether REPORTITEM_HEADLINE is defined in `dfirtrack.config`
    if dfirtrack_config.REPORTITEM_HEADLINE == '':
        messages.error(request, "The variable REPORTITEM_HEADLINE seems to be undefined. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_HEADLINE_VARIABLE_UNDEFINED")
        stop_reportitem_importer_file_filesystem = True

    # check whether REPORTITEM_SUBHEADLINE is defined in `dfirtrack.config`
    if dfirtrack_config.REPORTITEM_SUBHEADLINE == '':
        messages.error(request, "The variable REPORTITEM_SUBHEADLINE seems to be undefined. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_SUBHEADLINE_VARIABLE_UNDEFINED")
        stop_reportitem_importer_file_filesystem = True

    # check whether REPORTITEM_DELETE is defined in `dfirtrack.config`
    if not isinstance(dfirtrack_config.REPORTITEM_DELETE, bool):
        messages.error(request, "The variable REPORTITEM_DELETE seems to be undefined or not a boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " REPORTITEM_DELETE_VARIABLE_UNDEFINED")
        stop_reportitem_importer_file_filesystem = True

    return stop_reportitem_importer_file_filesystem 
