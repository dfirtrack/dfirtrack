import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from dfirtrack_config.models import MainConfigModel, SystemImporterFileCsvCronbasedConfigModel
#from dfirtrack_main.importer.file.csv_check_data import check_config, check_file, check_row
#from dfirtrack_main.importer.file.csv_messages import final_messages
#from dfirtrack_main.importer.file.csv_set_system_attributes import case_attributes_config_based, company_attributes_config_based, ip_attributes, optional_system_attributes, tag_attributes_config_based
from dfirtrack_main.logger.default_logger import error_logger, info_logger
from dfirtrack_main.models import Case, Company, Dnsname, Domain, Location, Ip, Os, Reason, Recommendation, Serviceprovider, System, Systemtype
#from io import TextIOWrapper
import os

@login_required(login_url="/login")
def config_check(request):

    # reset stop condition
    stop_system_importer_file_csv_cronbased = False

    # get config model
    model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')

    """ check user """

    # check for csv_import_username (after initial migration w/o user defined) - stop immediately
    if not model.csv_import_username:
        messages.error(request, "No user for import defined. Check config!")
        # set stop condition
        stop_system_importer_file_csv_cronbased = True

    """ check file system """

    # build csv file path
    csv_path = model.csv_import_path + '/' + model.csv_import_filename

    # CSV import path does not exist - stop immediately
    if not os.path.isdir(model.csv_import_path):
        # call message
        messages.error(request, "CSV import path does not exist. Check config or file system!")
        # set stop condition
        stop_system_importer_file_csv_cronbased = True
    else:
        # no read permission for CSV import path - stop immediately
        if not os.access(model.csv_import_path, os.R_OK):
            # call message
            messages.error(request, "No read permission for CSV import path. Check config or file system!")
            # set stop condition
            stop_system_importer_file_csv_cronbased = True
        else:
            # CSV import file does not exist - stop immediately
            if not os.path.isfile(csv_path):
                # call message
                messages.error(request, "CSV import file does not exist. Check config or provide file!")
                # set stop condition
                stop_system_importer_file_csv_cronbased = True
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_path, os.R_OK):
                    # call message
                    messages.error(request, "No read permission for CSV import file. Check config or file system!")
                    # set stop condition
                    stop_system_importer_file_csv_cronbased = True

    # check stop condition
    if stop_system_importer_file_csv_cronbased:
        # return to system list
        return redirect(reverse('system_list'))
    else:
        # TODO: build url with python
        # TODO: open in new tab
        # open django admin with pre-filled form for scheduled task
        return redirect('/admin/django_q/schedule/add/?name=system_importer_file_csv_cron_based&func=dfirtrack_main.importer.file.csv_cron_based.system')

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

def add_fk_attributes(system, system_created, model, row):
    """ add foreign key relationships to system """

    """ systemstatus """

    # set systemstatus for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_systemstatus):

        # set systemstatus for system
        system.systemstatus = model.csv_default_systemstatus

    """ analysisstatus """

    # set analysisstatus for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_analysisstatus):

        # set analysisstatus for system
        system.analysisstatus = model.csv_default_analysisstatus

# TODO: add checks for content of 'csv_column_...'
# TODO: do something like: 'try: ...get_or_create(...)'

# TODO: not forget the logger and / or message

    """ dnsname """

    # set dnsname for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_dnsname):
        # get dnsname from CSV
        if model.csv_choice_dnsname:
            # get dnsname from CSV column
            dnsname_name = row[model.csv_column_dnsname - 1]
            # check for empty string
            if dnsname_name:
                # get or create dnsname
                dnsname, created = Dnsname.objects.get_or_create(dnsname_name = dnsname_name)
                # call logger if created
                if created:
                    dnsname.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_DNSNAME_CREATED")
            else:
                # set empty value (field is empty)
                dnsname = None
        # get dnsname from DB
        elif model.csv_default_dnsname:
            dnsname = model.csv_default_dnsname
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            dnsname = None
        # set dnsname for system
        system.dnsname = dnsname

    """ domain """

    # set domain for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_domain):
        # get domain from CSV
        if model.csv_choice_domain:
            # get domain from CSV column
            domain_name = row[model.csv_column_domain - 1]
            # check for empty string and compare to system name (when queried with local account, hostname is returned under some circumstances depending on tool)
            if domain_name and domain_name != system.system_name:
                # get or create domain
                domain, created = Domain.objects.get_or_create(domain_name = domain_name)
                # call logger if created
                if created:
                    domain.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_DOMAIN_CREATED")
            else:
                # set empty value (field is empty)
                domain = None
        # get domain from DB
        elif model.csv_default_domain:
            domain = model.csv_default_domain
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            domain = None
        # set domain for system
        system.domain = domain

    """ location """

    # set location for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_location):
        # get location from CSV
        if model.csv_choice_location:
            # get location from CSV column
            location_name = row[model.csv_column_location - 1]
            # check for empty string
            if location_name:
                # get or create location
                location, created = Location.objects.get_or_create(location_name = location_name)
                # call logger if created
                if created:
                    location.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_LOCATION_CREATED")
            else:
                # set empty value (field is empty)
                location = None
        # get location from DB
        elif model.csv_default_location:
            location = model.csv_default_location
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            location = None
        # set location for system
        system.location = location

    """ os """

    # set os for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_os):
        # get os from CSV
        if model.csv_choice_os:
            # get os from CSV column
            os_name = row[model.csv_column_os - 1]
            # check for empty string
            if os_name:
                # get or create os
                os, created = Os.objects.get_or_create(os_name = os_name)
                # call logger if created
                if created:
                    os.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_OS_CREATED")
            else:
                # set empty value (field is empty)
                os = None
        # get os from DB
        elif model.csv_default_os:
            os = model.csv_default_os
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            os = None
        # set os for system
        system.os = os

    """ reason """

    # set reason for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_reason):
        # get reason from CSV
        if model.csv_choice_reason:
            # get reason from CSV column
            reason_name = row[model.csv_column_reason - 1]
            # check for empty string
            if reason_name:
                # get or create reason
                reason, created = Reason.objects.get_or_create(reason_name = reason_name)
                # call logger if created
                if created:
                    reason.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_REASON_CREATED")
            else:
                # set empty value (field is empty)
                reason = None
        # get reason from DB
        elif model.csv_default_reason:
            reason = model.csv_default_reason
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            reason = None
        # set reason for system
        system.reason = reason

    """ recommendation """

    # set recommendation for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_recommendation):
        # get recommendation from CSV
        if model.csv_choice_recommendation:
            # get recommendation from CSV column
            recommendation_name = row[model.csv_column_recommendation - 1]
            # check for empty string
            if recommendation_name:
                # get or create recommendation
                recommendation, created = Recommendation.objects.get_or_create(recommendation_name = recommendation_name)
                # call logger if created
                if created:
                    recommendation.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_RECOMMENDATION_CREATED")
            else:
                # set empty value (field is empty)
                recommendation = None
        # get recommendation from DB
        elif model.csv_default_recommendation:
            recommendation = model.csv_default_recommendation
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            recommendation = None
        # set recommendation for system
        system.recommendation = recommendation

    """ serviceprovider """

    # set serviceprovider for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_serviceprovider):
        # get serviceprovider from CSV
        if model.csv_choice_serviceprovider:
            # get serviceprovider from CSV column
            serviceprovider_name = row[model.csv_column_serviceprovider - 1]
            # check for empty string
            if serviceprovider_name:
                # get or create serviceprovider
                serviceprovider, created = Serviceprovider.objects.get_or_create(serviceprovider_name = serviceprovider_name)
                # call logger if created
                if created:
                    serviceprovider.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_SERVICEPROVIDER_CREATED")
            else:
                # set empty value (field is empty)
                serviceprovider = None
        # get serviceprovider from DB
        elif model.csv_default_serviceprovider:
            serviceprovider = model.csv_default_serviceprovider
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            serviceprovider = None
        # set serviceprovider for system
        system.serviceprovider = serviceprovider

    """ systemtype """

    # set systemtype for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_systemtype):
        # get systemtype from CSV
        if model.csv_choice_systemtype:
            # get systemtype from CSV column
            systemtype_name = row[model.csv_column_systemtype - 1]
            # check for empty string
            if systemtype_name:
                # get or create systemtype
                systemtype, created = Systemtype.objects.get_or_create(systemtype_name = systemtype_name)
                # call logger if created
                if created:
                    systemtype.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_SYSTEMTYPE_CREATED")
            else:
                # set empty value (field is empty)
                systemtype = None
        # get systemtype from DB
        elif model.csv_default_systemtype:
            systemtype = model.csv_default_systemtype
        # set empty value (removes for existing system if neither CSV nor DB is chosen, does nothing for new system)
        else:
            systemtype = None
        # set systemtype for system
        system.systemtype = systemtype

    # return system with foreign key relations
    return system

def add_many2many_attributes(system, system_created, model, row):
    """ add many2many relationships to system """

    """ IP addresses """

# TODO: add check for IP (used somewhere else)
# TODO: what does 'system.ip.clear()' do with existing system without IPs?

    # add ips for new system or change if remove old is set
    if system_created or (not system_created and model.csv_remove_ip):
        # remove ips if not new system
        if not system_created:
            # remove all IPs
            system.ip.clear()
        # get IPs from CSV
        if model.csv_choice_ip:
            # get ip string
            ip_string = row[model.csv_column_ip - 1]
            # check for empty string
            if ip_string:
                # get IP delimiter from config
                if model.csv_ip_delimiter == 'ip_comma':
                    ip_delimiter = ','
                elif model.csv_ip_delimiter == 'ip_semicolon':
                    ip_delimiter = ';'
                elif model.csv_ip_delimiter == 'ip_space':
                    ip_delimiter = ' '
                # split ip string to list depending on delimiter
                ip_list = ip_string.split(ip_delimiter)
                # iterate over list elements
                for ip_ip in ip_list:
                    # get or create ip
                    ip, created = Ip.objects.get_or_create(ip_ip = ip_ip)
                    # call logger if created
                    if created:
                        ip.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_IP_CREATED")
                    # add ip to system
                    system.ip.add(ip)

    """ case """

#    # set case for new system or change if remove old is set
#    if system_created or (not system_created and model.csv_remove_case):
#        # remove cases if not new system
#        if not system_created:
#            # remove all cases
#            system.case.clear()
#        # get case from CSV
#        if model.csv_choice_case:
#            # get case from CSV column
#            case_name = row[model.csv_column_case - 1]
#            # check for empty string
#            if case_name:
#                # get or create case
#                case, created = Case.objects.get_or_create(case_name = case_name)
#                # call logger if created
#                if created:
#                    case.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_CASE_CREATED")
#                # set case for system
#                system.case.add(case)
#        # get case from DB
#        elif model.csv_default_case:
#            # TODO: does this work?
#            cases = model.csv_default_case
#            for case in cases:
#                # add case to system
#                system.case.add(case)

    """ company """

#    # set company for new system or change if remove old is set
#    if system_created or (not system_created and model.csv_remove_company):
#        # remove companies if not new system
#        if not system_created:
#            # remove all companies
#            system.company.clear()
#        # get company from CSV
#        if model.csv_choice_company:
#            # get company from CSV column
#            company_name = row[model.csv_column_company - 1]
#            # check for empty string
#            if company_name:
#                # get or create company
#                company, created = Company.objects.get_or_create(company_name = company_name)
#                # call logger if created
#                if created:
#                    company.logger(model.csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_COMPANY_CREATED")
#                # set company for system
#                system.company.add(company)
#        # get company from DB
#        elif model.csv_default_company:
#            # TODO: does this work?
#            companys = model.csv_default_company
#            for company in companys:
#                # add company to system
#                system.company.add(company)

# TODO: add tag with prefix and so on

    # return system with many2many relations
    return system

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

def system():

#LOCK_ANALYSISSTATUS = 'LOCK_ANALYSISSTATUS'
#LOCK_SYSTEMSTATUS = 'LOCK_SYSTEMSTATUS'

    # get config model
    model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')

    """ check user """

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

    # build csv file path
    csv_path = model.csv_import_path + '/' + model.csv_import_filename

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
            if not os.path.isfile(csv_path):
                # call message
                error_logger(csv_import_username.username, " SYSTEM_IMPORTER_FILE_CSV_CRON_FILE_NOT_EXISTING")
                # leave function
                return
            else:
                # no read permission for CSV import file - stop immediately
                if not os.access(csv_path, os.R_OK):
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

######################################################


# deprecated, TODO: check for useful stuff regarding tag handling
#
#from dfirtrack.config import TAGLIST
#from dfirtrack.config import TAGPREFIX
#
#    """
#    - remove all tags for systems beginning with 'TAGPREFIX' (if there are any)
#    - evaluate given CSV line by line (without first row)
#        - check whether this line has relevant tags (leave loop if not)
#        - add relevant tags to this system
#    """
#
#        # check TAGLIST (from settings.config) for empty list
#        if not TAGLIST:
#            messages.error(request, "No relevant tags defined. Check `TAGLIST` in `dfirtrack.config`!")
#            # call logger
#            error_logger(str(request.user), " SYSTEM_TAG_IMPORTER_NO_TAGS_DEFINED.")
#            return redirect('/system/')
#        else:
#            taglist = TAGLIST
#
#        # check TAGPREFIX (from settings.config) for empty string
#        if TAGPREFIX is "":
#            messages.error(request, "No prefix string defined. Check `TAGPREFIX` in `dfirtrack.config`!")
#            # call logger
#            error_logger(str(request.user), " SYSTEM_TAG_IMPORTER_NO_TAGPREFIX_DEFINED.")
#            return redirect('/system/')
#        # expand the string by an underscore
#        else:
##            tagprefix = TAGPREFIX + "_"
#            tagprefix = TAGPREFIX + "-"
#
#        # create tagaddlist to append for every new system
#        tagaddlist = []
#        for tag in taglist:
#                tagaddlist.append(tagprefix + tag)
#
#        """ remove all tags for systems beginning with 'TAGPREFIX' (if there are any) """
#
#        # get all systems that have tags beginning with 'TAGPREFIX' | prefixtagsystems -> queryset
#        prefixtagsystems=System.objects.filter(tag__tag_name__startswith=tagprefix)
#
#        # iterate over systems in queryset | prefixtagsystem  -> system object
#        for prefixtagsystem in prefixtagsystems:
#
#            # get all tags beginning with 'TAGPREFIX' that belong to the actual system | systemprefixtags -> queryset
#            systemprefixtags=prefixtagsystem.tag.filter(tag_name__startswith=tagprefix)
#
#            # iterate over queryset | systemprefixtag -> tag object
#            for systemprefixtag in systemprefixtags:
#                # delete all existing tags (the m2m relationship) beginning with 'TAGPREFIX' for this system (so that removed tags from csv will be removed as well)
#                systemprefixtag.system_set.remove(prefixtagsystem)
#
#            # get tags from csv
#            tagcsvstring = row[9]
#            if tagcsvstring == '':
#                # autoincrement systems_skipped_counter
#                systems_skipped_counter += 1
#                # autoincrement row_counter
#                row_counter += 1
#                # leave because systems without tags are not relevant
#                continue
#            else:
#                # convert string (at whitespaces) to list
#                tagcsvlist = tagcsvstring.split()
#
#            # create empty list for mapping
#            tagaddlist = []
#            # check for relevant tags and add to list
#            for tag in taglist:
#                if tag in tagcsvlist:
#                    tagaddlist.append(tagprefix + tag)
#
#            # check if tagaddlist is empty
#            if not tagaddlist:
#                # autoincrement systems_skipped_counter
#                systems_skipped_counter += 1
#                # autoincrement row_counter
#                row_counter += 1
#                # leave because there are no relevant tags
#                continue
#
#                if not row[10]:
#                    # continue if there is an empty string
#                    pass
#                else:
#                    # get object
#                    tag_error = Tag.objects.get(tag_name=tagprefix + 'Error')
#                    # add error tag to system
#                    tag_error.system_set.add(system)
#
#                # iterate over tags in tagaddlist
#                for tag_name in tagaddlist:
#                    # get object
#                    tag = Tag.objects.get(tag_name=tag_name)
#                    # add tag to system
#                    tag.system_set.add(system)
#                # get tagcolor object
#                tagcolor = Tagcolor.objects.get(tagcolor_name='primary')
#
#                # create tag if needed
#                tag, created = Tag.objects.get_or_create(tag_name=tag_name, tagcolor=tagcolor)
#                # call logger if created
#                if created == True:
#                    tag.logger(str(request.user), " SYSTEMS_TAG_IMPORTER_TAG_CREATED")
#                    messages.success(request, 'Tag "' + tag.tag_name + '" created.')
#
#                # add tag to system
#                tag.system_set.add(system)
