from dfirtrack_main.exporter.spreadsheet.messages import error_message_cron
from dfirtrack_main.logger.default_logger import error_logger
import os

def check_content_file_system(main_config_model, module_text):

    # reset stop condition
    stop_cron_exporter = False

    # cron export path does not exist - stop immediately
    if not os.path.isdir(main_config_model.cron_export_path):
        # call message for all users
        error_message_cron(f'{module_text}: Export path does not exist. Check config or file system!')
        # call logger
        error_logger(main_config_model.cron_username, f' {module_text}_SPREADSHEET_EXPORTER_CRON_EXPORT_PATH_NOT_EXISTING')
        # set stop condition
        stop_cron_exporter = True
    else:
        # no write permission for cron export path - stop immediately
        if not os.access(main_config_model.cron_export_path, os.R_OK):
            # call message for all users
            error_message_cron(f'{module_text}: No write permission for export path. Check config or file system!')
            # call logger
            error_logger(main_config_model.cron_username, f' {module_text}_SPREADSHEET_EXPORTER_CRON_EXPORT_PATH_NO_WRITE_PERMISSION')
            # set stop condition
            stop_cron_exporter = True

    # return stop condition
    return stop_cron_exporter
