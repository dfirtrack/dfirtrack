from django.contrib import messages
from dfirtrack_main.logger.default_logger import warning_logger
import os


def pre_check_config_attributes(request, model):
    """ check variables of dfirtrack.config """

    # TODO: [config] move to 'run_check_config_attributes'
    # TODO: [config] modify for new importer
    # TODO: [config] check the existing configuration for logic errors
    # TODO: [config] like the field validation in dfirtrack_config.forms.SystemImporterFileCsvConfigForm

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
