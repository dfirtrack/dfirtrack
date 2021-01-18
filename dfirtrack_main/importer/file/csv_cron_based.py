import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from dfirtrack_config.models import SystemImporterFileCsvConfigbasedConfigModel, SystemImporterFileCsvCronbasedConfigModel
from dfirtrack_main.importer.file.csv_check_data import check_config, check_file, check_row
from dfirtrack_main.importer.file.csv_importer_forms import SystemImporterFileCsvConfigbasedForm
from dfirtrack_main.importer.file.csv_messages import final_messages
from dfirtrack_main.importer.file.csv_set_system_attributes import case_attributes_config_based, company_attributes_config_based, ip_attributes, optional_system_attributes, tag_attributes_config_based
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import System
from io import TextIOWrapper

@login_required(login_url="/login")
def config_check(request):

    # reset stop condition
    stop_system_importer_file_csv_cronbased = False

    # get config model
    model = SystemImporterFileCsvCronbasedConfigModel.objects.get(system_importer_file_csv_cronbased_config_name = 'SystemImporterFileCsvCronbasedConfig')

    # check for csv_import_username (after initial migration w/o user defined)
    if not model.csv_import_username:
        messages.error(request, "No user for import defined. Check config!")
        # set stop condition
        stop_system_importer_file_csv_cronbased = True

    # TODO: add check for csv_import_path is readable

    # check stop condition
    if stop_system_importer_file_csv_cronbased:
        # return to system list
        return redirect(reverse('system_list'))
    else:
        # TODO: build url with python
        # TODO: open in new tab
        # open django admin with pre-filled form for scheduled task
        return redirect('/admin/django_q/schedule/add/?name=system_importer_file_csv_cron_based&func=dfirtrack_main.importer.file.csv_cron_based.system')

@login_required(login_url="/login")
def system(request):
    pass

#    # get config model
#    model = SystemImporterFileCsvConfigbasedConfigModel.objects.get(system_importer_file_csv_configbased_config_name = 'SystemImporterFileCsvConfigbasedConfig')
#
#    # form was valid to post
#    if request.method == "POST":
#
#        # call logger
#        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_BEGAN")
#
#        # get systemcsv from request (no submitted file only relevant for tests, normally form enforces file submitting)
#        check_systemcsv = request.FILES.get('systemcsv', False)
#
#        # check request for systemcsv (file submitted)
#        if check_systemcsv:
#
#            # get text out of file (variable results from request object via file upload field)
#            systemcsv = TextIOWrapper(request.FILES['systemcsv'].file, encoding=request.encoding)
#
#            # read rows out of csv
#            rows = csv.reader(systemcsv, quotechar="'")
#
#            # check file for csv respectively some kind of text file
#            file_check = check_file(request, rows)
#
#            # leave system_importer_file_csv if file check throws errors
#            if not file_check:
#                return redirect(reverse('system_list'))
#            # jump to begin of file again after iterating in file check
#            systemcsv.seek(0)
#
#            """ prepare and start loop """
#
#            # set row_counter (needed for logger)
#            row_counter = 1
#
#            # set systems_created_counter (needed for messages)
#            systems_created_counter = 0
#
#            # set systems_updated_counter (needed for messages)
#            systems_updated_counter = 0
#
#            # set systems_skipped_counter (needed for messages)
#            systems_skipped_counter = 0
#
#            # iterate over rows
#            for row in rows:
#
#                # skip first row in case of headline
#                if row_counter == 1 and model.csv_headline is True:
#                    # autoincrement row counter
#                    row_counter += 1
#                    # leave loop for headline row
#                    continue
#
#                # check row for valid system values
#                continue_system_importer_file_csv = check_row(request, row, row_counter, model)
#                # leave loop for this row if there are invalid values
#                if continue_system_importer_file_csv:
#                    # autoincrement row counter
#                    row_counter += 1
#                    continue
#
#                # get system name (decremented by one because index starts with zero: user provides 1 -> first column in CSV has index 0)
#                system_name = row[model.csv_column_system - 1]
#
#                # get all systems with this system_name
#                systemquery = System.objects.filter(system_name=system_name)
#
#                """ check how many systems were returned """
#
#                # if there is only one system
#                if len(systemquery) == 1:
#
#                    # skip if system already exists (depending on CSV_SKIP_EXISTING_SYSTEM)
#                    if model.csv_skip_existing_system:
#
#                        # autoincrement counter
#                        systems_skipped_counter += 1
#                        # autoincrement row counter
#                        row_counter += 1
#                        # leave loop
#                        continue
#
#                    # modify existing system (depending on CSV_SKIP_EXISTING_SYSTEM)
#                    elif not model.csv_skip_existing_system:
#
#                        # get existing system object
#                        system = System.objects.get(system_name=system_name)
#
#                        # change attributes
#                        system = optional_system_attributes(system, model)
#
#                        # change mandatory meta attributes
#                        system.system_modify_time = timezone.now()
#                        system.system_modified_by_user_id = request.user
#
#                        # save object
#                        system.save()
#
#                        # change many2many
#                        system = case_attributes_config_based(system, model.csv_default_case, model)
#                        system = company_attributes_config_based(system, model.csv_default_company, model)
#                        system = tag_attributes_config_based(system, model.csv_default_tag, model)
#
#                        # change ip addresses
#                        if model.csv_choice_ip:
#                            system = ip_attributes(system, request, row, row_counter, model)
#
#                        # autoincrement systems_updated_counter
#                        systems_updated_counter += 1
#
#                        # call logger
#                        system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_MODIFIED")
#
#                # if there is more than one system
#                elif len(systemquery) > 1:
#                    messages.error(request, "System " + system_name + " already exists multiple times. Nothing was changed for this system.")
#
#                # if there is no system
#                else:
#
#                    # create new system object
#                    system = System()
#
#                    # add system_name from csv
#                    system.system_name = system_name
#
#                    # add attributes
#                    system = optional_system_attributes(system, model)
#
#                    # add mandatory meta attributes
#                    system.system_modify_time = timezone.now()
#                    system.system_created_by_user_id = request.user
#                    system.system_modified_by_user_id = request.user
#
#                    # save object
#                    system.save()
#
#                    # add many2many
#                    system = case_attributes_config_based(system, model.csv_default_case, model)
#                    system = company_attributes_config_based(system, model.csv_default_company, model)
#                    system = tag_attributes_config_based(system, model.csv_default_tag, model)
#
#                    # add ip addresses
#                    if model.csv_choice_ip:
#                        system = ip_attributes(system, request, row, row_counter, model)
#
#                    # autoincrement systems_created_counter
#                    systems_created_counter += 1
#
#                    # call logger
#                    system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_CREATED")
#
#                # autoincrement row counter
#                row_counter += 1
#
#        # check request for systemcsv (file not submitted)
#        else:
#
#            # get empty form
#            form = SystemImporterFileCsvConfigbasedForm()
#
#            # show form again
#            return render(
#                request,
#                'dfirtrack_main/system/system_importer_file_csv_config_based.html',
#                {
#                    'form': form,
#                }
#            )
#
#        # call final messages
#        final_messages(request, systems_created_counter, systems_updated_counter, systems_skipped_counter)
#
#        # call logger
#        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END")
#
#        return redirect(reverse('system_list'))
#
#    else:
#
#        # get config model
#        model = SystemImporterFileCsvConfigbasedConfigModel.objects.get(system_importer_file_csv_configbased_config_name = 'SystemImporterFileCsvConfigbasedConfig')
#
#        # check config before showing form
#        stop_system_importer_file_csv = check_config(request, model)
#
#        # leave system_importer_file_csv if variables caused errors
#        if stop_system_importer_file_csv:
#            return redirect(reverse('system_list'))
#
#        # show warning if existing systems will be updated
#        if not model.csv_skip_existing_system:
#            messages.warning(request, 'WARNING: Existing systems will be updated!')
#
#        # get empty form
#        form = SystemImporterFileCsvConfigbasedForm()
#
#        # call logger
#        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_ENTERED")
#
#    # show form
#    return render(
#        request,
#        'dfirtrack_main/system/system_importer_file_csv_config_based.html',
#        {
#            'form': form,
#        }
#    )
