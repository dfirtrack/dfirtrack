from django.contrib import messages
from dfirtrack.config import MARKDOWN_PATH as markdown_path
from dfirtrack_main.logger.default_logger import debug_logger, error_logger
import os

def path_check(request):
    """ check path from `dfirtrack.config` is existing in filesystem """

    # check MARKDOWN_PATH
    if not os.path.isdir(markdown_path):
        # call logger
        error_logger(str(request.user), " MARKDOWN_PATH_NOT_EXISTING")
        messages.error(request, "The path MARKDOWN_PATH does not exist. Check `dfirtrack.config` or filesystem!")
        # call logger for consistency
        debug_logger(str(request.user), " SYSTEM_MARKDOWN_SYSTEMS_END")
        # leave exporter
        return False
    else:
        return True
