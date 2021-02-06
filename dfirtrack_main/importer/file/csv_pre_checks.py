from django.contrib import messages
from dfirtrack_main.logger.default_logger import warning_logger
import os


def pre_check_config_cron_user(request, model):
    """ check config user BEFORE redirect for creating scheduled task """

    """
    calling function:
    * 'system_create_cron'
    performed checks:
    * CSV import user: configured
    output:
    * messages
    result:
    * success: forward to scheduled task page
    * error: redirect to 'system_list'
    """

    # reset stop condition
    stop_system_importer_file_csv = False

    """ check user """

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        # call message
        messages.error(request, "No user for import defined. Check config!")
        # set stop condition
        stop_system_importer_file_csv = True

    return stop_system_importer_file_csv

def pre_check_content_file_system(request, model, stop_system_importer_file_csv):
    """ check file system BEFORE redirect for creating scheduled task """

    """
    calling function:
    * 'system_create_cron'
    performed checks:
    * CSV import path: existence
    * CSV import path: read permission
    * CSV import file: existence
    * CSV import file: read permission
    * CSV import file: content (not empty)
    output:
    * messages
    result:
    * success: forward to scheduled task page
    * error: redirect to 'system_list'
    """

    """ check file system """

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # call message
        messages.error(request, "CSV import path does not exist. Check config or file system!")
        # set stop condition
        stop_system_importer_file_csv = True
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # call message
            messages.error(request, "No read permission for CSV import path. Check config or file system!")
            # set stop condition
            stop_system_importer_file_csv = True
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_import_file):
                # call message
                messages.error(request, "CSV import file does not exist. Check config or provide file!")
                # set stop condition
                stop_system_importer_file_csv = True
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_import_file, os.R_OK):
                    # call message
                    messages.error(request, "No read permission for CSV import file. Check config or file system!")
                    # set stop condition
                    stop_system_importer_file_csv = True
                else:
                    # CSV import file is empty - stop immediately
                    if os.path.getsize(csv_import_file) == 0:
                        # call message
                        messages.error(request, "CSV import file is empty. Check config or file system!")
                        # set stop condition
                        stop_system_importer_file_csv = True

    return stop_system_importer_file_csv

def pre_check_config_attributes(request, model):
    """ check variables of dfirtrack.config """

    # TODO: [config] modify for new importer
    # TODO: [config] check the existing configuration for logic errors
    # TODO: [config] like the field validation in dfirtrack_config.forms.SystemImporterFileCsvConfigForm
    # TODO: [config] differentiate between user, file system and attributes

    # reset stop condition
    stop_system_importer_file_csv = False

    # check CSV_COLUMN_SYSTEM for value
    if not 1<= model.csv_column_system <= 256:
        # call message
        messages.error(request, "`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEM out of range")
        stop_system_importer_file_csv = True

    # check CSV_COLUMN_IP for value
    if not 1<= model.csv_column_ip <= 256:
        # call message
        messages.error(request, "`CSV_COLUMN_IP` is outside the allowed range. Check config!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_IP out of range")
        stop_system_importer_file_csv = True

    # create final message and log
    if stop_system_importer_file_csv:
        # call message
        messages.warning(request, "Nothing was changed.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_ENDED_WITH_ERRORS")

    return stop_system_importer_file_csv
