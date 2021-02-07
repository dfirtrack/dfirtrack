from django.contrib import messages
from dfirtrack_config.models import MainConfigModel
from dfirtrack_main.logger.default_logger import error_logger, warning_logger
import os


def check_config_cron_user(model, request=None):
    """ check config user  """

    # reset stop condition
    stop_system_importer_file_csv = False

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        # if called from 'system_create_cron' (creating scheduled task)
        if request:
            # call message
            messages.error(request, "No user for import defined. Check config!")
            # get username (needed for logger)
            cron_username = str(request.user)
        # if called from 'system_cron' (scheduled task)
        else:
            # get main config model
            mainconfigmodel = MainConfigModel.objects.get(main_config_name = 'MainConfig')
            # get cron username from main config (needed for logger if no user was defined in the proper config)
            cron_username = mainconfigmodel.cron_username
        # call logger
        error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_NO_USER_DEFINED")
        # set stop condition
        stop_system_importer_file_csv = True

    # return stop condition
    return stop_system_importer_file_csv

def check_content_file_system(model, request=None):
    """ check file system """

    # reset stop condition
    stop_system_importer_file_csv = False

    """ set username for logger """

    # if function was called from 'system_instant'
    if request:
        cron_username = str(request.user)
    # if function was called from 'system_cron'
    else:
        cron_username = model.csv_import_username.username   # check for existence of user in config was done before

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # if function was called from 'system_instant'
        if request:
            # call messsage
            messages.error(request, "CSV import path does not exist. Check config or file system!")
        # call logger
        error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NOT_EXISTING")
        # set stop condition
        stop_system_importer_file_csv = True
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # if function was called from 'system_instant'
            if request:
                # call messsage
                messages.error(request, "No read permission for CSV import path. Check config or file system!")
            # call logger
            error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NO_READ_PERMISSION")
            # set stop condition
            stop_system_importer_file_csv = True
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_import_file):
                # if function was called from 'system_instant'
                if request:
                    # call messsage
                    messages.error(request, "CSV import file does not exist. Check config or provide file!")
                # call logger
                error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NOT_EXISTING")
                # set stop condition
                stop_system_importer_file_csv = True
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_import_file, os.R_OK):
                    # if function was called from 'system_instant'
                    if request:
                        # call messsage
                        messages.error(request, "No read permission for CSV import file. Check config or file system!")
                    # call logger
                    error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NO_READ_PERMISSION")
                    # set stop condition
                    stop_system_importer_file_csv = True
                else:
                    # CSV import file is empty - stop immediately
                    if os.path.getsize(csv_import_file) == 0:
                        # if function was called from 'system_instant'
                        if request:
                            # call messsage
                            messages.error(request, "CSV import file is empty. Check config or file system!")
                        # call logger
                        error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_EMPTY")
                        # set stop condition
                        stop_system_importer_file_csv = True

    # return stop condition
    return stop_system_importer_file_csv

def check_config_attributes(model, request=None):
    """ check config for logic errors about attributes """

    # reset stop condition
    stop_system_importer_file_csv = False

    """ set username for logger """

    # if function was called from 'system_instant' or 'system_upload' or 'system_create_cron'
    if request:
        username = str(request.user)
    # if function was called from 'system_cron'
    else:
        username = model.csv_import_username.username   # check for existence of user in config was done before

    # check CSV_COLUMN_SYSTEM for value
    if not 1 <= model.csv_column_system <= 99:
        # if function was called from 'system_instant' or 'system_upload'
        if request:
            # call message
            messages.error(request, "`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!")
        # call logger
        error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEM out of range")
        # set stop condition
        stop_system_importer_file_csv = True

    # CSV_COLUMN_IP
    if model.csv_column_ip:
        # check CSV_COLUMN_IP for value
        if not 1 <= model.csv_column_ip <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_IP` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_IP out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_DNSNAME
    if model.csv_column_dnsname:
        # check CSV_COLUMN_DNSNAME for value
        if not 1 <= model.csv_column_dnsname <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_DNSNAME` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_DNSNAME out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_DOMAIN
    if model.csv_column_domain:
        # check CSV_COLUMN_DOMAIN for value
        if not 1 <= model.csv_column_domain <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_DOMAIN` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_DOMAIN out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_LOCATION
    if model.csv_column_location:
        # check CSV_COLUMN_LOCATION for value
        if not 1 <= model.csv_column_location <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_LOCATION` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_LOCATION out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_OS
    if model.csv_column_os:
        # check CSV_COLUMN_OS for value
        if not 1 <= model.csv_column_os <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_OS` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_OS out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_REASON
    if model.csv_column_reason:
        # check CSV_COLUMN_REASON for value
        if not 1 <= model.csv_column_reason <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_REASON` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_REASON out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_RECOMMENDATION
    if model.csv_column_recommendation:
        # check CSV_COLUMN_RECOMMENDATION for value
        if not 1 <= model.csv_column_recommendation <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_RECOMMENDATION` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_RECOMMENDATION out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_SERVICEPROVIDER
    if model.csv_column_serviceprovider:
        # check CSV_COLUMN_SERVICEPROVIDER for value
        if not 1 <= model.csv_column_serviceprovider <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_SERVICEPROVIDER` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SERVICEPROVIDER out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_SYSTEMTYPE
    if model.csv_column_systemtype:
        # check CSV_COLUMN_SYSTEMTYPE for value
        if not 1 <= model.csv_column_systemtype <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_SYSTEMTYPE` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEMTYPE out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_CASE
    if model.csv_column_case:
        # check CSV_COLUMN_CASE for value
        if not 1 <= model.csv_column_case <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_CASE` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_CASE out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_COMPANY
    if model.csv_column_company:
        # check CSV_COLUMN_COMPANY for value
        if not 1 <= model.csv_column_company <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_COMPANY` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_COMPANY out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # CSV_COLUMN_TAG
    if model.csv_column_tag:
        # check CSV_COLUMN_TAG for value
        if not 1 <= model.csv_column_tag <= 99:
            # if function was called from 'system_instant' or 'system_upload'
            if request:
                # call message
                messages.error(request, "`CSV_COLUMN_TAG` is outside the allowed range. Check config!")
            # call logger
            error_logger(username, " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_TAG out of range")
            # set stop condition
            stop_system_importer_file_csv = True

    # TODO: [code] add checks like custom field validation in 'SystemImporterFileCsvConfigForm'

    return stop_system_importer_file_csv

def check_content_file_type(rows, username, request=None):
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
        # if function was called from 'system_instant' or 'system_upload'
        if request:
            # call message
            messages.error(request, "Wrong file type for CSV import. Check config or file system!")
        # call logger
        error_logger(username, " SYSTEM_IMPORTER_FILE_CSV_WRONG_FILE_TYPE")
        # return False if not successful
        return False

def check_content_attributes(request, row, row_counter, model):
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
