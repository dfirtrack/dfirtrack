from constance import config as constance_config
from django.contrib import messages
from dfirtrack_main.logger.default_logger import warning_logger
import os

def check_config(request):
    """ check variables in config """

    # reset stop condition
    stop_exporter_markdown = False

    # check MARKDOWN_PATH for empty string
    if not constance_config.MARKDOWN_PATH:
        messages.error(request, "`MARKDOWN_PATH` contains an emtpy string. Check config!")
        # call logger
        warning_logger(str(request.user), " EXPORTER_MARKDOWN variable MARKDOWN_PATH empty string")
        stop_exporter_markdown = True

    # check MARKDOWN_PATH for existence in file system (check only if it actually is a non-empty string)
    if constance_config.MARKDOWN_PATH:
        if not os.path.isdir(constance_config.MARKDOWN_PATH):
            messages.error(request, "`MARKDOWN_PATH` does not exist in file system. Check config or filesystem!")
            # call logger
            warning_logger(str(request.user), " EXPORTER_MARKDOWN path MARKDOWN_PATH not existing")
            stop_exporter_markdown = True

    # check MARKDOWN_PATH for write permission
    if not os.access(constance_config.MARKDOWN_PATH, os.W_OK):
        messages.error(request, "`MARKDOWN_PATH` is not writeable. Check config or filesystem!")
        # call logger
        warning_logger(str(request.user), " EXPORTER_MARKDOWN path MARKDOWN_PATH not writeable")
        stop_exporter_markdown = True

    return stop_exporter_markdown
