from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_config.forms import SystemImporterFileCsvConfigbasedConfigForm, SystemImporterFileCsvFormbasedConfigForm
from dfirtrack_config.models import SystemImporterFileCsvConfigbasedConfigModel, SystemImporterFileCsvFormbasedConfigModel
from dfirtrack_main.logger.default_logger import info_logger

@login_required(login_url="/login")
def system_importer_file_csv_config_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        # get config model
        model = SystemImporterFileCsvConfigbasedConfigModel.objects.get(system_importer_file_csv_configbased_config_name = 'SystemImporterFileCsvConfigbasedConfig')
        # get form
        form = SystemImporterFileCsvConfigbasedConfigForm(request.POST, instance = model)

        if form.is_valid():

            # save settings
            model = form.save(commit=False)
            model.save()
            form.save_m2m()

            # call logger
            info_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_CONFIG_BASED_CONFIG_CHANGED")

            # close popup
            return HttpResponse('<script type="text/javascript">window.close();</script>')

        else:
            # show form page again
            return render(
                request,
                'dfirtrack_config/system/system_importer_file_csv_config_based_config_popup.html',
                {
                    'form': form,
                }
            )

    else:

        # get config model
        model = SystemImporterFileCsvConfigbasedConfigModel.objects.get(system_importer_file_csv_configbased_config_name = 'SystemImporterFileCsvConfigbasedConfig')
        # get form
        form = SystemImporterFileCsvConfigbasedConfigForm(instance = model)

    # show form page
    return render(
        request,
        'dfirtrack_config/system/system_importer_file_csv_config_based_config_popup.html',
        {
            'form': form,
        }
    )

@login_required(login_url="/login")
def system_importer_file_csv_form_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        # get config model
        model = SystemImporterFileCsvFormbasedConfigModel.objects.get(system_importer_file_csv_formbased_config_name = 'SystemImporterFileCsvFormbasedConfig')
        # get form
        form = SystemImporterFileCsvFormbasedConfigForm(request.POST, instance = model)

        if form.is_valid():

            # save settings
            model = form.save(commit=False)
            model.save()
            form.save_m2m()

            # call logger
            info_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_FORM_BASED_CONFIG_CHANGED")

            # close popup
            return HttpResponse('<script type="text/javascript">window.close();</script>')

        else:
            # show form page again
            return render(
                request,
                'dfirtrack_config/system/system_importer_file_csv_form_based_config_popup.html',
                {
                    'form': form,
                }
            )

    else:

        # get config model
        model = SystemImporterFileCsvFormbasedConfigModel.objects.get(system_importer_file_csv_formbased_config_name = 'SystemImporterFileCsvFormbasedConfig')
        # get form
        form = SystemImporterFileCsvFormbasedConfigForm(instance = model)

    # show form page
    return render(
        request,
        'dfirtrack_config/system/system_importer_file_csv_form_based_config_popup.html',
        {
            'form': form,
        }
    )
