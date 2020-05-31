import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
import dfirtrack.config as dfirtrack_config
from .csv_check_data import check_config, check_file, check_row
from .csv_importer_forms import SystemImporterFileCsv
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import Analysisstatus, Case, Company, Dnsname, Domain, Ip, Location, Os, Reason, Serviceprovider, System, Systemstatus, Systemtype, Tag, Tagcolor
import ipaddress
from io import TextIOWrapper

def check_and_create_case(case, request):

    # create case
    case, created = Case.objects.get_or_create(
        case_name = case,
        case_is_incident = dfirtrack_config.CSV_INCIDENT_CASE,
        case_created_by_user_id = request.user,
    )
    if created == True:
        case.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_CASE_CREATED")

    return case

def check_and_create_company(company, request):

    # create company
    company, created = Company.objects.get_or_create(company_name=company)
    if created == True:
        company.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_COMPANY_CREATED")

    return company

def check_and_create_ip(column_ip, request, row_counter):

    # check ip column for ip
    try:
        ipaddress.ip_address(column_ip)
    except ValueError:
        messages.error(request, "Value for ip address in row " + str(row_counter) + " was not a valid IP address.")
        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_IP_COLUMN " + "row_" + str(row_counter) + ":invalid_ip")
        return None

    # create ip
    ip, created = Ip.objects.get_or_create(ip_ip=column_ip)
    if created == True:
        ip.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_IP_CREATED")

    return ip

def check_and_create_tag(tag, request):

    # get tagcolor
    tagcolor = Tagcolor.objects.get(tagcolor_name='primary')
    # create tag
    tag, created = Tag.objects.get_or_create(tag_name=tag, tagcolor=tagcolor)
    if created == True:
        tag.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_TAG_CREATED")

    return tag

def optional_system_attributes(system, request):
    """ system attributes are set depending on dfirtrack.config """

    # add or change attributes (if set via dfirtrack.config)

    # systemstatus
    if dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS:
        system.systemstatus = Systemstatus.objects.get(systemstatus_name = dfirtrack_config.CSV_DEFAULT_SYSTEMSTATUS)
    # analysisstatus
    if dfirtrack_config.CSV_CHOICE_ANALYSISSTATUS:
        system.analysisstatus = Analysisstatus.objects.get(analysisstatus_name = dfirtrack_config.CSV_DEFAULT_ANALYSISSTATUS)
    # reason
    if dfirtrack_config.CSV_CHOICE_REASON:
        system.reason, created = Reason.objects.get_or_create(reason_name = dfirtrack_config.CSV_DEFAULT_REASON)
        if created == True:
            system.reason.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_REASON_CREATED")
    # domain
    if dfirtrack_config.CSV_CHOICE_DOMAIN:
        system.domain, created = Domain.objects.get_or_create(domain_name = dfirtrack_config.CSV_DEFAULT_DOMAIN)
        if created == True:
            system.domain.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_DOMAIN_CREATED")
    # dnsname
    if dfirtrack_config.CSV_CHOICE_DNSNAME:
        system.dnsname, created = Dnsname.objects.get_or_create(dnsname_name = dfirtrack_config.CSV_DEFAULT_DNSNAME)
        if created == True:
            system.dnsname.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_DNSNAME_CREATED")
    # systemtype
    if dfirtrack_config.CSV_CHOICE_SYSTEMTYPE:
        system.systemtype, created = Systemtype.objects.get_or_create(systemtype_name = dfirtrack_config.CSV_DEFAULT_SYSTEMTYPE)
        if created == True:
            system.systemtype.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEMTYPE_CREATED")
    # os
    if dfirtrack_config.CSV_CHOICE_OS:
        system.os, created = Os.objects.get_or_create(os_name = dfirtrack_config.CSV_DEFAULT_OS)
        if created == True:
            system.os.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_OS_CREATED")
    # location
    if dfirtrack_config.CSV_CHOICE_LOCATION:
        system.location, created = Location.objects.get_or_create(location_name = dfirtrack_config.CSV_DEFAULT_LOCATION)
        if created == True:
            system.location.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_LOCATION_CREATED")
    # serviceprovider
    if dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER:
        system.serviceprovider, created = Serviceprovider.objects.get_or_create(serviceprovider_name = dfirtrack_config.CSV_DEFAULT_SERVICEPROVIDER)
        if created == True:
            system.serviceprovider.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SERVICEPROVIDER_CREATED")

    # return system object enriched with attributes
    return system

@login_required(login_url="/login")
def system(request):

    # form was valid to post
    if request.method == "POST":

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_BEGAN")

        if dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS:
            """
            set dummy value for 'systemstatus' because this field has 'blank=False' in dfirtrack_main.models
            because dfirtrack_main.importer.file.csv_importer_forms.SystemImporterFileCsv is a ModelForm it relies on the attributes of dfirtrack_main.models
            changing blank would require extensive changes throughout the code
            """

            # TODO: change the following behavior

            # copy request object because object self is immutable
            request_post = request.POST.copy()
            # set dummy value (not used in the further course)
            request_post.update({'systemstatus': 1})

        # get text out of file (variable results from request object via file upload field)
        systemcsv = TextIOWrapper(request.FILES['systemcsv'].file, encoding=request.encoding)

        # read rows out of csv
        rows = csv.reader(systemcsv, quotechar="'")

        # check file for csv respectively some kind of text file
        file_check = check_file(request, rows)
        # leave system_importer_file_csv if file check throws errors
        if not file_check:
            return redirect(reverse('system_list'))
        # jump to begin of file again after iterating in file check
        systemcsv.seek(0)

        """ prepare and start loop """

        # set row_counter (needed for logger)
        row_counter = 1

        # set systems_created_counter (needed for messages)
        systems_created_counter = 0

        # set systems_updated_counter (needed for messages)
        systems_updated_counter = 0

        # set systems_skipped_counter (needed for messages)
        systems_skipped_counter = 0

        # iterate over rows
        for row in rows:

            # skip first row in case of headline
            if row_counter == 1 and dfirtrack_config.CSV_HEADLINE is True:
                # autoincrement row counter
                row_counter += 1
                # leave loop for headline row
                continue

            # check row for valid values
            continue_system_importer_file_csv = check_row(request, row, row_counter)
            # leave loop for this row if there are invalid values
            if continue_system_importer_file_csv:
                # autoincrement row counter
                row_counter += 1
                continue

            # get system name
            system_name = row[dfirtrack_config.CSV_COLUMN_SYSTEM]

            # get all systems with this system_name
            systemquery = System.objects.filter(system_name=system_name)

            """ check how many systems were returned """

            # if there is only one system
            if len(systemquery) == 1:

                # skip if system already exists (depending on CSV_SKIP_EXISTING_SYSTEM)
                if dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM:

                    # autoincrement counter
                    systems_skipped_counter += 1
                    # autoincrement row counter
                    row_counter += 1
                    # leave loop
                    continue

                # modify existing system (depending on CSV_SKIP_EXISTING_SYSTEM)
                elif not dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM:

                    # get existing system object
                    system = System.objects.get(system_name=system_name)

                    # create form with request data
                    if dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS:
                        form = SystemImporterFileCsv(request_post, request.FILES, instance=system)
                    else:
                        form = SystemImporterFileCsv(request.POST, request.FILES, instance=system)

                    # change system
                    if form.is_valid():

                        # don't save form yet
                        system = form.save(commit=False)

                        # change attributes (if set via dfirtrack.config)
                        system = optional_system_attributes(system, request)

                        # change mandatory meta attributes
                        system.system_modify_time = timezone.now()
                        system.system_modified_by_user_id = request.user

                        # save object
                        system.save()

                        # save many to many
                        form.save_m2m()

                        # handle case many to many relationship
                        if dfirtrack_config.CSV_CHOICE_CASE:

                            # remove existing companies (not relevant for newly created systems in condition below)
                            # also not relevant in case of CSV_CHOICE_CASE is False because it is changed via form either way
                            if dfirtrack_config.CSV_REMOVE_CASE:
                                # remove many to many relation between system and case without deleting existing case objects (important if other systems have the same companies)
                                system.case.clear()

                            # iterate through caselist from dfirtrack.config
                            for case in dfirtrack_config.CSV_DEFAULT_CASE:
                                # get or create case
                                newcase = check_and_create_case(case, request)
                                # add case
                                system.case.add(newcase)

                        # handle company many to many relationship
                        if dfirtrack_config.CSV_CHOICE_COMPANY:

                            # remove existing companies (not relevant for newly created systems in condition below)
                            # also not relevant in case of CSV_CHOICE_COMPANY is False because it is changed via form either way
                            if dfirtrack_config.CSV_REMOVE_COMPANY:
                                # remove many to many relation between system and company without deleting existing company objects (important if other systems have the same companies)
                                system.company.clear()

                            # iterate through companylist from dfirtrack.config
                            for company in dfirtrack_config.CSV_DEFAULT_COMPANY:
                                # get or create company
                                newcompany = check_and_create_company(company, request)
                                # add company
                                system.company.add(newcompany)

                        # handle ip address many to many relationship
                        if dfirtrack_config.CSV_CHOICE_IP:

                            # remove existing IP address / addresses for this system (not relevant for newly created systems in condition below)
                            # existing IP addresses will be left if nothing is provided by CSV
                            if dfirtrack_config.CSV_REMOVE_IP:
                                # remove many to many relation between system and ip without deleting existing ip objects (important if other systems have the same IP address)
                                system.ip.clear()

                            # get ip address from CSV
                            column_ip = row[dfirtrack_config.CSV_COLUMN_IP]
                            # check and create ip address
                            ip_address = check_and_create_ip(column_ip, request, row_counter)
                            # add ip address
                            if ip_address:
                                system.ip.add(ip_address)

                        # handle tag many to many relationship
                        if dfirtrack_config.CSV_CHOICE_TAG:

                            # remove existing tags (not relevant for newly created systems in condition below)
                            # also not relevant in case of CSV_CHOICE_TAG is False because it is changed via form either way
                            if dfirtrack_config.CSV_REMOVE_TAG:
                                # remove many to many relation between system and tag without deleting existing tag objects (important if other systems have the same tags)
                                system.tag.clear()

                            # iterate through taglist from dfirtrack.config
                            for tag in dfirtrack_config.CSV_DEFAULT_TAG:
                                # get or create tag
                                newtag = check_and_create_tag(tag, request)
                                # add tag
                                system.tag.add(newtag)

                        # autoincrement systems_updated_counter
                        systems_updated_counter += 1

                        # call logger
                        system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_MODIFIED")

            # if there is more than one system
            elif len(systemquery) > 1:
                messages.error(request, "System " + system_name + " already exists multiple times. Nothing was changed for this system.")

            # if there is no system
            else:

                # create form with request data
                if dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS:
                    form = SystemImporterFileCsv(request_post, request.FILES)
                else:
                    form = SystemImporterFileCsv(request.POST, request.FILES)

                # create system
                if form.is_valid():

                    # create new system object
                    system = System()

                    # don't save form yet
                    system = form.save(commit=False)

                    # add system_name from csv
                    system.system_name = system_name

                    # add attributes (if set via dfirtrack.config)
                    system = optional_system_attributes(system, request)

                    # add mandatory meta attributes
                    system.system_modify_time = timezone.now()
                    system.system_created_by_user_id = request.user
                    system.system_modified_by_user_id = request.user

                    # save object
                    system.save()

                    # save many to many
                    form.save_m2m()

                    # handle case many to many relationship
                    if dfirtrack_config.CSV_CHOICE_CASE:

                        # CSV_REMOVE_CASE not relevant for newly created systems (in contrast to condition above)

                        # iterate through caselist from dfirtrack.config
                        for case in dfirtrack_config.CSV_DEFAULT_CASE:
                            # get or create case
                            newcase = check_and_create_case(case, request)
                            # add case
                            system.case.add(newcase)

                    # handle company many to many relationship
                    if dfirtrack_config.CSV_CHOICE_COMPANY:

                        # CSV_REMOVE_COMPANY not relevant for newly created systems (in contrast to condition above)

                        # iterate through companylist from dfirtrack.config
                        for company in dfirtrack_config.CSV_DEFAULT_COMPANY:
                            # get or create company
                            newcompany = check_and_create_company(company, request)
                            # add company
                            system.company.add(newcompany)

                    # handle ip address many to many relationship
                    if dfirtrack_config.CSV_CHOICE_IP:

                        # CSV_REMOVE_IP not relevant for newly created systems (in contrast to condition above)

                        # get ip address from CSV
                        column_ip = row[dfirtrack_config.CSV_COLUMN_IP]
                        # check and create ip address
                        ip_address = check_and_create_ip(column_ip, request, row_counter)
                        # add ip address
                        if ip_address:
                            system.ip.add(ip_address)

                    # handle tag many to many relationship
                    if dfirtrack_config.CSV_CHOICE_TAG:

                        # CSV_REMOVE_TAG not relevant for newly created systems (in contrast to condition above)

                        # iterate through taglist from dfirtrack.config
                        for tag in dfirtrack_config.CSV_DEFAULT_TAG:
                            # get or create tag
                            newtag = check_and_create_tag(tag, request)
                            # add tag
                            system.tag.add(newtag)

                    # autoincrement systems_created_counter
                    systems_created_counter += 1

                    # call logger
                    system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_CREATED")

            # autoincrement row counter
            row_counter += 1

        # call final messages
        if systems_created_counter > 0:
            if systems_created_counter  == 1:
                messages.success(request, str(systems_created_counter) + ' system was created.')
            else:
                messages.success(request, str(systems_created_counter) + ' systems were created.')
        if systems_updated_counter > 0:
            if systems_updated_counter  == 1:
                messages.success(request, str(systems_updated_counter) + ' system was updated.')
            else:
                messages.success(request, str(systems_updated_counter) + ' systems were updated.')
        if systems_skipped_counter > 0:
            if systems_skipped_counter  == 1:
                messages.warning(request, str(systems_skipped_counter) + ' system was skipped.')
            else:
                messages.warning(request, str(systems_skipped_counter) + ' systems were skipped.')

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END")

        return redirect(reverse('system_list'))

    else:

        # check config before showing form
        stop_system_importer_file_csv = check_config(request)

        # leave system_importer_file_csv if variables caused errors
        if stop_system_importer_file_csv:
            return redirect(reverse('system_list'))

        # show warning if existing systems will be updated
        if not dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM:
            messages.warning(request, 'WARNING: Existing systems will be updated!')

        # show empty form with default values (if CSV_CHOICE_ANALYSISSTATUS or CSV_CHOICE_SYSTEMSTATUS is set to True in dfirtrack.config they are simply ignored)
        form = SystemImporterFileCsv(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_ENTERED")

    # show form and submit bools from dfirtrack.config needed as variables in template
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv.html',
        {
            'form': form,
            'csv_choice_systemstatus': dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS,
            'csv_choice_analysisstatus': dfirtrack_config.CSV_CHOICE_ANALYSISSTATUS,
            'csv_choice_reason': dfirtrack_config.CSV_CHOICE_REASON,
            'csv_choice_domain': dfirtrack_config.CSV_CHOICE_DOMAIN,
            'csv_choice_dnsname': dfirtrack_config.CSV_CHOICE_DNSNAME,
            'csv_choice_systemtype': dfirtrack_config.CSV_CHOICE_SYSTEMTYPE,
            'csv_choice_os': dfirtrack_config.CSV_CHOICE_OS,
            'csv_choice_location': dfirtrack_config.CSV_CHOICE_LOCATION,
            'csv_choice_serviceprovider': dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER,
            'csv_choice_case': dfirtrack_config.CSV_CHOICE_CASE,
            'csv_choice_company': dfirtrack_config.CSV_CHOICE_COMPANY,
            'csv_choice_tag': dfirtrack_config.CSV_CHOICE_TAG,
        }
    )


# TODO: check for useful stuff regarding tag handling
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
