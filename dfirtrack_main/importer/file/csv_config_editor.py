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

            # assign values
            constance_config.CSV_CHOICE_IP = form.cleaned_data['csv_choice_ip']
            constance_config.CSV_REMOVE_IP = form.cleaned_data['csv_remove_ip']
            constance_config.CSV_COLUMN_IP = form.cleaned_data['csv_column_ip']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemImporterFileCsvConfigForm(
            initial = {
                'csv_choice_ip': constance_config.CSV_CHOICE_IP,
                'csv_remove_ip': constance_config.CSV_REMOVE_IP,
                'csv_column_ip': constance_config.CSV_COLUMN_IP,
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
