from constance import config as constance_config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dfirtrack_main.logger.default_logger import info_logger
from dfirtrack_main.models import System
import csv
from time import strftime

@login_required(login_url="/login")
def system(request):

    """ prepare file """

    # create csv MIME type object
    sod = HttpResponse(content_type='text/csv')

    # define filename
    sod['Content-Disposition'] = 'attachment; filename="systems.csv"'

    # create file object for writing lines
    sod_writer = csv.writer(sod)

    """ start with headline """

    # create empty list
    headline = []

    # check for attribute id
    if constance_config.SPREAD_SYSTEM_ID:
        headline.append('ID')

    # append mandatory attribute
    headline.append('System')

    # check for remaining attributes
    if constance_config.SPREAD_DNSNAME:
        headline.append('DNS name')
    if constance_config.SPREAD_DOMAIN:
        headline.append('Domain')
    if constance_config.SPREAD_SYSTEMSTATUS:
        headline.append('Systemstatus')
    if constance_config.SPREAD_ANALYSISSTATUS:
        headline.append('Analysisstatus')
    if constance_config.SPREAD_REASON:
        headline.append('Reason')
    if constance_config.SPREAD_RECOMMENDATION:
        headline.append('Recommendation')
    if constance_config.SPREAD_SYSTEMTYPE:
        headline.append('Systemtype')
    if constance_config.SPREAD_IP:
        headline.append('IP')
    if constance_config.SPREAD_OS:
        headline.append('OS')
    if constance_config.SPREAD_COMPANY:
        headline.append('Company')
    if constance_config.SPREAD_LOCATION:
        headline.append('Location')
    if constance_config.SPREAD_SERVICEPROVIDER:
        headline.append('Serviceprovider')
    if constance_config.SPREAD_TAG:
        headline.append('Tag')
    if constance_config.SPREAD_CASE:
        headline.append('Case')
    if constance_config.SPREAD_SYSTEM_CREATE_TIME:
        headline.append('Created')
    if constance_config.SPREAD_SYSTEM_MODIFY_TIME:
        headline.append('Modified')

    # write headline
    sod_writer.writerow(headline)

    """ append systems """

    # get all System objects ordered by system_name
    systems = System.objects.all().order_by("system_name")

    # iterate over systems
    for system in systems:

        # skip system depending on export variable
        if system.system_export_spreadsheet == False:
            continue

        # create empty list for line
        entryline = []

        """ check for attribute """

        # system id
        if constance_config.SPREAD_SYSTEM_ID:
            entryline.append(system.system_id)

        """ append mandatory attribute """

        # system name
        entryline.append(system.system_name)

        """ check for remaining attributes """

        # dnsname
        if constance_config.SPREAD_DNSNAME:
            if system.dnsname == None:
                dnsname = ''
            else:
                dnsname = system.dnsname.dnsname_name
            entryline.append(dnsname)
        # domain
        if constance_config.SPREAD_DOMAIN:
            if system.domain == None:
                domain = ''
            else:
                domain = system.domain.domain_name
            entryline.append(domain)
        # systemstatus
        if constance_config.SPREAD_SYSTEMSTATUS:
            entryline.append(system.systemstatus.systemstatus_name)
        # analysisstatus
        if constance_config.SPREAD_ANALYSISSTATUS:
            if system.analysisstatus == None:
                analysisstatus = ''
            else:
                analysisstatus = system.analysisstatus.analysisstatus_name
            entryline.append(analysisstatus)
        # reason
        if constance_config.SPREAD_REASON:
            if system.reason == None:
                reason = ''
            else:
                reason = system.reason.reason_name
            entryline.append(reason)
        # recommendation
        if constance_config.SPREAD_RECOMMENDATION:
            if system.recommendation== None:
                recommendation = ''
            else:
                recommendation = system.recommendation.recommendation_name
            entryline.append(recommendation)
        # systemtype
        if constance_config.SPREAD_SYSTEMTYPE:
            if system.systemtype == None:
                systemtype = ''
            else:
                systemtype = system.systemtype.systemtype_name
            entryline.append(systemtype)
        # ip
        if constance_config.SPREAD_IP:
            # get all ips of system
            ips_all = system.ip.all()
            # count ips
            n = system.ip.count()
            # create empty ip string
            ip = ''
            # set counter
            i = 1
            # iterate over ip objects in ip list
            for ip_obj in ips_all:
                # add actual ip to ip string
                ip = ip + ip_obj.ip_ip
                # add newline except for last ip
                if i < n:
                    ip = ip + '\n'
                    i = i + 1
            entryline.append(ip)
        # os
        if constance_config.SPREAD_OS:
            if system.os == None:
                os = ''
            else:
                os = system.os.os_name
            entryline.append(os)
        # company
        if constance_config.SPREAD_COMPANY:
            # get all companies of system
            companys_all = system.company.all()
            # count companies
            n = system.company.count()
            # create empty company string
            company = ''
            # set counter
            i = 1
            # iterate over company objects in company list
            for company_obj in companys_all:
                # add actual company to company string
                company = company + company_obj.company_name
                # add newline except for last company
                if i < n:
                    company = company + '\n'
                    i = i + 1
            entryline.append(company)
        # location
        if constance_config.SPREAD_LOCATION:
            if system.location == None:
                location = ''
            else:
                location = system.location.location_name
            entryline.append(location)
        # serviceprovider
        if constance_config.SPREAD_SERVICEPROVIDER:
            if system.serviceprovider == None:
                serviceprovider = ''
            else:
                serviceprovider = system.serviceprovider.serviceprovider_name
            entryline.append(serviceprovider)
        # tag
        if constance_config.SPREAD_TAG:
            # get all tags of system
            tags_all = system.tag.all()
            # count tags
            n = system.tag.count()
            # create empty tag string
            tag = ''
            # set counter
            i = 1
            # iterate over tag objects in tag list
            for tag_obj in tags_all:
                # add actual tag to tag string
                tag = tag + tag_obj.tag_name
                # add newline except for last tag
                if i < n:
                    tag = tag + '\n'
                    i = i + 1
            entryline.append(tag)
        # case
        if constance_config.SPREAD_CASE:
            # get all cases of system
            cases_all = system.case.all()
            # count cases
            n = system.case.count()
            # create empty case string
            case = ''
            # set counter
            i = 1
            # iterate over case objects in case list
            for case_obj in cases_all:
                # add actual case to case string
                case = case + case_obj.case_name
                # add newline except for last case
                if i < n:
                    case = case + '\n'
                    i = i + 1
            entryline.append(case)
        # system create time
        if constance_config.SPREAD_SYSTEM_CREATE_TIME:
            system_create_time = system.system_create_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(system_create_time)
        # system modify time
        if constance_config.SPREAD_SYSTEM_MODIFY_TIME:
            system_modify_time = system.system_modify_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(system_modify_time)

        # write entryline
        sod_writer.writerow(entryline)

    # write an empty row
    sod_writer.writerow([])

    # prepare string value for actual datetimes
    actualtime = strftime('%Y-%m-%d %H:%M')

    # write meta information
    sod_writer.writerow(['SOD created:', actualtime])
    creator = request.user
    sod_writer.writerow(['Created by:', creator])

    # call logger
    info_logger(str(request.user), " SYSTEM_CSV_CREATED")

    # return csv object
    return sod
