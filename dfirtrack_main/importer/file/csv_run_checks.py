from django.contrib import messages
from dfirtrack_config.models import MainConfigModel
from dfirtrack_main.logger.default_logger import error_logger, warning_logger
import os


def run_check_config_cron_user(model):
    """ check config user WHILE running importer """

    """
    calling function:
    * 'system_cron'
    performed checks:
    * CSV import user: configured
    output:
    * logger
    result:
    * error: stop import
    """

    # TODO: [maintenance] merge with 'config_check_pre_system_cron'
    # TODO: [maintenance] main challenge is the different usage of messages and loggers
    # TODO: [config] differentiate between user, file system and attributes

    # reset stop condition
    stop_system_importer_file_csv_run = False

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        # get main config model
        mainconfigmodel = MainConfigModel.objects.get(main_config_name = 'MainConfig')
        # get cron username from main config (needed for logger if no user was defined in the proper config)
        cron_username = mainconfigmodel.cron_username
        # call logger
        error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_NO_USER_DEFINED")
        # set stop condition
        stop_system_importer_file_csv_run = True

    # return stop condition
    return stop_system_importer_file_csv_run

def run_check_content_file_system(model, request=None):
    """ check file system WHILE running importer """

    """
    calling function:
    * 'system_instant'
    * 'system_cron'
    performed checks:
    * CSV import path: existence
    * CSV import path: read permission
    * CSV import file: existence
    * CSV import file: read permission
    * CSV import file: content (not empty)
    output:
    * message (just 'system_instant')
    * logger
    result:
    * error: stop import
    """

    # TODO: [maintenance] merge with 'config_check_pre_system_cron'
    # TODO: [maintenance] main challenge is the different usage of messages and loggers
    # TODO: [config] differentiate between user, file system and attributes

    # reset stop condition
    stop_system_importer_file_csv_run = False

    # if function was called from 'system_instant'
    if request:
        username = request.user.username
    # if function was called from 'system_cron'
    else:
        username = model.csv_import_username.username   # check for existence of user in config was done before

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # if function was called from 'system_instant'
        if request:
            # call messsage
            messages.error(request, "CSV import path does not exist. Check config or file system!")
        # call logger
        error_logger(username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NOT_EXISTING")
        # set stop condition
        stop_system_importer_file_csv_run = True
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # if function was called from 'system_instant'
            if request:
                # call messsage
                messages.error(request, "No read permission for CSV import path. Check config or file system!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NO_READ_PERMISSION")
            # set stop condition
            stop_system_importer_file_csv_run = True
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_import_file):
                # if function was called from 'system_instant'
                if request:
                    # call messsage
                    messages.error(request, "CSV import file does not exist. Check config or provide file!")
                # call logger
                error_logger(username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NOT_EXISTING")
                # set stop condition
                stop_system_importer_file_csv_run = True
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_import_file, os.R_OK):
                    # if function was called from 'system_instant'
                    if request:
                        # call messsage
                        messages.error(request, "No read permission for CSV import file. Check config or file system!")
                    # call logger
                    error_logger(username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NO_READ_PERMISSION")
                    # set stop condition
                    stop_system_importer_file_csv_run = True
                else:
                    # CSV import file is empty - stop immediately
                    if os.path.getsize(csv_import_file) == 0:
                        # if function was called from 'system_instant'
                        if request:
                            # call messsage
                            messages.error(request, "CSV import file is empty. Check config or file system!")
                        # call logger
                        error_logger(username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_EMPTY")
                        # set stop condition
                        stop_system_importer_file_csv_run = True

    # return stop condition
    return stop_system_importer_file_csv_run

def run_check_config_attributes():
    pass

def run_check_content_file_type(rows, username):
    """ check file for csv respectively some kind of text file """

    # TODO: [logic] add check for file containing null bytes (\x00)

    try:
        # try to iterate over rows
        for row in rows:
            # do nothing
            pass

        # return True if successful
        return True

    # wrong file type
    except UnicodeDecodeError:
        # call logger
        error_logger(username, " SYSTEM_IP_IMPORTER_WRONG_FILE_TYPE")
        # return False if not successful
        return False

def run_check_content_attributes(request, row, row_counter, model):
    """ check some values of csv rows """

    # TODO: [config] modify for new importer
    # TODO: [config] check configured fields in row for valid values
    # TODO: [config] some checks might be called from 'add_fk_attributes' or 'add_many2many_attributes'

    # reset continue condition
    continue_system_importer_file_csv = False

    # check system column for empty string
    if not row[model.csv_column_system - 1]:
        # call message
        messages.error(request, "Value for system in row " + str(row_counter) + " was an empty string. System not created.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_COLUMN " + "row_" + str(row_counter) + ":empty_column")
        continue_system_importer_file_csv = True

    # check system column for length of string
    if len(row[model.csv_column_system - 1]) > 50:
        # call message
        messages.error(request, "Value for system in row " + str(row_counter) + " was too long. System not created.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_COLUMN " + "row_" + str(row_counter) + ":long_string")
        continue_system_importer_file_csv = True

    return continue_system_importer_file_csv
