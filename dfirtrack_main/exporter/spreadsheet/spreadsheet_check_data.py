from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger

def check_config(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_system_exporter_spreadsheet = False

    # check SPREAD_SYSTEM_ID for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_ID, bool):
        messages.error(request, "`SPREAD_SYSTEM_ID` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_SYSTEM_ID not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_DNSNAME for bool
    if not isinstance(dfirtrack_config.SPREAD_DNSNAME, bool):
        messages.error(request, "`SPREAD_DNSNAME` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_DNSNAME not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_DOMAIN for bool
    if not isinstance(dfirtrack_config.SPREAD_DOMAIN, bool):
        messages.error(request, "`SPREAD_DOMAIN` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_DOMAIN not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_SYSTEMSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEMSTATUS, bool):
        messages.error(request, "`SPREAD_SYSTEMSTATUS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_SYSTEMSTATUS not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_ANALYSISSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_ANALYSISSTATUS, bool):
        messages.error(request, "`SPREAD_ANALYSISSTATUS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_ANALYSISSTATUS not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_REASON for bool
    if not isinstance(dfirtrack_config.SPREAD_REASON, bool):
        messages.error(request, "`SPREAD_REASON` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_REASON not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_RECOMMENDATION for bool
    if not isinstance(dfirtrack_config.SPREAD_RECOMMENDATION, bool):
        messages.error(request, "`SPREAD_RECOMMENDATION` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_RECOMMENDATION not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_SYSTEMTYPE for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEMTYPE, bool):
        messages.error(request, "`SPREAD_SYSTEMTYPE` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_SYSTEMTYPE not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_IP for bool
    if not isinstance(dfirtrack_config.SPREAD_IP, bool):
        messages.error(request, "`SPREAD_IP` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_IP not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_OS for bool
    if not isinstance(dfirtrack_config.SPREAD_OS, bool):
        messages.error(request, "`SPREAD_OS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_OS not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_COMPANY for bool
    if not isinstance(dfirtrack_config.SPREAD_COMPANY, bool):
        messages.error(request, "`SPREAD_COMPANY` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_COMPANY not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_LOCATION for bool
    if not isinstance(dfirtrack_config.SPREAD_LOCATION, bool):
        messages.error(request, "`SPREAD_LOCATION` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_LOCATION not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_SERVICEPROVIDER for bool
    if not isinstance(dfirtrack_config.SPREAD_SERVICEPROVIDER, bool):
        messages.error(request, "`SPREAD_SERVICEPROVIDER` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_SERVICEPROVIDER not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_TAG for bool
    if not isinstance(dfirtrack_config.SPREAD_TAG, bool):
        messages.error(request, "`SPREAD_TAG` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_TAG not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_CASE for bool
    if not isinstance(dfirtrack_config.SPREAD_CASE, bool):
        messages.error(request, "`SPREAD_CASE` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_CASE not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_SYSTEM_CREATE_TIME for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME, bool):
        messages.error(request, "`SPREAD_SYSTEM_CREATE_TIME` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_SYSTEM_CREATE_TIME not boolean")
        stop_system_exporter_spreadsheet = True

    # check SPREAD_SYSTEM_MODIFY_TIME for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME, bool):
        messages.error(request, "`SPREAD_SYSTEM_MODIFY_TIME` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_SYSTEM_MODIFY_TIME not boolean")
        stop_system_exporter_spreadsheet = True

    return stop_system_exporter_spreadsheet

def check_worksheet(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_system_exporter_spreadsheet_worksheet = False

    # check SPREAD_WORKSHEET_SYSTEMSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_SYSTEMSTATUS, bool):
        messages.error(request, "`SPREAD_WORKSHEET_SYSTEMSTATUS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_WORKSHEET_SYSTEMSTATUS not boolean")
        stop_system_exporter_spreadsheet_worksheet = True

    # check SPREAD_WORKSHEET_ANALYSISSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_ANALYSISSTATUS, bool):
        messages.error(request, "`SPREAD_WORKSHEET_ANALYSISSTATUS` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_WORKSHEET_ANALYSISSTATUS not boolean")
        stop_system_exporter_spreadsheet_worksheet = True

    # check SPREAD_WORKSHEET_REASON for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_REASON, bool):
        messages.error(request, "`SPREAD_WORKSHEET_REASON` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_WORKSHEET_REASON not boolean")
        stop_system_exporter_spreadsheet_worksheet = True

    # check SPREAD_WORKSHEET_RECOMMENDATION for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_RECOMMENDATION, bool):
        messages.error(request, "`SPREAD_WORKSHEET_RECOMMENDATION` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_WORKSHEET_RECOMMENDATION not boolean")
        stop_system_exporter_spreadsheet_worksheet = True

    # check SPREAD_WORKSHEET_TAG for bool
    if not isinstance(dfirtrack_config.SPREAD_WORKSHEET_TAG, bool):
        messages.error(request, "`SPREAD_WORKSHEET_TAG` is not boolean. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET variable SPREAD_WORKSHEET_TAG not boolean")
        stop_system_exporter_spreadsheet_worksheet = True

    return stop_system_exporter_spreadsheet_worksheet
