import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from dfirtrack_config.models import SystemImporterFileCsvFormbasedConfigModel
from dfirtrack_main.importer.file.csv_check_data import check_config, check_file, check_row
from dfirtrack_main.importer.file.csv_importer_forms import SystemImporterFileCsvFormbasedForm
from dfirtrack_main.importer.file.csv_messages import final_messages
from dfirtrack_main.importer.file.csv_set_system_attributes import case_attributes_form_based, company_attributes_form_based, ip_attributes, tag_attributes_form_based
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import System
from io import TextIOWrapper

@login_required(login_url="/login")
def system(request):

    # get config model
    model = SystemImporterFileCsvFormbasedConfigModel.objects.get(system_importer_file_csv_formbased_config_name = 'SystemImporterFileCsvFormbasedConfig')

    # form was valid to post
    if request.method == "POST":

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_BEGAN")

        # get systemcsv from request (no submitted file only relevant for tests, normally form enforces file submitting)
        check_systemcsv = request.FILES.get('systemcsv', False)

        # check request for systemcsv (file submitted)
        if check_systemcsv:

            # get text out of file (variable results from request object via file upload field)
            systemcsv = TextIOWrapper(request.FILES['systemcsv'].file, encoding=request.encoding)

            # read rows out of csv
            rows = csv.reader(systemcsv, quotechar="'")

            # check file for csv respectively some kind of text file
            file_check = check_file(rows, str(request.user))

            # leave system_importer_file_csv if file check throws errors
            if not file_check:
                return redirect(reverse('system_list'))
            # jump to begin of file again after iterating in file check
            systemcsv.seek(0)

            """ prepare and start loop """

            # set row_counter (needed for logger)
            row_counter = 1

            # set systems_created_counter (needed for messages)
            systems_created_counter = 0

            # set systems_updated_counter (needed for messages)
            systems_updated_counter = 0

            # set systems_skipped_counter (needed for messages)
            systems_skipped_counter = 0

            # iterate over rows
            for row in rows:

                # skip first row in case of headline
                if row_counter == 1 and model.csv_headline is True:
                    # autoincrement row counter
                    row_counter += 1
                    # leave loop for headline row
                    continue

                # check row for valid system values
                continue_system_importer_file_csv = check_row(request, row, row_counter, model)
                # leave loop for this row if there are invalid values
                if continue_system_importer_file_csv:
                    # autoincrement row counter
                    row_counter += 1
                    continue

                # get system name (decremented by one because index starts with zero: user provides 1 -> first column in CSV has index 0)
                system_name = row[model.csv_column_system - 1]

                # get all systems with this system_name
                systemquery = System.objects.filter(system_name=system_name)

                """ check how many systems were returned """

                # if there is only one system
                if len(systemquery) == 1:

                    # skip if system already exists (depending on CSV_SKIP_EXISTING_SYSTEM)
                    if model.csv_skip_existing_system:

                        # autoincrement counter
                        systems_skipped_counter += 1
                        # autoincrement row counter
                        row_counter += 1
                        # leave loop
                        continue

                    # modify existing system (depending on CSV_SKIP_EXISTING_SYSTEM)
                    elif not model.csv_skip_existing_system:

                        # get existing system object
                        system = System.objects.get(system_name=system_name)

                        # create form with request data
                        form = SystemImporterFileCsvFormbasedForm(request.POST, request.FILES, instance=system)

                        # change system
                        if form.is_valid():

                            # don't save form yet
                            system = form.save(commit=False)

                            # change mandatory meta attributes
                            system.system_modify_time = timezone.now()
                            system.system_modified_by_user_id = request.user

                            # save object
                            system.save()

                            # change many2many (classic 'form.save_m2m()' would remove existing relationships regardless config)
                            system = case_attributes_form_based(system, request.POST.getlist('case'), model)
                            system = company_attributes_form_based(system, request.POST.getlist('company'), model)
                            system = tag_attributes_form_based(system, request.POST.getlist('tag'), model)

                            # change ip addresses
                            if model.csv_choice_ip:
                                system = ip_attributes(system, request, row, row_counter, model)

                            # autoincrement systems_updated_counter
                            systems_updated_counter += 1

                            # call logger
                            system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_MODIFIED")

                # if there is more than one system
                elif len(systemquery) > 1:
                    messages.error(request, "System " + system_name + " already exists multiple times. Nothing was changed for this system.")

                # if there is no system
                else:

                    # create form with request data
                    form = SystemImporterFileCsvFormbasedForm(request.POST, request.FILES)

                    # create system
                    if form.is_valid():

                        # create new system object
                        system = System()

                        # don't save form yet
                        system = form.save(commit=False)

                        # add system_name from csv
                        system.system_name = system_name

                        # add mandatory meta attributes
                        system.system_modify_time = timezone.now()
                        system.system_created_by_user_id = request.user
                        system.system_modified_by_user_id = request.user

                        # save object
                        system.save()

                        # add many2many
                        system = case_attributes_form_based(system, request.POST.getlist('case'), model)
                        system = company_attributes_form_based(system, request.POST.getlist('company'), model)
                        system = tag_attributes_form_based(system, request.POST.getlist('tag'), model)

                        # add ip addresses
                        if model.csv_choice_ip:
                            system = ip_attributes(system, request, row, row_counter, model)

                        # autoincrement systems_created_counter
                        systems_created_counter += 1

                        # call logger
                        system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_CREATED")

                # autoincrement row counter
                row_counter += 1

        # check request for systemcsv (file not submitted)
        else:

            # get empty form with default values
            form = SystemImporterFileCsvFormbasedForm(initial={
                'systemstatus': 2,
                'analysisstatus': 1,
            })

            # show form again
            return render(
                request,
                'dfirtrack_main/system/system_importer_file_csv_form_based.html',
                {
                    'form': form,
                }
            )

        # call final messages
        final_messages(request, systems_created_counter, systems_updated_counter, systems_skipped_counter)

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END")

        return redirect(reverse('system_list'))

    else:

        # get config model
        model = SystemImporterFileCsvFormbasedConfigModel.objects.get(system_importer_file_csv_formbased_config_name = 'SystemImporterFileCsvFormbasedConfig')

        # check config before showing form
        stop_system_importer_file_csv = check_config(request, model)

        # leave system_importer_file_csv if variables caused errors
        if stop_system_importer_file_csv:
            return redirect(reverse('system_list'))

        # show warning if existing systems will be updated
        if not model.csv_skip_existing_system:
            messages.warning(request, 'WARNING: Existing systems will be updated!')

        # get empty form with default values
        form = SystemImporterFileCsvFormbasedForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_ENTERED")

    # show form
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_form_based.html',
        {
            'form': form,
        }
    )
