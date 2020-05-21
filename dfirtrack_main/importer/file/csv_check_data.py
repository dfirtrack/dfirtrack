from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger, critical_logger
from dfirtrack_main.models import Analysisstatus, Dnsname, Domain, Location, Os, Reason, Serviceprovider, Systemstatus, Systemtype

def check_config(request):
    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_system_importer_file_csv = False

    # check CSV_HEADLINE for bool
    if not isinstance(dfirtrack_config.CSV_HEADLINE, bool):
        messages.error(request, "Deformed `CSV_HEADLINE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_HEADLINE deformed")
        stop_system_importer_file_csv = True

    # check CSV_SKIP_EXISTING_SYSTEM for bool
    if not isinstance(dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM, bool):
        messages.error(request, "Deformed `CSV_SKIP_EXISTING_SYSTEM` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_SKIP_EXISTING_SYSTEM deformed")
        stop_system_importer_file_csv = True

    # check CSV_COLUMN_SYSTEM for int
    if not isinstance(dfirtrack_config.CSV_COLUMN_SYSTEM, int):
        messages.error(request, "Deformed `CSV_COLUMN_SYSTEM` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEM deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_SYSTEMSTATUS for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS, bool):
        messages.error(request, "Deformed `CSV_CHOICE_SYSTEMSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_SYSTEMSTATUS deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_SYSTEMSTATUS for existence
    try:
        Systemstatus.objects.get(systemstatus_name = dfirtrack_config.CSV_DEFAULT_SYSTEMSTATUS)
    except Systemstatus.DoesNotExist:
        messages.warning(request, "Systemstatus with configured name does not exist. Check `dfirtrack.config` or create systemstatus!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV systemstatus for variable CSV_DEFAULT_SYSTEMSTATUS does not exist")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_ANALYSISSTATUS for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_ANALYSISSTATUS, bool):
        messages.error(request, "Deformed `CSV_CHOICE_ANALYSISSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_ANALYSISSTATUS deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_ANALYSISSTATUS (check only if CSV_CHOICE_ANALYSISSTATUS is True) for existence
    if dfirtrack_config.CSV_CHOICE_ANALYSISSTATUS:
        try:
            Analysisstatus.objects.get(analysisstatus_name = dfirtrack_config.CSV_DEFAULT_ANALYSISSTATUS)
        except Analysisstatus.DoesNotExist:
            messages.warning(request, "Analysisstatus with configured name does not exist. Check `dfirtrack.config` or create analysisstatus!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV analysisstatus for variable CSV_DEFAULT_ANALYSISSTATUS does not exist")
            stop_system_importer_file_csv = True

    # check CSV_CHOICE_REASON for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_REASON, bool):
        messages.error(request, "Deformed `CSV_CHOICE_REASON` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_REASON deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_IP for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_IP, bool):
        messages.error(request, "Deformed `CSV_CHOICE_IP` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_IP deformed")
        stop_system_importer_file_csv = True

    # check CSV_COLUMN_IP for int
    if not isinstance(dfirtrack_config.CSV_COLUMN_IP, int):
        messages.error(request, "Deformed `CSV_COLUMN_IP` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_IP deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_DOMAIN for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_DOMAIN, bool):
        messages.error(request, "Deformed `CSV_CHOICE_DOMAIN` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_DOMAIN deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_DNSNAME for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_DNSNAME, bool):
        messages.error(request, "Deformed `CSV_CHOICE_DNSNAME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_DNSNAME deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_SYSTEMTYPE for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_SYSTEMTYPE, bool):
        messages.error(request, "Deformed `CSV_CHOICE_SYSTEMTYPE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_SYSTEMTYPE deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_OS for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_OS, bool):
        messages.error(request, "Deformed `CSV_CHOICE_OS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_OS deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_LOCATION for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_LOCATION, bool):
        messages.error(request, "Deformed `CSV_CHOICE_LOCATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_LOCATION deformed")
        stop_system_importer_file_csv = True

    # check CSV_CHOICE_SERVICEPROVIDER for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER, bool):
        messages.error(request, "Deformed `CSV_CHOICE_SERVICEPROVIDER` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_SERVICEPROVIDER deformed")
        stop_system_importer_file_csv = True

    # leave system_importer_file_csv if variables caused errors
    if stop_system_importer_file_csv:

        messages.warning(request, "Nothing was changed.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END_WITH_ERRORS")
        return stop_system_importer_file_csv

    else:
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
