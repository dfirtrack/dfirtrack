import os

from django.contrib import messages

from dfirtrack_main.exporter.spreadsheet.messages import error_message_cron
from dfirtrack_main.logger.default_logger import error_logger


def check_content_file_system(main_config_model, module_text, request=None):
    """check file system"""

    # reset stop condition
    stop_cron_exporter = False

    """ set username for logger """

    # if function was called from 'artifact_create_cron' / 'system_create_cron'
    if request:
        logger_username = str(request.user)
    # if function was called from 'artifact_cron' / 'system_cron'
    else:
        logger_username = main_config_model.cron_username

    # cron export path does not exist - stop immediately
    if not os.path.isdir(main_config_model.cron_export_path):
        # if function was called from 'artifact_create_cron' / 'system_create_cron'
        if request:
            # call message
            messages.error(
                request, 'Export path does not exist. Check config or file system!'
            )
        # if function was called from 'artifact_cron' / 'system_cron'
        else:
            # call message for all users
            error_message_cron(
                f'{module_text}: Export path does not exist. Check config or file system!'
            )
        # call logger
        error_logger(
            logger_username,
            f' {module_text}_SPREADSHEET_EXPORTER_CRON_EXPORT_PATH_NOT_EXISTING',
        )
        # set stop condition
        stop_cron_exporter = True
    else:
        # no write permission for cron export path - stop immediately
        if not os.access(main_config_model.cron_export_path, os.R_OK):
            # if function was called from 'artifact_create_cron' / 'system_create_cron'
            if request:
                # call message
                messages.error(
                    request,
                    'No write permission for export path. Check config or file system!',
                )
            # if function was called from 'artifact_cron' / 'system_cron'
            else:
                # call message for all users
                error_message_cron(
                    f'{module_text}: No write permission for export path. Check config or file system!'
                )
            # call logger
            error_logger(
                logger_username,
                f' {module_text}_SPREADSHEET_EXPORTER_CRON_EXPORT_PATH_NO_WRITE_PERMISSION',
            )
            # set stop condition
            stop_cron_exporter = True

    # return stop condition
    return stop_cron_exporter
