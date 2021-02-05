from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.importer.file.csv_import import system_handler
from dfirtrack_main.importer.file.csv_importer_forms import SystemImporterFileCsvForm
from dfirtrack_main.logger.default_logger import debug_logger


@login_required(login_url="/login")
def system_instant(request):
    """  CSV import via button, file is on server file system """

    # call CSV importer
    system_handler(request)

    # return
    return redirect(reverse('system_list'))

def system_cron():
    """  CSV import via scheduled task, file is on server file system """

    # call CSV importer
    system_handler()

@login_required(login_url="/login")
def system_upload(request):
    """  CSV import via upload form, file is on user system  """

    # POST request
    if request.method == "POST":

        # get systemcsv from request (no submitted file only relevant for tests, normally form enforces file submitting)
        check_systemcsv = request.FILES.get('systemcsv', False)

        # check request for systemcsv (file submitted - no submitted file only relevant for tests, normally form enforces file submitting)
        if check_systemcsv:

            # call CSV importer
            system_handler(request, True)

        # check request for systemcsv (file not submitted - no submitted file only relevant for tests, normally form enforces file submitting)
        else:

            # get empty form
            form = SystemImporterFileCsvForm()

            # show form again
            return render(
                request,
                'dfirtrack_main/system/system_importer_file_csv.html',
                {
                    'form': form,
                }
            )

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END")

        return redirect(reverse('system_list'))

    # GET request
    else:

        # TODO: [config] csv_check_data.check_config:
        # TODO: [config] check the existing configuration for logic errors
        # TODO: [config] like the field validation in dfirtrack_config.forms.SystemImporterFileCsvConfigForm

        # get config model
        model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name = 'SystemImporterFileCsvConfig')

        # show warning if existing systems will be updated
        if not model.csv_skip_existing_system:
            messages.warning(request, 'WARNING: Existing systems will be updated!')

        # get empty form
        form = SystemImporterFileCsvForm()

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_CRON_ENTERED")

    # show form
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv.html',
        {
            'form': form,
        }
    )
