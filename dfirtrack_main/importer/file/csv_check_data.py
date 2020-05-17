from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger, critical_logger
from dfirtrack_main.models import Analysisstatus, Dnsname, Domain, Location, Reason, Serviceprovider, Systemstatus, Systemtype

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

    # check CSV_DEFAULT_REASON (check only if CSV_CHOICE_REASON is True) for existence
    if dfirtrack_config.CSV_CHOICE_REASON:
        try:
            Reason.objects.get(reason_id = dfirtrack_config.CSV_DEFAULT_REASON)
        except Reason.DoesNotExist:
            messages.warning(request, "Reason with configured ID does not exist. Check `dfirtrack.config` or create reason!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV reason for variable CSV_DEFAULT_REASON does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_REASON` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_REASON deformed")
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

    # check CSV_DEFAULT_DOMAIN (check only if CSV_CHOICE_DOMAIN is True) for existence
    if dfirtrack_config.CSV_CHOICE_DOMAIN:
        try:
            Domain.objects.get(domain_id = dfirtrack_config.CSV_DEFAULT_DOMAIN)
        except Domain.DoesNotExist:
            messages.warning(request, "Domain with configured ID does not exist. Check `dfirtrack.config` or create domain!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV domain for variable CSV_DEFAULT_DOMAIN does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_DOMAIN` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_DOMAIN deformed")
            stop_system_importer_file_csv = True

    # check CSV_CHOICE_DNSNAME for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_DNSNAME, bool):
        messages.error(request, "Deformed `CSV_CHOICE_DNSNAME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_DNSNAME deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_DNSNAME (check only if CSV_CHOICE_DNSNAME is True) for existence
    if dfirtrack_config.CSV_CHOICE_DNSNAME:
        try:
            Dnsname.objects.get(dnsname_id = dfirtrack_config.CSV_DEFAULT_DNSNAME)
        except Dnsname.DoesNotExist:
            messages.warning(request, "Dnsname with configured ID does not exist. Check `dfirtrack.config` or create dnsname!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV dnsname for variable CSV_DEFAULT_DNSNAME does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_DNSNAME` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_DNSNAME deformed")
            stop_system_importer_file_csv = True

    # check CSV_CHOICE_SYSTEMTYPE for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_SYSTEMTYPE, bool):
        messages.error(request, "Deformed `CSV_CHOICE_SYSTEMTYPE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_SYSTEMTYPE deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_SYSTEMTYPE (check only if CSV_CHOICE_SYSTEMTYPE is True) for existence
    if dfirtrack_config.CSV_CHOICE_SYSTEMTYPE:
        try:
            Systemtype.objects.get(systemtype_id = dfirtrack_config.CSV_DEFAULT_SYSTEMTYPE)
        except Systemtype.DoesNotExist:
            messages.warning(request, "Systemtype with configured ID does not exist. Check `dfirtrack.config` or create systemtype!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV systemtype for variable CSV_DEFAULT_SYSTEMTYPE does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_SYSTEMTYPE` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_SYSTEMTYPE deformed")
            stop_system_importer_file_csv = True

    # check CSV_CHOICE_OS for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_OS, bool):
        messages.error(request, "Deformed `CSV_CHOICE_OS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_OS deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_OS (check only if CSV_CHOICE_OS is True) for existence
    if dfirtrack_config.CSV_CHOICE_OS:
        try:
            Os.objects.get(os_id = dfirtrack_config.CSV_DEFAULT_OS)
        except Os.DoesNotExist:
            messages.warning(request, "OS with configured ID does not exist. Check `dfirtrack.config` or create OS!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV OS for variable CSV_DEFAULT_OS does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_OS` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_OS deformed")
            stop_system_importer_file_csv = True

    # check CSV_CHOICE_LOCATION for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_LOCATION, bool):
        messages.error(request, "Deformed `CSV_CHOICE_LOCATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_LOCATION deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_LOCATION (check only if CSV_CHOICE_LOCATION is True) for existence
    if dfirtrack_config.CSV_CHOICE_LOCATION:
        try:
            Location.objects.get(location_id = dfirtrack_config.CSV_DEFAULT_LOCATION)
        except Location.DoesNotExist:
            messages.warning(request, "Location with configured ID does not exist. Check `dfirtrack.config` or create location!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV location for variable CSV_DEFAULT_LOCATION does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_LOCATION` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_LOCATION deformed")
            stop_system_importer_file_csv = True

    # check CSV_CHOICE_SERVICEPROVIDER for bool
    if not isinstance(dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER, bool):
        messages.error(request, "Deformed `CSV_CHOICE_SERVICEPROVIDER` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_CHOICE_SERVICEPROVIDER deformed")
        stop_system_importer_file_csv = True

    # check CSV_DEFAULT_SERVICEPROVIDER (check only if CSV_CHOICE_SERVICEPROVIDER is True) for existence
    if dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER:
        try:
            Serviceprovider.objects.get(serviceprovider_id = dfirtrack_config.CSV_DEFAULT_SERVICEPROVIDER)
        except Serviceprovider.DoesNotExist:
            messages.warning(request, "Serviceprovider with configured ID does not exist. Check `dfirtrack.config` or create serviceprovider!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV serviceprovider for variable CSV_DEFAULT_SERVICEPROVIDER does not exist")
            stop_system_importer_file_csv = True
        except ValueError:
            messages.error(request, "Deformed `CSV_DEFAULT_SERVICEPROVIDER` Check `dfirtrack.config`!")
            # call logger
            warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV variable CSV_DEFAULT_SERVICEPROVIDER deformed")
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
