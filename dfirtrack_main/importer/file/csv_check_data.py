from constance import config as constance_config
from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger, critical_logger
from dfirtrack_main.models import Analysisstatus, Dnsname, Domain, Location, Os, Reason, Serviceprovider, Systemstatus, Systemtype

def check_system_importer_file_csv_config_based_variables(request):
    pass

def check_system_importer_file_csv_form_based_variables(request):
    pass

def check_config(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_system_importer_file_csv = False

#    # check CSV_HEADLINE for bool
#    if not isinstance(dfirtrack_config.CSV_HEADLINE, bool):
#        messages.error(request, "`CSV_HEADLINE` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_HEADLINE not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_SKIP_EXISTING_SYSTEM for bool
#    if not isinstance(dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM, bool):
#        messages.error(request, "`CSV_SKIP_EXISTING_SYSTEM` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_SKIP_EXISTING_SYSTEM not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_CHOICE_IP for bool
#    if not isinstance(dfirtrack_config.CSV_CHOICE_IP, bool):
#        messages.error(request, "`CSV_CHOICE_IP` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_IP not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_REMOVE_IP for bool
#    if not isinstance(dfirtrack_config.CSV_REMOVE_IP, bool):
#        messages.error(request, "`CSV_REMOVE_IP` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_REMOVE_IP not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_COLUMN_SYSTEM for int
#    if not isinstance(dfirtrack_config.CSV_COLUMN_SYSTEM, int):
#        messages.error(request, "`CSV_COLUMN_SYSTEM` is not an integer. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEM no integer")
#        stop_system_importer_file_csv = True

    # check CSV_COLUMN_SYSTEM for value
    if not 1<= constance_config.CSV_COLUMN_SYSTEM <= 256:
        messages.error(request, "`CSV_COLUMN_SYSTEM` is outside the allowed range. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEM out of range")
        stop_system_importer_file_csv = True

#    # check CSV_COLUMN_IP for int
#    if not isinstance(dfirtrack_config.CSV_COLUMN_IP, int):
#        messages.error(request, "`CSV_COLUMN_IP` is not an integer. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_IP no integer")
#        stop_system_importer_file_csv = True

    # check CSV_COLUMN_IP for value
    if not 1<= constance_config.CSV_COLUMN_IP <= 256:
        messages.error(request, "`CSV_COLUMN_IP` is outside the allowed range. Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_IP out of range")
        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_SYSTEMSTATUS for existence
#    try:
#        Systemstatus.objects.get(systemstatus_name = dfirtrack_config.CSV_DEFAULT_SYSTEMSTATUS)
#    except Systemstatus.DoesNotExist:
#        messages.warning(request, "Systemstatus with configured name '" + dfirtrack_config.CSV_DEFAULT_SYSTEMSTATUS + "' does not exist. Check `dfirtrack.config` or create systemstatus!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV systemstatus for variable CSV_DEFAULT_SYSTEMSTATUS does not exist")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_ANALYSISSTATUS for existence
#    try:
#        Analysisstatus.objects.get(analysisstatus_name = dfirtrack_config.CSV_DEFAULT_ANALYSISSTATUS)
#    except Analysisstatus.DoesNotExist:
#        messages.warning(request, "Analysisstatus with configured name does not exist. Check `dfirtrack.config` or create analysisstatus!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV analysisstatus for variable CSV_DEFAULT_ANALYSISSTATUS does not exist")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_REASON for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_REASON, str):
#        messages.error(request, "`CSV_DEFAULT_REASON` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_REASON no string")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_DOMAIN for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_DOMAIN, str):
#        messages.error(request, "`CSV_DEFAULT_DOMAIN` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_DOMAIN no string")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_DNSNAME for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_DNSNAME, str):
#        messages.error(request, "`CSV_DEFAULT_DNSNAME` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_DNSNAME no string")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_SYSTEMTYPE for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_SYSTEMTYPE, str):
#        messages.error(request, "`CSV_DEFAULT_SYSTEMTYPE` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_SYSTEMTYPE no string")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_OS for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_OS, str):
#        messages.error(request, "`CSV_DEFAULT_OS` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_OS no string")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_LOCATION for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_LOCATION, str):
#        messages.error(request, "`CSV_DEFAULT_LOCATION` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_LOCATION no string")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_SERVICEPROVIDER for string
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_SERVICEPROVIDER, str):
#        messages.error(request, "`CSV_DEFAULT_SERVICEPROVIDER` is not a string. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_SERVICEPROVIDER no string")
#        stop_system_importer_file_csv = True

#    # check CSV_REMOVE_CASE for bool
#    if not isinstance(dfirtrack_config.CSV_REMOVE_CASE, bool):
#        messages.error(request, "`CSV_REMOVE_CASE` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_REMOVE_CASE not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_CASE for list
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_CASE, list):
#        messages.error(request, "`CSV_DEFAULT_CASE` is not a list. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_CASE no list")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_CASE list elements for string and empty string
#    if isinstance(dfirtrack_config.CSV_DEFAULT_CASE, list):
#        for default_case in dfirtrack_config.CSV_DEFAULT_CASE:
#            # check for string
#            if not isinstance(default_case, str):
#                messages.error(request, "`CSV_DEFAULT_CASE` list contains one ore more no string values. Check `dfirtrack.config`!")
#                # call logger
#                warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_CASE list contains no string")
#                stop_system_importer_file_csv = True
#                # leave loop to get only one error per list
#                break
#            # check for empty string
#            if isinstance(default_case, str) and not default_case:
#                messages.error(request, "`CSV_DEFAULT_CASE` list contains one ore more empty strings. Check `dfirtrack.config`!")
#                # call logger
#                warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_CASE list contains empty string")
#                stop_system_importer_file_csv = True
#                # leave loop to get only one error per list
#                break

#    # check CSV_INCIDENT_CASE for bool
#    if not isinstance(dfirtrack_config.CSV_INCIDENT_CASE, bool):
#        messages.error(request, "`CSV_INCIDENT_CASE` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_INCIDENT_CASE not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_REMOVE_COMPANY for bool
#    if not isinstance(dfirtrack_config.CSV_REMOVE_COMPANY, bool):
#        messages.error(request, "`CSV_REMOVE_COMPANY` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_REMOVE_COMPANY not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_COMPANY for list
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_COMPANY, list):
#        messages.error(request, "`CSV_DEFAULT_COMPANY` is not a list. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_COMPANY no list")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_COMPANY list elements for string and empty string
#    if isinstance(dfirtrack_config.CSV_DEFAULT_COMPANY, list):
#        for default_company in dfirtrack_config.CSV_DEFAULT_COMPANY:
#            # check for string
#            if not isinstance(default_company, str):
#                messages.error(request, "`CSV_DEFAULT_COMPANY` list contains one ore more no string values. Check `dfirtrack.config`!")
#                # call logger
#                warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_COMPANY list contains no string")
#                stop_system_importer_file_csv = True
#                # leave loop to get only one error per list
#                break
#            # check for empty string
#            if isinstance(default_company, str) and not default_company:
#                messages.error(request, "`CSV_DEFAULT_COMPANY` list contains one ore more empty strings. Check `dfirtrack.config`!")
#                # call logger
#                warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_COMPANY list contains empty string")
#                stop_system_importer_file_csv = True
#                # leave loop to get only one error per list
#                break

#    # check CSV_REMOVE_TAG for bool
#    if not isinstance(dfirtrack_config.CSV_REMOVE_TAG, bool):
#        messages.error(request, "`CSV_REMOVE_TAG` is not boolean. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_REMOVE_TAG not boolean")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_TAG for list
#    if not isinstance(dfirtrack_config.CSV_DEFAULT_TAG, list):
#        messages.error(request, "`CSV_DEFAULT_TAG` is not a list. Check `dfirtrack.config`!")
#        # call logger
#        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_TAG no list")
#        stop_system_importer_file_csv = True

#    # check CSV_DEFAULT_TAG list elements for string and empty string
#    if isinstance(dfirtrack_config.CSV_DEFAULT_TAG, list):
#        for default_tag in dfirtrack_config.CSV_DEFAULT_TAG:
#            # check for string
#            if not isinstance(default_tag, str):
#                messages.error(request, "`CSV_DEFAULT_TAG` list contains one ore more no string values. Check `dfirtrack.config`!")
#                # call logger
#                warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_TAG list contains no string")
#                stop_system_importer_file_csv = True
#                # leave loop to get only one error per list
#                break
#            # check for empty string
#            if isinstance(default_tag, str) and not default_tag:
#                messages.error(request, "`CSV_DEFAULT_TAG` list contains one ore more empty strings. Check `dfirtrack.config`!")
#                # call logger
#                warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_TAG list contains empty string")
#                stop_system_importer_file_csv = True
#                # leave loop to get only one error per list
#                break

    # create final message and log
    if stop_system_importer_file_csv:
        messages.warning(request, "Nothing was changed.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_ENDED_WITH_ERRORS")

    return stop_system_importer_file_csv

def check_file(request, rows):
    """ check file for csv respectively some kind of text file """

    try:
        # try to iterate over rows
        for row in rows:
            # do nothing
            pass

        # return True if successful
        return True

    # wrong file type
    except UnicodeDecodeError:
        messages.error(request, "File seems not to be a CSV file. Check file.")
        # call logger
        critical_logger(str(request.user), " SYSTEM_IP_IMPORTER_WRONG_FILE_TYPE")
        # return False if not successful
        return False

def check_row(request, row, row_counter):
    """ check some values of csv rows """

    # reset continue condition
    continue_system_importer_file_csv = False

    # check system column for empty value
    if row[dfirtrack_config.CSV_COLUMN_SYSTEM] == '':
        messages.error(request, "Value for system in row " + str(row_counter) + " was an empty string. System not created.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_COLUMN " + "row_" + str(row_counter) + ":empty_column")
        continue_system_importer_file_csv = True

    # TODO: falls-check for string does not work as expected (even true-check for int does not yield the expected result)
    ## check system column for string
    #if not isinstance(row[dfirtrack_config.CSV_COLUMN_SYSTEM], str):
    #    messages.error(request, "Value for system in row " + str(row_counter) + " was not a string. System not created.")
    #    # call logger
    #    warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_COLUMN " + "row_" + str(i) + ":no_string")
    #    continue_system_importer_file_csv = True

    # check system column for length of string
    if len(row[dfirtrack_config.CSV_COLUMN_SYSTEM]) > 50:
        messages.error(request, "Value for system in row " + str(row_counter) + " was too long. System not created.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_COLUMN " + "row_" + str(row_counter) + ":long_string")
        continue_system_importer_file_csv = True

    return continue_system_importer_file_csv
