from constance import config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_main.config_forms import SystemExporterSpreadsheetCsvForm, SystemExporterSpreadsheetXlsForm

@login_required(login_url="/login")
def system_exporter_spreadsheet_csv_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemExporterSpreadsheetCsvForm(request.POST)

        if form.is_valid():

            # assign values
            config.SPREAD_SYSTEM_ID = form.cleaned_data['spread_system_id']
            config.SPREAD_DNSNAME = form.cleaned_data['spread_dnsname']
            config.SPREAD_DOMAIN = form.cleaned_data['spread_domain']
            config.SPREAD_SYSTEMSTATUS = form.cleaned_data['spread_systemstatus']
            config.SPREAD_ANALYSISSTATUS = form.cleaned_data['spread_analysisstatus']
            config.SPREAD_REASON = form.cleaned_data['spread_reason']
            config.SPREAD_RECOMMENDATION = form.cleaned_data['spread_recommendation']
            config.SPREAD_SYSTEMTYPE = form.cleaned_data['spread_systemtype']
            config.SPREAD_IP = form.cleaned_data['spread_ip']
            config.SPREAD_OS = form.cleaned_data['spread_os']
            config.SPREAD_COMPANY = form.cleaned_data['spread_company']
            config.SPREAD_LOCATION = form.cleaned_data['spread_location']
            config.SPREAD_SERVICEPROVIDER = form.cleaned_data['spread_serviceprovider']
            config.SPREAD_TAG = form.cleaned_data['spread_tag']
            config.SPREAD_CASE = form.cleaned_data['spread_case']
            config.SPREAD_SYSTEM_CREATE_TIME = form.cleaned_data['spread_system_create_time']
            config.SPREAD_SYSTEM_MODIFY_TIME = form.cleaned_data['spread_system_modify_time']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemExporterSpreadsheetCsvForm(
            initial = {
                'spread_system_id': config.SPREAD_SYSTEM_ID,
                'spread_dnsname': config.SPREAD_DNSNAME,
                'spread_domain': config.SPREAD_DOMAIN,
                'spread_systemstatus': config.SPREAD_SYSTEMSTATUS,
                'spread_analysisstatus': config.SPREAD_ANALYSISSTATUS,
                'spread_reason': config.SPREAD_REASON,
                'spread_recommendation': config.SPREAD_RECOMMENDATION,
                'spread_systemtype': config.SPREAD_SYSTEMTYPE,
                'spread_ip': config.SPREAD_IP,
                'spread_os': config.SPREAD_OS,
                'spread_company': config.SPREAD_COMPANY,
                'spread_location': config.SPREAD_LOCATION,
                'spread_serviceprovider': config.SPREAD_SERVICEPROVIDER,
                'spread_tag': config.SPREAD_TAG,
                'spread_case': config.SPREAD_CASE,
                'spread_system_create_time': config.SPREAD_SYSTEM_CREATE_TIME,
                'spread_system_modify_time': config.SPREAD_SYSTEM_MODIFY_TIME,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_exporter_spreadsheet_csv_config_popup.html',
        {
            'form': form,
        }
    )

@login_required(login_url="/login")
def system_exporter_spreadsheet_xls_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemExporterSpreadsheetXlsForm(request.POST)

        if form.is_valid():

            # assign values
            config.SPREAD_SYSTEM_ID = form.cleaned_data['spread_system_id']
            config.SPREAD_DNSNAME = form.cleaned_data['spread_dnsname']
            config.SPREAD_DOMAIN = form.cleaned_data['spread_domain']
            config.SPREAD_SYSTEMSTATUS = form.cleaned_data['spread_systemstatus']
            config.SPREAD_ANALYSISSTATUS = form.cleaned_data['spread_analysisstatus']
            config.SPREAD_REASON = form.cleaned_data['spread_reason']
            config.SPREAD_RECOMMENDATION = form.cleaned_data['spread_recommendation']
            config.SPREAD_SYSTEMTYPE = form.cleaned_data['spread_systemtype']
            config.SPREAD_IP = form.cleaned_data['spread_ip']
            config.SPREAD_OS = form.cleaned_data['spread_os']
            config.SPREAD_COMPANY = form.cleaned_data['spread_company']
            config.SPREAD_LOCATION = form.cleaned_data['spread_location']
            config.SPREAD_SERVICEPROVIDER = form.cleaned_data['spread_serviceprovider']
            config.SPREAD_TAG = form.cleaned_data['spread_tag']
            config.SPREAD_CASE = form.cleaned_data['spread_case']
            config.SPREAD_SYSTEM_CREATE_TIME = form.cleaned_data['spread_system_create_time']
            config.SPREAD_SYSTEM_MODIFY_TIME = form.cleaned_data['spread_system_modify_time']
            config.SPREAD_WORKSHEET_SYSTEMSTATUS = form.cleaned_data['spread_worksheet_systemstatus']
            config.SPREAD_WORKSHEET_ANALYSISSTATUS = form.cleaned_data['spread_worksheet_analysisstatus']
            config.SPREAD_WORKSHEET_REASON = form.cleaned_data['spread_worksheet_reason']
            config.SPREAD_WORKSHEET_RECOMMENDATION = form.cleaned_data['spread_worksheet_recommendation']
            config.SPREAD_WORKSHEET_TAG = form.cleaned_data['spread_worksheet_tag']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemExporterSpreadsheetXlsForm(
            initial = {
                'spread_system_id': config.SPREAD_SYSTEM_ID,
                'spread_dnsname': config.SPREAD_DNSNAME,
                'spread_domain': config.SPREAD_DOMAIN,
                'spread_systemstatus': config.SPREAD_SYSTEMSTATUS,
                'spread_analysisstatus': config.SPREAD_ANALYSISSTATUS,
                'spread_reason': config.SPREAD_REASON,
                'spread_recommendation': config.SPREAD_RECOMMENDATION,
                'spread_systemtype': config.SPREAD_SYSTEMTYPE,
                'spread_ip': config.SPREAD_IP,
                'spread_os': config.SPREAD_OS,
                'spread_company': config.SPREAD_COMPANY,
                'spread_location': config.SPREAD_LOCATION,
                'spread_serviceprovider': config.SPREAD_SERVICEPROVIDER,
                'spread_tag': config.SPREAD_TAG,
                'spread_case': config.SPREAD_CASE,
                'spread_system_create_time': config.SPREAD_SYSTEM_CREATE_TIME,
                'spread_system_modify_time': config.SPREAD_SYSTEM_MODIFY_TIME,
                'spread_worksheet_systemstatus': config.SPREAD_WORKSHEET_SYSTEMSTATUS,
                'spread_worksheet_analysisstatus': config.SPREAD_WORKSHEET_ANALYSISSTATUS,
                'spread_worksheet_reason': config.SPREAD_WORKSHEET_REASON,
                'spread_worksheet_recommendation': config.SPREAD_WORKSHEET_RECOMMENDATION,
                'spread_worksheet_tag': config.SPREAD_WORKSHEET_TAG,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_exporter_spreadsheet_xls_config_popup.html',
        {
            'form': form,
        }
    )
