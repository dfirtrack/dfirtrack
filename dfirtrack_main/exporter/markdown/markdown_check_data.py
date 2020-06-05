from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger
import os

def check_config(request):
    """ check variables in `dfirtrack.config` """

    # reset stop condition
    stop_exporter_markdown = False

    # check MARKDOWN_PATH for string
    if not isinstance(dfirtrack_config.MARKDOWN_PATH, str):
        messages.error(request, "`MARKDOWN_PATH` is not a string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " EXPORTER_MARKDOWN variable MARKDOWN_PATH no string")
        stop_exporter_markdown = True

    # check MARKDOWN_PATH for empty string (check only if it actually is a string)
    if isinstance(dfirtrack_config.MARKDOWN_PATH, str) and not dfirtrack_config.MARKDOWN_PATH:
        messages.error(request, "`MARKDOWN_PATH` contains an emtpy string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " EXPORTER_MARKDOWN variable MARKDOWN_PATH empty string")
        stop_exporter_markdown = True

    # check MARKDOWN_PATH for existence in file system (check only if it actually is a non-empty string)
    if isinstance(dfirtrack_config.MARKDOWN_PATH, str) and dfirtrack_config.MARKDOWN_PATH:
        if not os.path.isdir(dfirtrack_config.MARKDOWN_PATH):
            messages.error(request, "`MARKDOWN_PATH` does not exist in file system. Check `dfirtrack.config` or filesystem!")
            # call logger
            warning_logger(str(request.user), " EXPORTER_MARKDOWN path MARKDOWN_PATH not existing")
            stop_exporter_markdown = True

    return stop_exporter_markdown
