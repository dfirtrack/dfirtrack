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

    # check CSV_COLUMN_SYSTEM for value
    if not 1<= constance_config.CSV_COLUMN_SYSTEM <= 256:
        messages.error(request, "`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_SYSTEM out of range")
        stop_system_importer_file_csv = True

    # check CSV_COLUMN_IP for value
    if not 1<= constance_config.CSV_COLUMN_IP <= 256:
        messages.error(request, "`CSV_COLUMN_IP` is outside the allowed range. Check config!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_COLUMN_IP out of range")
        stop_system_importer_file_csv = True

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
