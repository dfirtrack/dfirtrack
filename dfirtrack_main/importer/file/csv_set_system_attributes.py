from django.contrib import messages
from dfirtrack_main.logger.default_logger import warning_logger
from dfirtrack_main.models import Case, Company, Ip, Tag
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

def optional_system_attributes(system, model):
    """ system attributes are set depending on config """

    # add or change attributes (set via config)

    # systemstatus
    system.systemstatus = model.csv_default_systemstatus
    # analysisstatus
    system.analysisstatus = model.csv_default_analysisstatus
    # reason (set only, if something was submitted)
    if model.csv_default_reason:
        system.reason = model.csv_default_reason
    # domain (set only, if something was submitted)
    if model.csv_default_domain:
        system.domain = model.csv_default_domain
    # dnsname (set only, if something was submitted)
    if model.csv_default_dnsname:
        system.dnsname = model.csv_default_dnsname
    # systemtype (set only, if something was submitted)
    if model.csv_default_systemtype:
        system.systemtype = model.csv_default_systemtype
    # os (set only, if something was submitted)
    if model.csv_default_os:
        system.os = model.csv_default_os
    # location (set only, if something was submitted)
    if model.csv_default_location:
        system.location = model.csv_default_location
    # serviceprovider (set only, if something was submitted)
    if model.csv_default_serviceprovider:
        system.serviceprovider = model.csv_default_serviceprovider

    # return system object enriched with attributes
    return system

def case_attributes_config_based(system, caselist, model):

    # remove existing cases (not relevant for newly created systems)
    if model.csv_remove_case:
        # remove many to many relation between system and case without deleting existing case objects (important if other systems have the same cases)
        system.case.clear()

    # iterate through caselist from config
    for case in caselist.all():
        # add case
        system.case.add(case)

    # return system object enriched with attributes
    return system

def case_attributes_form_based(system, caselist, model):

    # remove existing cases (not relevant for newly created systems)
    if model.csv_remove_case:
        # remove many to many relation between system and case without deleting existing case objects (important if other systems have the same cases)
        system.case.clear()

    # iterate through caselist from form
    for case_id in caselist:
        # get or create case
        case = Case.objects.get(case_id = case_id)
        # add case
        system.case.add(case)

    # return system object enriched with attributes
    return system

def company_attributes_config_based(system, companylist, model):

    # remove existing companies (not relevant for newly created systems)
    if model.csv_remove_company:
        # remove many to many relation between system and company without deleting existing company objects (important if other systems have the same companies)
        system.company.clear()

    # iterate through companylist from config
    for company in companylist.all():
        # add company
        system.company.add(company)

    # return system object enriched with attributes
    return system

def company_attributes_form_based(system, companylist, model):

    # remove existing companies (not relevant for newly created systems)
    if model.csv_remove_company:
        # remove many to many relation between system and company without deleting existing company objects (important if other systems have the same companies)
        system.company.clear()

    # iterate through companylist from form
    for company_id in companylist:
        # get or create company
        company = Company.objects.get(company_id = company_id)
        # add company
        system.company.add(company)

    # return system object enriched with attributes
    return system

def tag_attributes_config_based(system, taglist, model):

    # remove existing tags (not relevant for newly created systems)
    if model.csv_remove_tag:
        # remove many to many relation between system and tag without deleting existing tag objects (important if other systems have the same tags)
        system.tag.clear()

    # iterate through taglist from config
    for tag in taglist.all():
        # add tag
        system.tag.add(tag)

    # return system object enriched with attributes
    return system

def tag_attributes_form_based(system, taglist, model):

    # remove existing tags (not relevant for newly created systems)
    if model.csv_remove_tag:
        # remove many to many relation between system and tag without deleting existing tag objects (important if other systems have the same tags)
        system.tag.clear()

    # iterate through taglist from form
    for tag_id in taglist:
        # get or create tag
        tag = Tag.objects.get(tag_id = tag_id)
        # add tag
        system.tag.add(tag)

    # return system object enriched with attributes
    return system

def ip_attributes(system, request, row, row_counter, model):
    """ IP addresses are set depending on config """

    # remove existing IP addresses for this system (not relevant for newly created systems)
    if model.csv_remove_ip:
        # remove many to many relation between system and ip without deleting existing ip objects (important if other systems have the same IP address)
        system.ip.clear()

    # get ip address from CSV (decremented by one because index starts with zero: user provides 2 -> second column in CSV has index 1)
    column_ip = row[model.csv_column_ip - 1]
    # check and create ip address
    ip_address = check_and_create_ip(column_ip, request, row_counter)
    # add ip address
    if ip_address:
        system.ip.add(ip_address)

    # return system object enriched with IP
    return system
