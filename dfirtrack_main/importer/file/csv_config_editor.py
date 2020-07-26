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
            constance_config.CSV_CHOICE_SYSTEMSTATUS = form.cleaned_data['csv_choice_systemstatus']
            constance_config.CSV_CHOICE_ANALYSISSTATUS = form.cleaned_data['csv_choice_analysisstatus']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemImporterFileCsvConfigForm(
            initial = {
                'csv_choice_systemstatus': constance_config.CSV_CHOICE_SYSTEMSTATUS,
                'csv_choice_analysisstatus': constance_config.CSV_CHOICE_ANALYSISSTATUS,
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
