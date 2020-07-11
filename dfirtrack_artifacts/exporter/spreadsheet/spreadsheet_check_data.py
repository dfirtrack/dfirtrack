from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_main.logger.default_logger import warning_logger

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
