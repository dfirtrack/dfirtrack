from constance import config as constance_config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_main.config_forms import SystemImporterFileCsvConfigbasedConfigForm, SystemImporterFileCsvFormbasedConfigForm

@login_required(login_url="/login")
def system_importer_file_csv_config_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemImporterFileCsvConfigbasedConfigForm(request.POST)

        if form.is_valid():

            """ assign values """

            # general settings
            constance_config.CSV_SKIP_EXISTING_SYSTEM = form.cleaned_data['csv_skip_existing_system']
            constance_config.CSV_COLUMN_SYSTEM = form.cleaned_data['csv_column_system']
            constance_config.CSV_HEADLINE = form.cleaned_data['csv_headline']
            # IP related settings
            constance_config.CSV_CHOICE_IP = form.cleaned_data['csv_choice_ip']
            constance_config.CSV_REMOVE_IP = form.cleaned_data['csv_remove_ip']
            constance_config.CSV_COLUMN_IP = form.cleaned_data['csv_column_ip']
            # overriding settings
            constance_config.CSV_REMOVE_CASE = form.cleaned_data['csv_remove_case']
            constance_config.CSV_REMOVE_COMPANY = form.cleaned_data['csv_remove_company']
            constance_config.CSV_REMOVE_TAG = form.cleaned_data['csv_remove_tag']
            # config based settings
            constance_config.CSV_DEFAULT_SYSTEMSTATUS = form.cleaned_data['csv_default_systemstatus']
            constance_config.CSV_DEFAULT_ANALYSISSTATUS = form.cleaned_data['csv_default_analysisstatus']
            constance_config.CSV_DEFAULT_REASON = form.cleaned_data['csv_default_reason']
            constance_config.CSV_DEFAULT_DOMAIN = form.cleaned_data['csv_default_domain']
            constance_config.CSV_DEFAULT_DNSNAME = form.cleaned_data['csv_default_dnsname']
            constance_config.CSV_DEFAULT_SYSTEMTYPE = form.cleaned_data['csv_default_systemtype']
            constance_config.CSV_DEFAULT_OS = form.cleaned_data['csv_default_os']
            constance_config.CSV_DEFAULT_LOCATION = form.cleaned_data['csv_default_location']
            constance_config.CSV_DEFAULT_SERVICEPROVIDER = form.cleaned_data['csv_default_serviceprovider']
            constance_config.CSV_DEFAULT_CASE = form.cleaned_data['csv_default_case']
            constance_config.CSV_DEFAULT_COMPANY = form.cleaned_data['csv_default_company']
            constance_config.CSV_DEFAULT_TAG = form.cleaned_data['csv_default_tag']

            # close popup
            return HttpResponse('<script type="text/javascript">window.close();</script>')
        else:
            # show form page
            return render(
                request,
                'dfirtrack_main/system/system_importer_file_csv_config_based_config_popup.html',
                {
                    'form': form,
                }
            )

    else:

        # submit existing values to form
        form = SystemImporterFileCsvConfigbasedConfigForm(
            initial = {
                # general settings
                'csv_skip_existing_system': constance_config.CSV_SKIP_EXISTING_SYSTEM,
                'csv_column_system': constance_config.CSV_COLUMN_SYSTEM,
                'csv_headline': constance_config.CSV_HEADLINE,
                # IP related settings
                'csv_choice_ip': constance_config.CSV_CHOICE_IP,
                'csv_remove_ip': constance_config.CSV_REMOVE_IP,
                'csv_column_ip': constance_config.CSV_COLUMN_IP,
                # overriding settings
                'csv_remove_case': constance_config.CSV_REMOVE_CASE,
                'csv_remove_company': constance_config.CSV_REMOVE_COMPANY,
                'csv_remove_tag': constance_config.CSV_REMOVE_TAG,
                # config based settings
                'csv_default_systemstatus': constance_config.CSV_DEFAULT_SYSTEMSTATUS,
                'csv_default_analysisstatus': constance_config.CSV_DEFAULT_ANALYSISSTATUS,
                'csv_default_reason': constance_config.CSV_DEFAULT_REASON,
                'csv_default_domain': constance_config.CSV_DEFAULT_DOMAIN,
                'csv_default_dnsname': constance_config.CSV_DEFAULT_DNSNAME,
                'csv_default_systemtype': constance_config.CSV_DEFAULT_SYSTEMTYPE,
                'csv_default_os': constance_config.CSV_DEFAULT_OS,
                'csv_default_location': constance_config.CSV_DEFAULT_LOCATION,
                'csv_default_serviceprovider': constance_config.CSV_DEFAULT_SERVICEPROVIDER,
                'csv_default_case': constance_config.CSV_DEFAULT_CASE,
                'csv_default_company': constance_config.CSV_DEFAULT_COMPANY,
                'csv_default_tag': constance_config.CSV_DEFAULT_TAG,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_config_based_config_popup.html',
        {
            'form': form,
        }
    )

@login_required(login_url="/login")
def system_importer_file_csv_form_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemImporterFileCsvFormbasedConfigForm(request.POST)

        if form.is_valid():

            """ assign values """

            # general settings
            constance_config.CSV_SKIP_EXISTING_SYSTEM = form.cleaned_data['csv_skip_existing_system']
            constance_config.CSV_COLUMN_SYSTEM = form.cleaned_data['csv_column_system']
            constance_config.CSV_HEADLINE = form.cleaned_data['csv_headline']
            # IP related settings
            constance_config.CSV_CHOICE_IP = form.cleaned_data['csv_choice_ip']
            constance_config.CSV_REMOVE_IP = form.cleaned_data['csv_remove_ip']
            constance_config.CSV_COLUMN_IP = form.cleaned_data['csv_column_ip']
            # overriding settings
            constance_config.CSV_REMOVE_CASE = form.cleaned_data['csv_remove_case']
            constance_config.CSV_REMOVE_COMPANY = form.cleaned_data['csv_remove_company']
            constance_config.CSV_REMOVE_TAG = form.cleaned_data['csv_remove_tag']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemImporterFileCsvFormbasedConfigForm(
            initial = {
                # general settings
                'csv_skip_existing_system': constance_config.CSV_SKIP_EXISTING_SYSTEM,
                'csv_column_system': constance_config.CSV_COLUMN_SYSTEM,
                'csv_headline': constance_config.CSV_HEADLINE,
                # IP related settings
                'csv_choice_ip': constance_config.CSV_CHOICE_IP,
                'csv_remove_ip': constance_config.CSV_REMOVE_IP,
                'csv_column_ip': constance_config.CSV_COLUMN_IP,
                # overriding settings
                'csv_remove_case': constance_config.CSV_REMOVE_CASE,
                'csv_remove_company': constance_config.CSV_REMOVE_COMPANY,
                'csv_remove_tag': constance_config.CSV_REMOVE_TAG,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_form_based_config_popup.html',
        {
            'form': form,
        }
    )
