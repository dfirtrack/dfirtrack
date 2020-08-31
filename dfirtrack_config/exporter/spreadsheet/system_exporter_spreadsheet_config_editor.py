from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_config.forms import SystemExporterSpreadsheetCsvConfigForm, SystemExporterSpreadsheetXlsConfigForm
from dfirtrack_config.models import SystemExporterSpreadsheetCsvConfigModel, SystemExporterSpreadsheetXlsConfigModel

@login_required(login_url="/login")
def system_exporter_spreadsheet_csv_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemExporterSpreadsheetCsvConfigForm(request.POST)
        model = SystemExporterSpreadsheetCsvConfigModel.objects.get(system_exporter_spreadsheet_csv_config_name = 'SystemExporterSpreadsheetCsvConfig')

        if form.is_valid():

            # assign values
            model.spread_csv_system_id = form.cleaned_data['spread_system_id']
            model.spread_csv_dnsname = form.cleaned_data['spread_dnsname']
            model.spread_csv_domain = form.cleaned_data['spread_domain']
            model.spread_csv_systemstatus = form.cleaned_data['spread_systemstatus']
            model.spread_csv_analysisstatus = form.cleaned_data['spread_analysisstatus']
            model.spread_csv_reason = form.cleaned_data['spread_reason']
            model.spread_csv_recommendation = form.cleaned_data['spread_recommendation']
            model.spread_csv_systemtype = form.cleaned_data['spread_systemtype']
            model.spread_csv_ip = form.cleaned_data['spread_ip']
            model.spread_csv_os = form.cleaned_data['spread_os']
            model.spread_csv_company = form.cleaned_data['spread_company']
            model.spread_csv_location = form.cleaned_data['spread_location']
            model.spread_csv_serviceprovider = form.cleaned_data['spread_serviceprovider']
            model.spread_csv_tag = form.cleaned_data['spread_tag']
            model.spread_csv_case = form.cleaned_data['spread_case']
            model.spread_csv_system_create_time = form.cleaned_data['spread_system_create_time']
            model.spread_csv_system_modify_time = form.cleaned_data['spread_system_modify_time']
            model.save()

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # get config model
        model = SystemExporterSpreadsheetCsvConfigModel.objects.get(system_exporter_spreadsheet_csv_config_name = 'SystemExporterSpreadsheetCsvConfig')
        # submit existing values to form
        form = SystemExporterSpreadsheetCsvConfigForm(
            initial = {
                'spread_system_id': model.spread_csv_system_id,
                'spread_dnsname': model.spread_csv_dnsname,
                'spread_domain': model.spread_csv_domain,
                'spread_systemstatus': model.spread_csv_systemstatus,
                'spread_analysisstatus': model.spread_csv_analysisstatus,
                'spread_reason': model.spread_csv_reason,
                'spread_recommendation': model.spread_csv_recommendation,
                'spread_systemtype': model.spread_csv_systemtype,
                'spread_ip': model.spread_csv_ip,
                'spread_os': model.spread_csv_os,
                'spread_company': model.spread_csv_company,
                'spread_location': model.spread_csv_location,
                'spread_serviceprovider': model.spread_csv_serviceprovider,
                'spread_tag': model.spread_csv_tag,
                'spread_case': model.spread_csv_case,
                'spread_system_create_time': model.spread_csv_system_create_time,
                'spread_system_modify_time': model.spread_csv_system_modify_time,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_config/system/system_exporter_spreadsheet_csv_config_popup.html',
        {
            'form': form,
        }
    )

@login_required(login_url="/login")
def system_exporter_spreadsheet_xls_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemExporterSpreadsheetXlsConfigForm(request.POST)
        model = SystemExporterSpreadsheetXlsConfigModel.objects.get(system_exporter_spreadsheet_xls_config_name = 'SystemExporterSpreadsheetXlsConfig')

        if form.is_valid():

            # assign values
            model.spread_xls_system_id = form.cleaned_data['spread_system_id']
            model.spread_xls_dnsname = form.cleaned_data['spread_dnsname']
            model.spread_xls_domain = form.cleaned_data['spread_domain']
            model.spread_xls_systemstatus = form.cleaned_data['spread_systemstatus']
            model.spread_xls_analysisstatus = form.cleaned_data['spread_analysisstatus']
            model.spread_xls_reason = form.cleaned_data['spread_reason']
            model.spread_xls_recommendation = form.cleaned_data['spread_recommendation']
            model.spread_xls_systemtype = form.cleaned_data['spread_systemtype']
            model.spread_xls_ip = form.cleaned_data['spread_ip']
            model.spread_xls_os = form.cleaned_data['spread_os']
            model.spread_xls_company = form.cleaned_data['spread_company']
            model.spread_xls_location = form.cleaned_data['spread_location']
            model.spread_xls_serviceprovider = form.cleaned_data['spread_serviceprovider']
            model.spread_xls_tag = form.cleaned_data['spread_tag']
            model.spread_xls_case = form.cleaned_data['spread_case']
            model.spread_xls_system_create_time = form.cleaned_data['spread_system_create_time']
            model.spread_xls_system_modify_time = form.cleaned_data['spread_system_modify_time']
            model.spread_xls_worksheet_systemstatus = form.cleaned_data['spread_worksheet_systemstatus']
            model.spread_xls_worksheet_analysisstatus = form.cleaned_data['spread_worksheet_analysisstatus']
            model.spread_xls_worksheet_reason = form.cleaned_data['spread_worksheet_reason']
            model.spread_xls_worksheet_recommendation = form.cleaned_data['spread_worksheet_recommendation']
            model.spread_xls_worksheet_tag = form.cleaned_data['spread_worksheet_tag']
            model.save()

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # get config model
        model = SystemExporterSpreadsheetXlsConfigModel.objects.get(system_exporter_spreadsheet_xls_config_name = 'SystemExporterSpreadsheetXlsConfig')
        # submit existing values to form
        form = SystemExporterSpreadsheetXlsConfigForm(
            initial = {
                'spread_system_id': model.spread_xls_system_id,
                'spread_dnsname': model.spread_xls_dnsname,
                'spread_domain': model.spread_xls_domain,
                'spread_systemstatus': model.spread_xls_systemstatus,
                'spread_analysisstatus': model.spread_xls_analysisstatus,
                'spread_reason': model.spread_xls_reason,
                'spread_recommendation': model.spread_xls_recommendation,
                'spread_systemtype': model.spread_xls_systemtype,
                'spread_ip': model.spread_xls_ip,
                'spread_os': model.spread_xls_os,
                'spread_company': model.spread_xls_company,
                'spread_location': model.spread_xls_location,
                'spread_serviceprovider': model.spread_xls_serviceprovider,
                'spread_tag': model.spread_xls_tag,
                'spread_case': model.spread_xls_case,
                'spread_system_create_time': model.spread_xls_system_create_time,
                'spread_system_modify_time': model.spread_xls_system_modify_time,
                'spread_worksheet_systemstatus': model.spread_xls_worksheet_systemstatus,
                'spread_worksheet_analysisstatus': model.spread_xls_worksheet_analysisstatus,
                'spread_worksheet_reason': model.spread_xls_worksheet_reason,
                'spread_worksheet_recommendation': model.spread_xls_worksheet_recommendation,
                'spread_worksheet_tag': model.spread_xls_worksheet_tag,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_config/system/system_exporter_spreadsheet_xls_config_popup.html',
        {
            'form': form,
        }
    )
