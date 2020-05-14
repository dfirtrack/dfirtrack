from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.logger.default_logger import info_logger, warning_logger
from dfirtrack_main.models import System
import csv
from time import strftime

@login_required(login_url="/login")
def system(request):

    """ check variables of dfirtrack.config """

    # reset stop condition
    stop_system_exporter_spreadsheet_csv = False

    # check SPREAD_SYSTEM_ID for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_ID, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEM_ID` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_SYSTEM_ID deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_DNSNAME for bool
    if not isinstance(dfirtrack_config.SPREAD_DNSNAME, bool):
        messages.error(request, "Deformed `SPREAD_DNSNAME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_DNSNAME deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_DOMAIN for bool
    if not isinstance(dfirtrack_config.SPREAD_DOMAIN, bool):
        messages.error(request, "Deformed `SPREAD_DOMAIN` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_DOMAIN deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_SYSTEMSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEMSTATUS, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEMSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_SYSTEMSTATUS deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_ANALYSISSTATUS for bool
    if not isinstance(dfirtrack_config.SPREAD_ANALYSISSTATUS, bool):
        messages.error(request, "Deformed `SPREAD_ANALYSISSTATUS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_ANALYSISSTATUS deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_REASON for bool
    if not isinstance(dfirtrack_config.SPREAD_REASON, bool):
        messages.error(request, "Deformed `SPREAD_REASON` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_REASON deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_RECOMMENDATION for bool
    if not isinstance(dfirtrack_config.SPREAD_RECOMMENDATION, bool):
        messages.error(request, "Deformed `SPREAD_RECOMMENDATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_RECOMMENDATION deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_SYSTEMTYPE for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEMTYPE, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEMTYPE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_SYSTEMTYPE deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_IP for bool
    if not isinstance(dfirtrack_config.SPREAD_IP, bool):
        messages.error(request, "Deformed `SPREAD_IP` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_IP deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_OS for bool
    if not isinstance(dfirtrack_config.SPREAD_OS, bool):
        messages.error(request, "Deformed `SPREAD_OS` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_OS deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_COMPANY for bool
    if not isinstance(dfirtrack_config.SPREAD_COMPANY, bool):
        messages.error(request, "Deformed `SPREAD_COMPANY` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_COMPANY deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_LOCATION for bool
    if not isinstance(dfirtrack_config.SPREAD_LOCATION, bool):
        messages.error(request, "Deformed `SPREAD_LOCATION` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_LOCATION deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_SERVICEPROVIDER for bool
    if not isinstance(dfirtrack_config.SPREAD_SERVICEPROVIDER, bool):
        messages.error(request, "Deformed `SPREAD_SERVICEPROVIDER` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_SERVICEPROVIDER deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_TAG for bool
    if not isinstance(dfirtrack_config.SPREAD_TAG, bool):
        messages.error(request, "Deformed `SPREAD_TAG` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_TAG deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_CASE for bool
    if not isinstance(dfirtrack_config.SPREAD_CASE, bool):
        messages.error(request, "Deformed `SPREAD_CASE` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_CASE deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_SYSTEM_CREATE_TIME for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEM_CREATE_TIME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_SYSTEM_CREATE_TIME deformed")
        stop_system_exporter_spreadsheet_csv = True

    # check SPREAD_SYSTEM_MODIFY_TIME for bool
    if not isinstance(dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME, bool):
        messages.error(request, "Deformed `SPREAD_SYSTEM_MODIFY_TIME` Check `dfirtrack.config`!")
        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV variable SPREAD_SYSTEM_MODIFY_TIME deformed")
        stop_system_exporter_spreadsheet_csv = True

    # leave system_exporter_spreadsheet_csv if variables caused errors
    if stop_system_exporter_spreadsheet_csv:

        # call logger
        warning_logger(str(request.user), " SYSTEM_EXPORTER_SPREADSHEET_CSV_END_WITH_ERRORS")
        return redirect(reverse('system_list'))

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
    if dfirtrack_config.SPREAD_SYSTEM_ID:
        headline.append('ID')

    # append mandatory attribute
    headline.append('System')

    # check for remaining attributes
    if dfirtrack_config.SPREAD_DNSNAME:
        headline.append('DNS name')
    if dfirtrack_config.SPREAD_DOMAIN:
        headline.append('Domain')
    if dfirtrack_config.SPREAD_SYSTEMSTATUS:
        headline.append('Systemstatus')
    if dfirtrack_config.SPREAD_ANALYSISSTATUS:
        headline.append('Analysisstatus')
    if dfirtrack_config.SPREAD_REASON:
        headline.append('Reason')
    if dfirtrack_config.SPREAD_RECOMMENDATION:
        headline.append('Recommendation')
    if dfirtrack_config.SPREAD_SYSTEMTYPE:
        headline.append('Systemtype')
    if dfirtrack_config.SPREAD_IP:
        headline.append('IP')
    if dfirtrack_config.SPREAD_OS:
        headline.append('OS')
    if dfirtrack_config.SPREAD_COMPANY:
        headline.append('Company')
    if dfirtrack_config.SPREAD_LOCATION:
        headline.append('Location')
    if dfirtrack_config.SPREAD_SERVICEPROVIDER:
        headline.append('Serviceprovider')
    if dfirtrack_config.SPREAD_TAG:
        headline.append('Tag')
    if dfirtrack_config.SPREAD_CASE:
        headline.append('Case')
    if dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME:
        headline.append('Created')
    if dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME:
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
        if dfirtrack_config.SPREAD_SYSTEM_ID:
            entryline.append(system.system_id)

        """ append mandatory attribute """

        # system name
        entryline.append(system.system_name)

        """ check for remaining attributes """

        # dnsname
        if dfirtrack_config.SPREAD_DNSNAME:
            if system.dnsname == None:
                dnsname = ''
            else:
                dnsname = system.dnsname.dnsname_name
            entryline.append(dnsname)
        # domain
        if dfirtrack_config.SPREAD_DOMAIN:
            if system.domain == None:
                domain = ''
            else:
                domain = system.domain.domain_name
            entryline.append(domain)
        # systemstatus
        if dfirtrack_config.SPREAD_SYSTEMSTATUS:
            entryline.append(system.systemstatus.systemstatus_name)
        # analysisstatus
        if dfirtrack_config.SPREAD_ANALYSISSTATUS:
            entryline.append(system.analysisstatus.analysisstatus_name)
        # reason
        if dfirtrack_config.SPREAD_REASON:
            if system.reason == None:
                reason = ''
            else:
                reason = system.reason.reason_name
            entryline.append(reason)
        # recommendation
        if dfirtrack_config.SPREAD_RECOMMENDATION:
            if system.recommendation== None:
                recommendation = ''
            else:
                recommendation = system.recommendation.recommendation_name
            entryline.append(recommendation)
        # systemtype
        if dfirtrack_config.SPREAD_SYSTEMTYPE:
            if system.systemtype == None:
                systemtype = ''
            else:
                systemtype = system.systemtype.systemtype_name
            entryline.append(systemtype)
        # ip
        if dfirtrack_config.SPREAD_IP:
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
        if dfirtrack_config.SPREAD_OS:
            if system.os == None:
                os = ''
            else:
                os = system.os.os_name
            entryline.append(os)
        # company
        if dfirtrack_config.SPREAD_COMPANY:
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
        if dfirtrack_config.SPREAD_LOCATION:
            if system.location == None:
                location = ''
            else:
                location = system.location.location_name
            entryline.append(location)
        # serviceprovider
        if dfirtrack_config.SPREAD_SERVICEPROVIDER:
            if system.serviceprovider == None:
                serviceprovider = ''
            else:
                serviceprovider = system.serviceprovider.serviceprovider_name
            entryline.append(serviceprovider)
        # tag
        if dfirtrack_config.SPREAD_TAG:
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
        if dfirtrack_config.SPREAD_CASE:
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
        if dfirtrack_config.SPREAD_SYSTEM_CREATE_TIME:
            system_create_time = system.system_create_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(system_create_time)
        # system modify time
        if dfirtrack_config.SPREAD_SYSTEM_MODIFY_TIME:
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
