from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack_config.models import MainConfigModel, SystemImporterFileCsvCronbasedConfigModel
from dfirtrack_main.logger.default_logger import error_logger, warning_logger
import os

def check_config(request, model):
    """ check variables of dfirtrack.config """

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

def check_file(request, rows):
    """ check file for csv respectively some kind of text file """

    # TODO: add check for file containing null bytes (\x00)
    # TODO: add check for empty file (0 bytes)

    try:
        # try to iterate over rows
        for row in rows:
            # do nothing
            pass

        # return True if successful
        return True

    # wrong file type
    except UnicodeDecodeError:
        # call message
        messages.error(request, "File seems not to be a CSV file. Check file.")
        # call logger
        error_logger(str(request.user), " SYSTEM_IP_IMPORTER_WRONG_FILE_TYPE")
        # return False if not successful
        return False

def check_row(request, row, row_counter, model):
    """ check some values of csv rows """

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

@login_required(login_url="/login")
def config_check_cron(request):
    """ config check before redirect for creating scheduled task """

    # reset stop condition
    stop_system_importer_file_csv_cronbased = False

    # get config model
    model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')

    """ check user """

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        # call message
        messages.error(request, "No user for import defined. Check config!")
        # set stop condition
        stop_system_importer_file_csv_cronbased = True

    """ check file system """

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # call message
        messages.error(request, "CSV import path does not exist. Check config or file system!")
        # set stop condition
        stop_system_importer_file_csv_cronbased = True
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # call message
            messages.error(request, "No read permission for CSV import path. Check config or file system!")
            # set stop condition
            stop_system_importer_file_csv_cronbased = True
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_import_file):
                # call message
                messages.error(request, "CSV import file does not exist. Check config or provide file!")
                # set stop condition
                stop_system_importer_file_csv_cronbased = True
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_import_file, os.R_OK):
                    # call message
                    messages.error(request, "No read permission for CSV import file. Check config or file system!")
                    # set stop condition
                    stop_system_importer_file_csv_cronbased = True

    # check stop condition
    if stop_system_importer_file_csv_cronbased:
        # return to system list
        return redirect(reverse('system_list'))
    else:
        # TODO: build url with python
        # TODO: open in new tab
        # open django admin with pre-filled form for scheduled task
        return redirect('/admin/django_q/schedule/add/?name=system_importer_file_csv_cron_based&func=dfirtrack_main.importer.file.csv_cron_based.system')

def config_check_run(model):
    """ config check before running importer """

    # reset stop condition
    stop_system_importer_file_csv_run = False

    """ check user """

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

    """ check file system """

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # call logger
        error_logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NOT_EXISTING")
        # set stop condition
        stop_system_importer_file_csv_run = True
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # call logger
            error_logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NO_READ_PERMISSION")
            # set stop condition
            stop_system_importer_file_csv_run = True
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_import_file):
                # call logger
                error_logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NOT_EXISTING")
                # set stop condition
                stop_system_importer_file_csv_run = True
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_import_file, os.R_OK):
                    # call logger
                    error_logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NO_READ_PERMISSION")
                    # set stop condition
                    stop_system_importer_file_csv_run = True

    # return stop condition
    return stop_system_importer_file_csv_run
