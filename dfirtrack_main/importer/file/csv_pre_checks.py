from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack_config.models import MainConfigModel, SystemImporterFileCsvConfigModel
from dfirtrack_main.logger.default_logger import error_logger, warning_logger
import os


@login_required(login_url="/login")
def pre_check_config_cron_user(request):
    """ config user and file system BEFORE redirect for creating scheduled task """

    # TODO: [config] split to 'pre_check_content_file_system'

    """
    related function:
    * 'system_cron'
    performed checks:
    * CSV import user: configured
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

    # TODO: [config] split to user and file system
    # TODO: [maintenance] merge with run-based check functions
    # TODO: [maintenance] such as 'check_config_user_run' and 'check_file_system_run'
    # TODO: [maintenance] main challenge is the different usage of messages and loggers
    # TODO: [config] differentiate between user, file system and attributes

    # reset stop condition
    stop_system_importer_file_csv = False

    # get config model (necessary because directly called by url)
    model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name = 'SystemImporterFileCsvConfig')

    """ check user """

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        # call message
        messages.error(request, "No user for import defined. Check config!")
        # set stop condition
        stop_system_importer_file_csv = True

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

    # check stop condition
    if stop_system_importer_file_csv:
        # return to system list
        return redirect(reverse('system_list'))
    else:
        # TODO: [logic] build url with python
        # open django admin with pre-filled form for scheduled task
        return redirect('/admin/django_q/schedule/add/?name=system_importer_file_csv&func=dfirtrack_main.importer.file.csv.system_cron')

def pre_check_content_file_system():
    pass

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
