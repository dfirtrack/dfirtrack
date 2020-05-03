from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dfirtrack_main.logger.default_logger import info_logger
from dfirtrack_main.models import System
import csv
from time import strftime

@login_required(login_url="/login")
def system(request):

    # create csv MIME type object
    sod = HttpResponse(content_type='text/csv')

    # define filename
    sod['Content-Disposition'] = 'attachment; filename="systems.csv"'

    # create file object for writing lines
    sod_writer = csv.writer(sod)

    # write headline
    sod_writer.writerow([
        'ID',
        'System',
        'Status',
        'Reason',
        'Recommendation',
        'Type',
        'IP',
        'Domain',
        'DNS Name',
        'OS',
        'Company',
        'Location',
        'Serviceprovider',
        'Created',
        'Last modified',
    ])

    # get all System objects ordered by system_name
    systems = System.objects.all().order_by("system_name")

    # iterate over systems
    for system in systems:

        # skip system depending on export variable
        if system.system_export_spreadsheet == False:
            continue

        # set foreign key field to none if it doesn't exist
        if system.reason == None:
            reason = ''
        else:
            reason = system.reason.reason_name

        # set foreign key field to none if it doesn't exist
        if system.recommendation== None:
            recommendation = ''
        else:
            recommendation = system.recommendation.recommendation_name

        # set foreign key field to none if it doesn't exist
        if system.systemtype == None:
            systemtype = ''
        else:
            systemtype = system.systemtype.systemtype_name

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

        # set foreign key field to none if it doesn't exist
        if system.domain == None:
            domain = ''
        else:
            domain = system.domain.domain_name

        # set foreign key field to none if it doesn't exist
        if system.dnsname == None:
            dnsname = ''
        else:
            dnsname = system.dnsname.dnsname_name

        # set foreign key field to none if it doesn't exist
        if system.os == None:
            os = ''
        else:
            os = system.os.os_name

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

        # set foreign key field to none if it doesn't exist
        if system.location == None:
            location = ''
        else:
            location = system.location.location_name

        # set foreign key field to none if it doesn't exist
        if system.serviceprovider == None:
            serviceprovider = ''
        else:
            serviceprovider = system.serviceprovider.serviceprovider_name

        # prepare string values for datetimes
        create_time = system.system_create_time.strftime('%Y-%m-%d %H:%M')
        modify_time = system.system_modify_time.strftime('%Y-%m-%d %H:%M')

        # write a line for every system
        sod_writer.writerow([
            system.system_id,
            system.system_name,
            system.systemstatus.systemstatus_name,
            reason,
            recommendation,
            systemtype,
            ip,
            domain,
            dnsname,
            os,
            company,
            location,
            serviceprovider,
            create_time,
            modify_time,
        ])

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
