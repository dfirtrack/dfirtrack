from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dfirtrack_config.models import SystemExporterSpreadsheetCsvConfigModel
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

    # get config model
    model = SystemExporterSpreadsheetCsvConfigModel.objects.get(system_exporter_spreadsheet_csv_config_name = 'SystemExporterSpreadsheetCsvConfig')

    """ start with headline """

    # create empty list
    headline = []

    # check for attribute id
    if model.spread_csv_system_id:
        headline.append('ID')

    # append mandatory attribute
    headline.append('System')

    # check for remaining attributes
    if model.spread_csv_dnsname:
        headline.append('DNS name')
    if model.spread_csv_domain:
        headline.append('Domain')
    if model.spread_csv_systemstatus:
        headline.append('Systemstatus')
    if model.spread_csv_analysisstatus:
        headline.append('Analysisstatus')
    if model.spread_csv_reason:
        headline.append('Reason')
    if model.spread_csv_recommendation:
        headline.append('Recommendation')
    if model.spread_csv_systemtype:
        headline.append('Systemtype')
    if model.spread_csv_ip:
        headline.append('IP')
    if model.spread_csv_os:
        headline.append('OS')
    if model.spread_csv_company:
        headline.append('Company')
    if model.spread_csv_location:
        headline.append('Location')
    if model.spread_csv_serviceprovider:
        headline.append('Serviceprovider')
    if model.spread_csv_tag:
        headline.append('Tag')
    if model.spread_csv_case:
        headline.append('Case')
    if model.spread_csv_system_create_time:
        headline.append('Created')
    if model.spread_csv_system_modify_time:
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
        if model.spread_csv_system_id:
            entryline.append(system.system_id)

        """ append mandatory attribute """

        # system name
        entryline.append(system.system_name)

        """ check for remaining attributes """

        # dnsname
        if model.spread_csv_dnsname:
            if system.dnsname == None:
                dnsname = ''
            else:
                dnsname = system.dnsname.dnsname_name
            entryline.append(dnsname)
        # domain
        if model.spread_csv_domain:
            if system.domain == None:
                domain = ''
            else:
                domain = system.domain.domain_name
            entryline.append(domain)
        # systemstatus
        if model.spread_csv_systemstatus:
            entryline.append(system.systemstatus.systemstatus_name)
        # analysisstatus
        if model.spread_csv_analysisstatus:
            if system.analysisstatus == None:
                analysisstatus = ''
            else:
                analysisstatus = system.analysisstatus.analysisstatus_name
            entryline.append(analysisstatus)
        # reason
        if model.spread_csv_reason:
            if system.reason == None:
                reason = ''
            else:
                reason = system.reason.reason_name
            entryline.append(reason)
        # recommendation
        if model.spread_csv_recommendation:
            if system.recommendation== None:
                recommendation = ''
            else:
                recommendation = system.recommendation.recommendation_name
            entryline.append(recommendation)
        # systemtype
        if model.spread_csv_systemtype:
            if system.systemtype == None:
                systemtype = ''
            else:
                systemtype = system.systemtype.systemtype_name
            entryline.append(systemtype)
        # ip
        if model.spread_csv_ip:
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
        if model.spread_csv_os:
            if system.os == None:
                os = ''
            else:
                os = system.os.os_name
            entryline.append(os)
        # company
        if model.spread_csv_company:
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
        if model.spread_csv_location:
            if system.location == None:
                location = ''
            else:
                location = system.location.location_name
            entryline.append(location)
        # serviceprovider
        if model.spread_csv_serviceprovider:
            if system.serviceprovider == None:
                serviceprovider = ''
            else:
                serviceprovider = system.serviceprovider.serviceprovider_name
            entryline.append(serviceprovider)
        # tag
        if model.spread_csv_tag:
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
        if model.spread_csv_case:
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
        if model.spread_csv_system_create_time:
            system_create_time = system.system_create_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(system_create_time)
        # system modify time
        if model.spread_csv_system_modify_time:
            system_modify_time = system.system_modify_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(system_modify_time)

        # write entryline
        sod_writer.writerow(entryline)

        # call logger
        info_logger(str(request.user), ' SYSTEM_CSV SYSTEM ' + str(system.system_id) + '||' + system.system_name)

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
