from django.contrib import messages
from dfirtrack_config.models import MainConfigModel, SystemExporterMarkdownConfigModel
from dfirtrack_main.exporter.markdown.messages import error_message_cron
from dfirtrack_main.logger.default_logger import error_logger
import os


def check_content_file_system(request=None):
    """ check file system """

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')

    # reset stop condition
    stop_exporter_markdown = False

    """ set username for logger """

    # get config
    main_config_model = MainConfigModel.objects.get(main_config_name = 'MainConfig')

    # if function was called from 'system' / 'system_create_cron'
    if request:
        logger_username = str(request.user)
    # if function was called from 'system_cron'
    else:
        logger_username = main_config_model.cron_username

    # check MARKDOWN_PATH for empty string - stop immediately
    if not model.markdown_path:
        # if function was called from 'system'
        if request:
            messages.error(request, 'Markdown path contains an emtpy string. Check config!')
        # if function was called from 'system_cron'
        else:
            error_message_cron('Markdown path contains an emtpy string. Check config!')
        # call logger
        error_logger(logger_username, ' MARKDOWN_EXPORTER_MARKDOWN_PATH_EMPTY_STRING')
        # set stop condition
        stop_exporter_markdown = True
    else:
        # check MARKDOWN_PATH for existence in file system - stop immediately
        if not os.path.isdir(model.markdown_path):
            # if function was called from 'system'
            if request:
                messages.error(request, 'Markdown path does not exist in file system. Check config or filesystem!')
            # if function was called from 'system_cron'
            else:
                error_message_cron('Markdown path does not exist in file system. Check config or filesystem!')
            # call logger
            error_logger(logger_username, ' MARKDOWN_EXPORTER_MARKDOWN_PATH_NOT_EXISTING')
            # set stop condition
            stop_exporter_markdown = True
        else:
            # check MARKDOWN_PATH for write permission - stop immediately
            if not os.access(model.markdown_path, os.W_OK):
                # if function was called from 'system'
                if request:
                    messages.error(request, 'No write permission for markdown path. Check config or filesystem!')
                # if function was called from 'system_cron'
                else:
                    error_message_cron('No write permission for markdown path. Check config or filesystem!')
                # call logger
                error_logger(logger_username, ' MARKDOWN_EXPORTER_MARKDOWN_PATH_NO_WRITE_PERMISSION')
                # set stop condition
                stop_exporter_markdown = True

    # return stop condition
    return stop_exporter_markdown
