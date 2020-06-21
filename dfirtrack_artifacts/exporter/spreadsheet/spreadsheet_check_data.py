from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_main.logger.default_logger import warning_logger

def check_config(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_artifact_exporter_spreadsheet = False

    # check ARTIFACTLIST_ARTIFACT_ID for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_ID, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_ID` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_ID not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_SYSTEM_ID for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_SYSTEM_ID, bool):
        messages.error(request, "`ARTIFACTLIST_SYSTEM_ID` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_SYSTEM_ID not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_SYSTEM_NAME for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_SYSTEM_NAME, bool):
        messages.error(request, "`ARTIFACTLIST_SYSTEM_NAME` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_SYSTEM_NAME not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACTSTATUS for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACTSTATUS, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACTSTATUS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACTSTATUS not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACTTYPE for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACTTYPE, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACTTYPE` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACTTYPE not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_SOURCE_PATH for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_SOURCE_PATH, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_SOURCE_PATH` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_SOURCE_PATH not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_STORAGE_PATH for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_STORAGE_PATH, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_STORAGE_PATH` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_STORAGE_PATH not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_NOTE for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_NOTE, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_NOTE` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_NOTE not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_MD5 for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_MD5, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_MD5` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_MD5 not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_SHA1 for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_SHA1, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_SHA1` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_SHA1 not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_SHA256 for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_SHA256, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_SHA256` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_SHA256 not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_CREATE_TIME for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_CREATE_TIME, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_CREATE_TIME` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_CREATE_TIME not boolean")
        stop_artifact_exporter_spreadsheet = True

    # check ARTIFACTLIST_ARTIFACT_MODIFY_TIME for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_ARTIFACT_MODIFY_TIME, bool):
        messages.error(request, "`ARTIFACTLIST_ARTIFACT_MODIFY_TIME` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_ARTIFACT_MODIFY_TIME not boolean")
        stop_artifact_exporter_spreadsheet = True

    return stop_artifact_exporter_spreadsheet

def check_worksheet(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_artifact_exporter_spreadsheet_worksheet = False

    # check ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS, bool):
        messages.error(request, "`ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS not boolean")
        stop_artifact_exporter_spreadsheet_worksheet = True

    # check ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE for bool
    if not isinstance(dfirtrack_config.ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE, bool):
        messages.error(request, "`ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE not boolean")
        stop_artifact_exporter_spreadsheet_worksheet = True

    return stop_artifact_exporter_spreadsheet_worksheet

def check_artifactstatus(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_artifact_exporter_spreadsheet_artifactstatus = False

    # check ARTIFACTLIST_CHOICE_ARTIFACTSTATUS for list
    if not isinstance(dfirtrack_config.ARTIFACTLIST_CHOICE_ARTIFACTSTATUS, list):
        messages.error(request, "`ARTIFACTLIST_CHOICE_ARTIFACTSTATUS` is not a list. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_CHOICE_ARTIFACTSTATUS no list")
        stop_artifact_exporter_spreadsheet_artifactstatus = True

    # check ARTIFACTLIST_CHOICE_ARTIFACTSTATUS for existence
    for artifactstatus in dfirtrack_config.ARTIFACTLIST_CHOICE_ARTIFACTSTATUS:
        try:
            Artifactstatus.objects.get(artifactstatus_name = artifactstatus)
        except Artifactstatus.DoesNotExist:
            messages.warning(request, "Artifactstatus with configured name does not exist. Check `dfirtrack.config` or create artifactstatus!")
            # call logger
            warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET variable ARTIFACTLIST_CHOICE_ARTIFACTSTATUS does not exist")
            stop_artifact_exporter_spreadsheet_artifactstatus = True

    return stop_artifact_exporter_spreadsheet_artifactstatus
