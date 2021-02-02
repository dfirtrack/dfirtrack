from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_config.forms import SystemImporterFileCsvConfigbasedConfigForm, SystemImporterFileCsvCronbasedConfigForm, SystemImporterFileCsvFormbasedConfigForm
from dfirtrack_config.models import SystemImporterFileCsvConfigbasedConfigModel, SystemImporterFileCsvCronbasedConfigModel, SystemImporterFileCsvFormbasedConfigModel
from dfirtrack_main.logger.default_logger import info_logger
import os

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

            # create message
            messages.success(request, 'System importer file CSV config based config changed')

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
def system_importer_file_csv_cron_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        # get config model
        model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')
        # get form
        form = SystemImporterFileCsvCronbasedConfigForm(request.POST, instance = model)

        if form.is_valid():

            # save settings
            model = form.save(commit=False)
            model.save()
            form.save_m2m()

            # create message
            messages.success(request, 'System importer file CSV cron based config changed')

            # call logger
            info_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_CRON_BASED_CONFIG_CHANGED")

            """ check file system """

            # build csv file path
            csv_path = model.csv_import_path + '/' + model.csv_import_filename

            """
            CSV import path does not exist - handled in dfirtrack_config.form
            CSV import path is not readable - handled in dfirtrack_config.form
            CSV import file does exist but is not readable - handled in dfirtrack_config.form
            """

            # CSV import file does not exist - show warning
            if not os.path.isfile(csv_path):
                # create message
                messages.warning(request, 'CSV import file does not exist at the moment. Make sure the file is available during import.')
            # CSV import file is empty - show warning
            if os.path.getsize(csv_path) == 0:
                # create message
                messages.warning(request, 'CSV import file is empty. Make sure the file contains systems during import.')

            # close popup
            return HttpResponse('<script type="text/javascript">window.close();</script>')

        else:
            # show form page again
            return render(
                request,
                'dfirtrack_config/system/system_importer_file_csv_cron_based_config_popup.html',
                {
                    'form': form,
                }
            )

    else:

        # get config model
        model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')
        # get form
        form = SystemImporterFileCsvCronbasedConfigForm(instance = model)

    # show form page
    return render(
        request,
        'dfirtrack_config/system/system_importer_file_csv_cron_based_config_popup.html',
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

            # create message
            messages.success(request, 'System importer file CSV form based config changed')

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
