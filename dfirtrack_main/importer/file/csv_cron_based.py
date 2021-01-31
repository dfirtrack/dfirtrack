import csv
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from dfirtrack_config.models import MainConfigModel, SystemImporterFileCsvCronbasedConfigModel
#from dfirtrack_main.importer.file.csv_check_data import check_config, check_file, check_row
#from dfirtrack_main.importer.file.csv_messages import final_messages
#from dfirtrack_main.importer.file.csv_set_system_attributes import case_attributes_config_based, company_attributes_config_based, ip_attributes, optional_system_attributes, tag_attributes_config_based
from dfirtrack_main.importer.file.csv_add_attributes import add_fk_attributes, add_many2many_attributes
from dfirtrack_main.logger.default_logger import error_logger, info_logger
from dfirtrack_main.models import System
#from io import TextIOWrapper
import os

# TODO: check old snippets

# TODO: useful?
#            # check file for csv respectively some kind of text file
#            file_check = check_file(request, rows)
#
#            # leave system_importer_file_csv if file check throws errors
#            if not file_check:
#                return redirect(reverse('system_list'))
#            # jump to begin of file again after iterating in file check
#            systemcsv.seek(0)

# TODO: useful?
#                # check row for valid system values
#                continue_system_importer_file_csv = check_row(request, row, row_counter, model)
#                # leave loop for this row if there are invalid values
#                if continue_system_importer_file_csv:
#                    # autoincrement row counter
#                    row_counter += 1
#                    continue

# TODO: useful?
#        # call final messages
#        final_messages(request, systems_created_counter, systems_updated_counter, systems_skipped_counter)
#
#        # call logger
#        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END")

#def create_attributes(csv_import_username):
#
#    """ get tags """
#
#    # get tagcolor
#    tagcolor_white = Tagcolor.objects.get(tagcolor_name = 'white')
#
#    # get or create lock analysisstatus tag
#    tag_lock_analysisstatus, created = Tag.objects.get_or_create(
#        tag_name = LOCK_ANALYSISSTATUS,
#        tagcolor = tagcolor_white,
#    )
#    # call logger
#    if created:
#        tag_lock_analysisstatus.logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_TAG_CREATED")
#
#    # get or create lock systemstatus tag
#    tag_lock_systemstatus, created = Tag.objects.get_or_create(
#        tag_name = LOCK_SYSTEMSTATUS,
#        tagcolor = tagcolor_white,
#    )
#    # call logger
#    if created:
#        tag_lock_systemstatus.logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_TAG_CREATED")

#def set_status(system, row):
#
#    """ set automatic systemstatus here depending on tags """
#
##    # existing tags from CSV leads to 'IOCs checked', manually swiching to 'Analysis ongoing' necessary
##    if row[CSV_COLUMN_TAGS]:
##        analysisstatus = Analysisstatus.objects.get(analysisstatus_name = 'Needs analysis')
##        systemstatus = Systemstatus.objects.get(systemstatus_name = 'IOCs checked')
##
##    # no tags from CSV leads to 'IOCs checked'
##    # TODO: with finalization baselining systemstatus needs to be switched from 'IOCs checked' to 'Clean'
##    else:
##        analysisstatus = Analysisstatus.objects.get(analysisstatus_name = 'Nothing to do')
##        systemstatus = Systemstatus.objects.get(systemstatus_name = 'IOCs checked')
##
##    # exception: tag 'FOOBAR_INBOX_INTERN' or 'FOOBAR_REQUESTED_INTERN' discards previous checks and leads to 'Analysis ongoing'
##    if 'FOOBAR_INBOX_INTERN' in row[CSV_COLUMN_TAGS]:
##        analysisstatus = Analysisstatus.objects.get(analysisstatus_name = 'Needs analysis')
##        systemstatus = Systemstatus.objects.get(systemstatus_name = 'Analysis ongoing')
##
##    # exception: tag 'FOOBAR_INBOX_INTERN' or 'FOOBAR_REQUESTED_INTERN' discards previous checks and leads to 'Analysis ongoing'
##    if 'FOOBAR_REQUESTED_INTERN' in row[CSV_COLUMN_TAGS]:
##        analysisstatus = Analysisstatus.objects.get(analysisstatus_name = 'Needs analysis')
##        systemstatus = Systemstatus.objects.get(systemstatus_name = 'Analysis ongoing')
#
#    # get default status
#    analysisstatus = Analysisstatus.objects.get(analysisstatus_name = '10_needs_analysis')
#    systemstatus = Systemstatus.objects.get(systemstatus_name = '10_unknown')
#
#    # get lockstatus
#    tag_lock_analysisstatus = Tag.objects.get(tag_name = 'LOCK_ANALYSISSTATUS')
#    tag_lock_systemstatus = Tag.objects.get(tag_name = 'LOCK_SYSTEMSTATUS')
#
#    # change status if not locked (only applicable for existing systems)
#    if system.system_id:
#        if tag_lock_analysisstatus not in system.tag.all():
#            system.analysisstatus = analysisstatus
#        if tag_lock_systemstatus not in system.tag.all():
#            system.systemstatus = systemstatus
#    else:
#        system.analysisstatus = analysisstatus
#        system.systemstatus = systemstatus
#
#    return system

# TODO: remove optional argument used for debugging
def system(request=None):

#LOCK_ANALYSISSTATUS = 'LOCK_ANALYSISSTATUS'
#LOCK_SYSTEMSTATUS = 'LOCK_SYSTEMSTATUS'

    # get config model
    model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')

    """ check user """

# TODO: move to config check

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        # get main config model
        mainconfigmodel = MainConfigModel.objects.get(main_config_name = 'MainConfig')
        # get cron username from main config (needed for logger if no user was defined in the proper config)
        cron_username = mainconfigmodel.cron_username
        # call logger
        error_logger(cron_username, " SYSTEM_IMPORTER_FILE_CSV_CRON_NO_USER_DEFINED")
        # leave function
        return

    # get user
    csv_import_username = model.csv_import_username

    # call logger
    info_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_BEGAN")

    """ check file system """

# TODO: move to config check

    # build csv file path
    csv_import_file = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # call message
        error_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NOT_EXISTING")
        # leave function
        return
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # call message
            error_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_PATH_NO_READ_PERMISSION")
            # leave function
            return
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_import_file):
                # call message
                error_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NOT_EXISTING")
                # leave function
                return
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_import_file, os.R_OK):
                    # call message
                    error_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NO_READ_PERMISSION")
                    # leave function
                    return

#    """ get attributes """
#
#    # create attributes
#    create_attributes(csv_import_username)

    """ file handling  """

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

        """ skip headline if necessary """

        # check for first row and headline condition
        if row_counter == 1 and model.csv_headline:
            # autoincrement row counter
            row_counter += 1
            # leave loop for headline row
            continue

        # get system name (for domain name comparison)
        system_name = row[model.csv_column_system - 1]

        """ filter for systems """

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

# TODO: check function
#            system = set_status(system, row)

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

            # TODO: add message

            # autoincrement systems_multiple_counter
            systems_multiple_counter += 1

            # call logger
            error_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_MULTIPLE_SYSTEMS " + "System:" + system_name)

        # if there is no system -> create system
        else:

            # create new system object
            system = System()

            # add system_name from csv
            system.system_name = system_name

# TODO: check function
#            system = set_status(system, row)

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

    # TODO: add message

    # call logger
    info_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_STATUS " + "created:" + str(systems_created_counter) + "|" + "updated:" + str(systems_updated_counter) + "|" + "skipped:" + str(systems_skipped_counter) + "|" + "multiple:" + str(systems_multiple_counter))
    info_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_END")

    # TODO: remove optional argument used for debugging
    if request:
        return redirect(reverse('system_list'))
