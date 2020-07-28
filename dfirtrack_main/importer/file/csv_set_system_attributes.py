from django.contrib import messages
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import warning_logger
from dfirtrack_main.models import Analysisstatus, Case, Company, Dnsname, Domain, Ip, Location, Os, Reason, Serviceprovider, System, Systemstatus, Systemtype, Tag, Tagcolor
import ipaddress

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

    # check whether tag already exists (necessary, if tag exists with another tagcolor than default)
    tagquery = Tag.objects.filter(tag_name=tag)
    if len(tagquery) == 1:
        # get tag
        tag = Tag.objects.get(tag_name=tag)
    else:
        # get tagcolor
        tagcolor = Tagcolor.objects.get(tagcolor_name='primary')
        # create tag
        tag, created = Tag.objects.get_or_create(tag_name=tag, tagcolor=tagcolor)
        if created == True:
            tag.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_TAG_CREATED")

    return tag

def optional_system_attributes(system, request):
    """ system attributes are set depending on dfirtrack.config """

    # add or change attributes (set via dfirtrack.config)

    # systemstatus
    system.systemstatus = Systemstatus.objects.get(systemstatus_name = dfirtrack_config.CSV_DEFAULT_SYSTEMSTATUS)
    # analysisstatus
    system.analysisstatus = Analysisstatus.objects.get(analysisstatus_name = dfirtrack_config.CSV_DEFAULT_ANALYSISSTATUS)
    # reason
    if dfirtrack_config.CSV_DEFAULT_REASON:
        system.reason, created = Reason.objects.get_or_create(reason_name = dfirtrack_config.CSV_DEFAULT_REASON)
        if created == True:
            system.reason.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_REASON_CREATED")
    # domain (create only, if something was submitted)
    if dfirtrack_config.CSV_DEFAULT_DOMAIN:
        system.domain, created = Domain.objects.get_or_create(domain_name = dfirtrack_config.CSV_DEFAULT_DOMAIN)
        if created == True:
            system.domain.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_DOMAIN_CREATED")
    # dnsname (create only, if something was submitted)
    if dfirtrack_config.CSV_DEFAULT_DNSNAME:
        system.dnsname, created = Dnsname.objects.get_or_create(dnsname_name = dfirtrack_config.CSV_DEFAULT_DNSNAME)
        if created == True:
            system.dnsname.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_DNSNAME_CREATED")
    # systemtype (create only, if something was submitted)
    if dfirtrack_config.CSV_DEFAULT_SYSTEMTYPE:
        system.systemtype, created = Systemtype.objects.get_or_create(systemtype_name = dfirtrack_config.CSV_DEFAULT_SYSTEMTYPE)
        if created == True:
            system.systemtype.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEMTYPE_CREATED")
    # os (create only, if something was submitted)
    if dfirtrack_config.CSV_DEFAULT_OS:
        system.os, created = Os.objects.get_or_create(os_name = dfirtrack_config.CSV_DEFAULT_OS)
        if created == True:
            system.os.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_OS_CREATED")
    # location (create only, if something was submitted)
    if dfirtrack_config.CSV_DEFAULT_LOCATION:
        system.location, created = Location.objects.get_or_create(location_name = dfirtrack_config.CSV_DEFAULT_LOCATION)
        if created == True:
            system.location.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_LOCATION_CREATED")
    # serviceprovider (create only, if something was submitted)
    if dfirtrack_config.CSV_DEFAULT_SERVICEPROVIDER:
        system.serviceprovider, created = Serviceprovider.objects.get_or_create(serviceprovider_name = dfirtrack_config.CSV_DEFAULT_SERVICEPROVIDER)
        if created == True:
            system.serviceprovider.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SERVICEPROVIDER_CREATED")

    # return system object enriched with attributes
    return system

def many_to_many_system_attributes(system, request):
    """ many2many system attributes are set depending on dfirtrack.config """

    """ case """

    # remove existing companies (not relevant for newly created systems)
    if dfirtrack_config.CSV_REMOVE_CASE:
        # remove many to many relation between system and case without deleting existing case objects (important if other systems have the same companies)
        system.case.clear()
    
    # iterate through caselist from dfirtrack.config
    for case in dfirtrack_config.CSV_DEFAULT_CASE:
        # get or create case
        newcase = check_and_create_case(case, request)
        # add case
        system.case.add(newcase)

    """ company """

    # remove existing companies (not relevant for newly created systems)
    if dfirtrack_config.CSV_REMOVE_COMPANY:
        # remove many to many relation between system and company without deleting existing company objects (important if other systems have the same companies)
        system.company.clear()
    
    # iterate through companylist from dfirtrack.config
    for company in dfirtrack_config.CSV_DEFAULT_COMPANY:
        # get or create company
        newcompany = check_and_create_company(company, request)
        # add company
        system.company.add(newcompany)

    """ ip """

# TODO: make ip work again (arguments missing for check_and_create_ip())
#    # remove existing IP addresses for this system (not relevant for newly created systems)
#    if dfirtrack_config.CSV_REMOVE_IP:
#        # remove many to many relation between system and ip without deleting existing ip objects (important if other systems have the same IP address)
#        system.ip.clear()
#    
#    # get ip address from CSV
#    column_ip = row[dfirtrack_config.CSV_COLUMN_IP]
#    # check and create ip address
#    ip_address = check_and_create_ip(column_ip, request, row_counter)
#    # add ip address
#    if ip_address:
#        system.ip.add(ip_address)

    """ tag """
    
    # remove existing tags (not relevant for newly created systems)
    if dfirtrack_config.CSV_REMOVE_TAG:
        # remove many to many relation between system and tag without deleting existing tag objects (important if other systems have the same tags)
        system.tag.clear()

    # iterate through taglist from dfirtrack.config
    for tag in dfirtrack_config.CSV_DEFAULT_TAG:
        # get or create tag
        newtag = check_and_create_tag(tag, request)
        # add tag
        system.tag.add(newtag)

    # return system object enriched with attributes
    return system
