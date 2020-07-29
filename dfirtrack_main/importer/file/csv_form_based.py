import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.importer.file.csv_check_data import check_config, check_file, check_row
from dfirtrack_main.importer.file.csv_importer_forms import SystemImporterFileCsvFormbasedForm
from dfirtrack_main.importer.file.csv_messages import final_messages
from dfirtrack_main.importer.file.csv_set_system_attributes import ip_attributes, many_to_many_system_attributes
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import System
from io import TextIOWrapper

@login_required(login_url="/login")
def system(request):

    # form was valid to post
    if request.method == "POST":

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_BEGAN")

        # get text out of file (variable results from request object via file upload field)
        systemcsv = TextIOWrapper(request.FILES['systemcsv'].file, encoding=request.encoding)

        # read rows out of csv
        rows = csv.reader(systemcsv, quotechar="'")

        # check file for csv respectively some kind of text file
        file_check = check_file(request, rows)
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
            if row_counter == 1 and dfirtrack_config.CSV_HEADLINE is True:
                # autoincrement row counter
                row_counter += 1
                # leave loop for headline row
                continue

            # check row for valid system values
            continue_system_importer_file_csv = check_row(request, row, row_counter)
            # leave loop for this row if there are invalid values
            if continue_system_importer_file_csv:
                # autoincrement row counter
                row_counter += 1
                continue

            # get system name (decremented by one because index starts with zero: user provides 1 -> first column in CSV has index 0)
            system_name = row[dfirtrack_config.CSV_COLUMN_SYSTEM - 1]

            # get all systems with this system_name
            systemquery = System.objects.filter(system_name=system_name)

            """ check how many systems were returned """

            # if there is only one system
            if len(systemquery) == 1:

                # skip if system already exists (depending on CSV_SKIP_EXISTING_SYSTEM)
                if dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM:

                    # autoincrement counter
                    systems_skipped_counter += 1
                    # autoincrement row counter
                    row_counter += 1
                    # leave loop
                    continue

                # modify existing system (depending on CSV_SKIP_EXISTING_SYSTEM)
                elif not dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM:

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

                        # save many to many
                        form.save_m2m()
                        # TODO: this way existing many2many relations will be removed in every case
                        ## change many2many (if set via dfirtrack.config)
                        #system = many_to_many_system_attributes(system, request)

                        # set ip addresses (if set via dfirtrack.config)
                        if dfirtrack_config.CSV_CHOICE_IP:
                            system = ip_attributes(system, request, row, row_counter)

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

                    # save many to many
                    form.save_m2m()
                    # TODO: this way existing many2many relations will be removed in every case
                    ## change many2many (if set via dfirtrack.config)
                    #system = many_to_many_system_attributes(system, request)

                    # set ip addresses (if set via dfirtrack.config)
                    if dfirtrack_config.CSV_CHOICE_IP:
                        system = ip_attributes(system, request, row, row_counter)

                    # autoincrement systems_created_counter
                    systems_created_counter += 1

                    # call logger
                    system.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_SYSTEM_CREATED")

            # autoincrement row counter
            row_counter += 1

        # call final messages
        final_messages(request, systems_created_counter, systems_updated_counter, systems_skipped_counter)

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_END")

        return redirect(reverse('system_list'))

    else:

        # check config before showing form
        # TODO: remove after implementing django-constance
        #stop_system_importer_file_csv = check_config(request)

        # leave system_importer_file_csv if variables caused errors
        #if stop_system_importer_file_csv:
            #return redirect(reverse('system_list'))

        # show warning if existing systems will be updated
        if not dfirtrack_config.CSV_SKIP_EXISTING_SYSTEM:
            messages.warning(request, 'WARNING: Existing systems will be updated!')

        # show empty form with default values
        form = SystemImporterFileCsvFormbasedForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })

        # call logger
        debug_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_ENTERED")

    # show form and submit bools from dfirtrack.config needed as variables in template
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_form_based.html',
        {
            'form': form,
        }
    )

# deprecated, TODO: check for useful stuff regarding tag handling
#
#from dfirtrack.config import TAGLIST
#from dfirtrack.config import TAGPREFIX
#
#    """
#    - remove all tags for systems beginning with 'TAGPREFIX' (if there are any)
#    - evaluate given CSV line by line (without first row)
#        - check whether this line has relevant tags (leave loop if not)
#        - add relevant tags to this system
#    """
#
#        # check TAGLIST (from settings.config) for empty list
#        if not TAGLIST:
#            messages.error(request, "No relevant tags defined. Check `TAGLIST` in `dfirtrack.config`!")
#            # call logger
#            error_logger(str(request.user), " SYSTEM_TAG_IMPORTER_NO_TAGS_DEFINED.")
#            return redirect('/system/')
#        else:
#            taglist = TAGLIST
#
#        # check TAGPREFIX (from settings.config) for empty string
#        if TAGPREFIX is "":
#            messages.error(request, "No prefix string defined. Check `TAGPREFIX` in `dfirtrack.config`!")
#            # call logger
#            error_logger(str(request.user), " SYSTEM_TAG_IMPORTER_NO_TAGPREFIX_DEFINED.")
#            return redirect('/system/')
#        # expand the string by an underscore
#        else:
##            tagprefix = TAGPREFIX + "_"
#            tagprefix = TAGPREFIX + "-"
#
#        # create tagaddlist to append for every new system
#        tagaddlist = []
#        for tag in taglist:
#                tagaddlist.append(tagprefix + tag)
#
#        """ remove all tags for systems beginning with 'TAGPREFIX' (if there are any) """
#
#        # get all systems that have tags beginning with 'TAGPREFIX' | prefixtagsystems -> queryset
#        prefixtagsystems=System.objects.filter(tag__tag_name__startswith=tagprefix)
#
#        # iterate over systems in queryset | prefixtagsystem  -> system object
#        for prefixtagsystem in prefixtagsystems:
#
#            # get all tags beginning with 'TAGPREFIX' that belong to the actual system | systemprefixtags -> queryset
#            systemprefixtags=prefixtagsystem.tag.filter(tag_name__startswith=tagprefix)
#
#            # iterate over queryset | systemprefixtag -> tag object
#            for systemprefixtag in systemprefixtags:
#                # delete all existing tags (the m2m relationship) beginning with 'TAGPREFIX' for this system (so that removed tags from csv will be removed as well)
#                systemprefixtag.system_set.remove(prefixtagsystem)
#
#            # get tags from csv
#            tagcsvstring = row[9]
#            if tagcsvstring == '':
#                # autoincrement systems_skipped_counter
#                systems_skipped_counter += 1
#                # autoincrement row_counter
#                row_counter += 1
#                # leave because systems without tags are not relevant
#                continue
#            else:
#                # convert string (at whitespaces) to list
#                tagcsvlist = tagcsvstring.split()
#
#            # create empty list for mapping
#            tagaddlist = []
#            # check for relevant tags and add to list
#            for tag in taglist:
#                if tag in tagcsvlist:
#                    tagaddlist.append(tagprefix + tag)
#
#            # check if tagaddlist is empty
#            if not tagaddlist:
#                # autoincrement systems_skipped_counter
#                systems_skipped_counter += 1
#                # autoincrement row_counter
#                row_counter += 1
#                # leave because there are no relevant tags
#                continue
#
#                if not row[10]:
#                    # continue if there is an empty string
#                    pass
#                else:
#                    # get object
#                    tag_error = Tag.objects.get(tag_name=tagprefix + 'Error')
#                    # add error tag to system
#                    tag_error.system_set.add(system)
#
#                # iterate over tags in tagaddlist
#                for tag_name in tagaddlist:
#                    # get object
#                    tag = Tag.objects.get(tag_name=tag_name)
#                    # add tag to system
#                    tag.system_set.add(system)
#                # get tagcolor object
#                tagcolor = Tagcolor.objects.get(tagcolor_name='primary')
#
#                # create tag if needed
#                tag, created = Tag.objects.get_or_create(tag_name=tag_name, tagcolor=tagcolor)
#                # call logger if created
#                if created == True:
#                    tag.logger(str(request.user), " SYSTEMS_TAG_IMPORTER_TAG_CREATED")
#                    messages.success(request, 'Tag "' + tag.tag_name + '" created.')
#
#                # add tag to system
#                tag.system_set.add(system)
