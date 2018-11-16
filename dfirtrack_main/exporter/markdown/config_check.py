from django.contrib import messages
from django.shortcuts import redirect
from dfirtrack.config import MARKDOWN_PATH as markdown_path
from dfirtrack_main.logger.default_logger import debug_logger, error_logger

def config_check(request):
    """ check variables in `dfirtrack.config` """

    # check MARKDOWN_PATH
    if markdown_path == '':
        # call logger
        error_logger(str(request.user), " MARKDOWN_PATH_VARIABLE_UNDEFINED")
        messages.error(request, "The variable MARKDOWN_PATH seems to be undefined. Check `dfirtrack.config`!")
        # call logger for consistency
        debug_logger(str(request.user), " SYSTEM_MARKDOWN_SYSTEMS_END")
        # leave exporter
        return redirect('/systems/')
