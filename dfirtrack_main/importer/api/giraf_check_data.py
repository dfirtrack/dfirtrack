from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger

def check_config(request):                              # coverage: ignore branch
    """ check variables in `dfirtrack.config` """

    # reset stop condition
    stop_importer_api_giraf = False

    # check GIRAF_URL for string
    if not isinstance(dfirtrack_config.GIRAF_URL, str):
        messages.error(request, "`GIRAF_URL` is not a string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " IMPORTER_API_GIRAF variable GIRAF_URL no string")
        stop_importer_api_giraf = True

    # check GIRAF_URL for empty string (check only if it actually is a string)
    if isinstance(dfirtrack_config.GIRAF_URL, str) and not dfirtrack_config.GIRAF_URL:
        messages.error(request, "`GIRAF_URL` contains an empty string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " IMPORTER_API_GIRAF variable GIRAF_URL empty string")
        stop_importer_api_giraf = True

    # check GIRAF_USER for string
    if not isinstance(dfirtrack_config.GIRAF_USER, str):
        messages.error(request, "`GIRAF_USER` is not a string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " IMPORTER_API_GIRAF variable GIRAF_USER no string")
        stop_importer_api_giraf = True

    # check GIRAF_USER for empty string (check only if it actually is a string)
    if isinstance(dfirtrack_config.GIRAF_USER, str) and not dfirtrack_config.GIRAF_USER:
        messages.error(request, "`GIRAF_USER` contains an empty string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " IMPORTER_API_GIRAF variable GIRAF_USER empty string")
        stop_importer_api_giraf = True

    # check GIRAF_PASS for string
    if not isinstance(dfirtrack_config.GIRAF_PASS, str):
        messages.error(request, "`GIRAF_PASS` is not a string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " IMPORTER_API_GIRAF variable GIRAF_PASS no string")
        stop_importer_api_giraf = True

    # check GIRAF_PASS for empty string (check only if it actually is a string)
    if isinstance(dfirtrack_config.GIRAF_PASS, str) and not dfirtrack_config.GIRAF_PASS:
        messages.error(request, "`GIRAF_PASS` contains an empty string. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " IMPORTER_API_GIRAF variable GIRAF_PASS empty string")
        stop_importer_api_giraf = True

    return stop_importer_api_giraf
