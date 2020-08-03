from constance import config as constance_config
from django.contrib import messages
from dfirtrack_main.logger.default_logger import warning_logger
from dfirtrack_main.models import Analysisstatus, Case, Company, Dnsname, Domain, Ip, Location, Os, Reason, Serviceprovider, System, Systemstatus, Systemtype, Tag, Tagcolor
import ipaddress

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

def optional_system_attributes(system, request):
    """ system attributes are set depending on config """

    # add or change attributes (set via config)

    # systemstatus
    system.systemstatus = Systemstatus.objects.get(systemstatus_id = constance_config.CSV_DEFAULT_SYSTEMSTATUS)
    # analysisstatus
    system.analysisstatus = Analysisstatus.objects.get(analysisstatus_id = constance_config.CSV_DEFAULT_ANALYSISSTATUS)
    # reason (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_REASON:
        system.reason = Reason.objects.get(reason_id = constance_config.CSV_DEFAULT_REASON)
    # domain (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_DOMAIN:
        system.domain = Domain.objects.get(domain_id = constance_config.CSV_DEFAULT_DOMAIN)
    # dnsname (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_DNSNAME:
        system.dnsname = Dnsname.objects.get(dnsname_id = constance_config.CSV_DEFAULT_DNSNAME)
    # systemtype (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_SYSTEMTYPE:
        system.systemtype = Systemtype.objects.get(systemtype_id = constance_config.CSV_DEFAULT_SYSTEMTYPE)
    # os (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_OS:
        system.os = Os.objects.get(os_id = constance_config.CSV_DEFAULT_OS)
    # location (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_LOCATION:
        system.location = Location.objects.get(location_id = constance_config.CSV_DEFAULT_LOCATION)
    # serviceprovider (set only, if something was submitted)
    if constance_config.CSV_DEFAULT_SERVICEPROVIDER:
        system.serviceprovider = Serviceprovider.objects.get(serviceprovider_id = constance_config.CSV_DEFAULT_SERVICEPROVIDER)

    # return system object enriched with attributes
    return system

def case_attributes(system, request, caselist):

    # remove existing companies (not relevant for newly created systems)
    if constance_config.CSV_REMOVE_CASE:
        # remove many to many relation between system and case without deleting existing case objects (important if other systems have the same companies)
        system.case.clear()

    # iterate through caselist from config
    for case_id in caselist:
        # get or create case
        case = Case.objects.get(case_id = case_id)
        # add case
        system.case.add(case)

    # return system object enriched with attributes
    return system

def company_attributes(system, request, companylist):

    # remove existing companies (not relevant for newly created systems)
    if constance_config.CSV_REMOVE_COMPANY:
        # remove many to many relation between system and company without deleting existing company objects (important if other systems have the same companies)
        system.company.clear()

    # iterate through companylist from config
    for company_id in companylist:
        # get or create company
        company = Company.objects.get(company_id = company_id)
        # add company
        system.company.add(company)

    # return system object enriched with attributes
    return system

def tag_attributes(system, request, taglist):

    # remove existing tags (not relevant for newly created systems)
    if constance_config.CSV_REMOVE_TAG:
        # remove many to many relation between system and tag without deleting existing tag objects (important if other systems have the same tags)
        system.tag.clear()

    # iterate through taglist from config
    for tag_id in taglist:
        # get or create tag
        tag = Tag.objects.get(tag_id = tag_id)
        # add tag
        system.tag.add(tag)

    # return system object enriched with attributes
    return system

def ip_attributes(system, request, row, row_counter):
    """ IP addresses are set depending on config """

    # remove existing IP addresses for this system (not relevant for newly created systems)
    if constance_config.CSV_REMOVE_IP:
        # remove many to many relation between system and ip without deleting existing ip objects (important if other systems have the same IP address)
        system.ip.clear()

    # get ip address from CSV (decremented by one because index starts with zero: user provides 2 -> second column in CSV has index 1)
    column_ip = row[constance_config.CSV_COLUMN_IP - 1]
    # check and create ip address
    ip_address = check_and_create_ip(column_ip, request, row_counter)
    # add ip address
    if ip_address:
        system.ip.add(ip_address)

    # return system object enriched with IP
    return system
