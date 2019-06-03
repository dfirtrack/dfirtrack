from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dfirtrack_main.logger.default_logger import info_logger
from dfirtrack_main.models import System
import xlwt
from time import strftime

@login_required(login_url="/login")
def systems(request):

    # create xls MIME type object
    sod = HttpResponse(content_type='application/ms-excel')

    # define filename
    sod['Content-Disposition'] = 'attachment; filename="systems.xls"'

    # preamble
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Systems')

    # set counter
    row_num = 0

    # define styling
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style.font = font
    borders = xlwt.Borders()

    # prepare headline
    columns = [
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
    ]

    # write headline
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num], style)

    style = xlwt.XFStyle()

    # get all System objects ordered by system_name
    systems = System.objects.all().order_by("system_name")

    # iterate over systems
    for system in systems:

        # autoincrement row counter
        row_num += 1

        # set column counter
        col_num = 1

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

        # prepare a line for every system
        columns = [
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
        ]

        # write a line for every system (iterate over column content)
        for col_num in range(len(columns)):
            worksheet.write(row_num, col_num, columns[col_num], style)

    # write an empty row
    row_num += 2

    # write meta information
    actualtime = strftime('%Y-%m-%d %H:%M')
    worksheet.write(row_num, 0, 'SOD created:', style)
    worksheet.write(row_num, 1, actualtime, style)
    row_num += 1
    creator = str(request.user)
    worksheet.write(row_num, 0, 'Created by:', style)
    worksheet.write(row_num, 1, creator, style)

    # close file
    workbook.save(sod)

    # call logger
    info_logger(str(request.user), " SYSTEM_XLS_CREATED")

    # return xls object
    return sod
