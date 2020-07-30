from constance import config as constance_config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_main.config_forms import SystemImporterFileCsvConfigForm

@login_required(login_url="/login")
def system_importer_file_csv_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemImporterFileCsvConfigForm(request.POST)

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

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemImporterFileCsvConfigForm(
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
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_config_popup.html',
        {
            'form': form,
        }
    )
