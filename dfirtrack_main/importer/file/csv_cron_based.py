import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from dfirtrack_config.models import SystemImporterFileCsvCronbasedConfigModel
#from dfirtrack_main.importer.file.csv_check_data import check_config, check_file, check_row
from dfirtrack_main.importer.file.csv_add_attributes import add_fk_attributes, add_many2many_attributes, create_lock_tags
from dfirtrack_main.importer.file.csv_check_data import config_check_run, check_file
from dfirtrack_main.importer.file.csv_messages import final_messages
from dfirtrack_main.logger.default_logger import warning_logger, info_logger
from dfirtrack_main.models import System

def csv_import(request=None):

    # get config model
    model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')

    """ check config """

    # check user and file system
    stop_system_importer_file_csv_run = config_check_run(model)

    # call messages if function was called from 'system_instant' and 'system_upload'
    if stop_system_importer_file_csv_run and request:
        # call messages
        messages.error(request, "Config still contains errors. Check config!")
    # TODO: call messages if function was called from 'system_cron' for all users?
    elif stop_system_importer_file_csv_run and not request:
        pass

    # leave system_importer_file_csv if config caused errors
    if stop_system_importer_file_csv_run:
        # return to calling function
        return

    """ start system importer """

    # get user
    csv_import_username = model.csv_import_username

    # call logger
    info_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_BEGAN")

    # create lock tags
    create_lock_tags(model)

    """ file handling  """

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # get field delimiter from config
    if model.csv_field_delimiter == 'field_comma':
        delimiter = ','
    elif model.csv_field_delimiter == 'field_semicolon':
        delimiter = ';'

    # get text quotechar from config
    if model.csv_text_quote == 'text_double_quotation_marks':
        quotechar = '"'
    elif model.csv_text_quote == 'text_single_quotation_marks':
        quotechar = "'"

    # open file
    systemcsv = open(csv_import_file, 'r')

    # read rows out of csv
    rows = csv.reader(systemcsv, delimiter=delimiter, quotechar=quotechar)

    """ check file """

    # check file for csv respectively some kind of text file
    file_check = check_file(rows, csv_import_username.username)

    # call messages if function was called from 'system_instant' and 'system_upload'
    if not file_check and request:
        # call message
        messages.error(request, "File seems not to be a CSV file. Check file!")
    # TODO: call messages if function was called from 'system_cron' for all users?
    elif not file_check and not request:
        pass

    # leave system_importer_file_csv if file check throws errors
    if not file_check:
        # close file
        systemcsv.close()
        # return to calling function
        return

    # jump to begin of file again after iterating in file check
    systemcsv.seek(0)

    """ prepare and start loop """

    # set row_counter (needed for logger)
    row_counter = 1

    # set systems_created_counter (needed for logger)
    systems_created_counter = 0

    # set systems_updated_counter (needed for logger)
    systems_updated_counter = 0

    # set systems_multiple_counter (needed for logger)
    systems_multiple_counter = 0

    # set systems_skipped_counter (needed for logger)
    systems_skipped_counter = 0

    # iterate over rows
    for row in rows:

# TODO: useful?
#                # check row for valid system values
#                continue_system_importer_file_csv = check_row(request, row, row_counter, model)
#                # leave loop for this row if there are invalid values
#                if continue_system_importer_file_csv:
#                    # autoincrement row counter
#                    row_counter += 1
#                    continue

        """ skip headline if necessary """

        # check for first row and headline condition
        if row_counter == 1 and model.csv_headline:
            # autoincrement row counter
            row_counter += 1
            # leave loop for headline row
            continue

        """ filter for systems """

        # get system name (for domain name comparison)
        system_name = row[model.csv_column_system - 1]

# TODO: add option which attributes are used for filtering? (like domain, dnsname, company)
# e.g. 'csv_identification_dnsname'

        # get all systems
        systemquery = System.objects.filter(
            system_name = system_name,
#            dnsname = dnsname,
#            domain = domain,
        )

        """ check how many systems were returned """

        # if there is only one system -> modify system
        if len(systemquery) == 1:

            # skip if system already exists (depending on csv_skip_existing_system)
            if model.csv_skip_existing_system:

                # autoincrement counter
                systems_skipped_counter += 1
                # autoincrement row counter
                row_counter += 1
                # leave loop
                continue

# TODO: add option which attributes are used for filtering? (like domain, dnsname, company)
# e.g. 'csv_identification_dnsname'

            # get existing system object
            system = System.objects.get(
                system_name=system_name,
#                dnsname = dnsname,
#                domain = domain,
            )

            # change mandatory meta attributes
            system.system_modify_time = timezone.now()
            system.system_modified_by_user_id = csv_import_username

            # set value for already existing system (modify system)
            system_created = False

            # add foreign key relationships to system
            system = add_fk_attributes(system, system_created, model, row)

            # save object
            system.save()

            # add many2many relationships to system
            system = add_many2many_attributes(system, system_created, model, row)

            # autoincrement systems_updated_counter
            systems_updated_counter += 1

            # call logger
            system.logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_SYSTEM_MODIFIED")

        # if there is more than one system
        elif len(systemquery) > 1:

            # TODO: add list with system_name for message

            # autoincrement systems_multiple_counter
            systems_multiple_counter += 1

            # call logger
            warning_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_MULTIPLE_SYSTEMS " + "System:" + system_name)

        # if there is no system -> create system
        else:

            # create new system object
            system = System()

            # add system_name from csv
            system.system_name = system_name

            # add mandatory meta attributes
            system.system_modify_time = timezone.now()
            system.system_created_by_user_id = csv_import_username
            system.system_modified_by_user_id = csv_import_username

            # set value for new system (create system)
            system_created = True

            # add foreign key relationships to system
            system = add_fk_attributes(system, system_created, model, row)

            # save object
            system.save()

            # add many2many relationships to system
            system = add_many2many_attributes(system, system_created, model, row)

            # autoincrement systems_created_counter
            systems_created_counter += 1

            # call logger
            system.logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_SYSTEM_CREATED")

        # autoincrement row counter
        row_counter += 1

    # close file
    systemcsv.close()

    # call messages if function was called from 'system_instant' and 'system_upload'
    if request:
        # call final messages
        final_messages(request, systems_created_counter, systems_updated_counter, systems_skipped_counter, systems_multiple_counter)
    # TODO: call messages if function was called from 'system_cron' for all users?
    else:
        pass

    # call logger
    info_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_STATUS " + "created:" + str(systems_created_counter) + "|" + "updated:" + str(systems_updated_counter) + "|" + "skipped:" + str(systems_skipped_counter) + "|" + "multiple:" + str(systems_multiple_counter))
    info_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_END")

    # return to calling function
    return

@login_required(login_url="/login")
def system_instant(request):

    # TODO: change user for calling importer
    # call CSV importer
    csv_import(request)

    # return
    return redirect(reverse('system_list'))

def system_cron():

    # TODO: change user for calling importer
    # call CSV importer
    csv_import()

@login_required(login_url="/login")
def system_upload(request):

    # return
    return redirect(reverse('system_list'))
