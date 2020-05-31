from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
import dfirtrack.config as dfirtrack_config
from .filesystem_check_data import check_config
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import Headline, Reportitem, System
import os.path

@login_required(login_url="/login")
def reportitem(request):
    """ this function checks for every system the existence of a markdown file with information about system the and imports the content of this file as reportitem for the corresponding system """

    # call logger
    debug_logger(str(request.user), " REPORTITEM_FILESYSTEM_IMPORTER_BEGIN")

    # check config before continuing
    stop_reportitem_importer_file_filesystem = check_config(request)

    # leave reportitem_importer_file_filesystem if variables caused errors
    if stop_reportitem_importer_file_filesystem:
        return redirect(reverse('system_list'))

    # get all system objects
    systems = System.objects.all()

    # create headline if it does not exist
    headline, created = Headline.objects.get_or_create(headline_name=dfirtrack_config.REPORTITEM_HEADLINE)
    if created == True:
        # call logger
        headline.logger(str(request.user), " REPORTITEM_FILESYSTEM_IMPORTER_HEADLINE_CREATED")

    # set counter for non-existing files (needed for messages)
    nofile_found_counter = 0

    # set counter for created reportitems (needed for messages)
    reportitems_created_counter = 0

    # set counter for modified reportitems (needed for messages)
    reportitems_modified_counter = 0

    # set counter for deleted reportitems (needed for messages)
    reportitems_deleted_counter = 0

    # iterate over systems
    for system in systems:

        # create path for reportfile
        reportpath = dfirtrack_config.REPORTITEM_FILESYSTEMPATH + "/" + system.system_name + ".md"

        # check whether a file is existing for this system
        if not os.path.isfile(reportpath):
            # call logger
            warning_logger(str(request.user), " REPORTITEM_FILESYSTEM_IMPORTER_NO_FILE system_name:" + system.system_name)
            # autoincrement counter
            nofile_found_counter += 1

            # check whether already existing reportitem for this system should be deleted if no file was provided
            if dfirtrack_config.REPORTITEM_DELETE:
                # delete already existing reportitem for this system if no file was provided
                try:
                    reportitem = Reportitem.objects.get(system = system, headline = headline, reportitem_subheadline = dfirtrack_config.REPORTITEM_SUBHEADLINE)
                    # call logger (before deleting instance)
                    reportitem.logger(str(request.user), " REPORTITEM_FILESYSTEM_IMPORTER_REPORTITEM_DELETED")
                    reportitem.delete()
                    # autoincrement counter
                    reportitems_deleted_counter += 1
                except Reportitem.DoesNotExist:
                    pass

            # continue with next system
            continue

        # create reportitem if it does not exist (get_or_create won't work in this context because of needed user objects for saving)
        try:
            reportitem = Reportitem.objects.get(system = system, headline = headline, reportitem_subheadline = dfirtrack_config.REPORTITEM_SUBHEADLINE)
            reportitems_modified_counter += 1
        except Reportitem.DoesNotExist:
            reportitem = Reportitem()
            reportitems_created_counter += 1
            reportitem.system = system
            reportitem.headline = headline
            reportitem.reportitem_subheadline = dfirtrack_config.REPORTITEM_SUBHEADLINE
            reportitem.reportitem_created_by_user_id = request.user

        # open file
        reportfile = open(reportpath, "r")
        # add changing values (existing reportitem_note will be overwritten)
        reportitem.reportitem_note = reportfile.read()
        # close file
        reportfile.close()
        reportitem.reportitem_modified_by_user_id = request.user
        reportitem.save()

        # call logger
        reportitem.logger(str(request.user), " REPORTITEM_FILESYSTEM_IMPORTER_REPORTITEM_CREATED_OR_MODIFIED")

    # call final messages
    if nofile_found_counter > 0:
        if nofile_found_counter == 1:
            messages.warning(request, "No file was found for " + str(nofile_found_counter) + " system.")
        else:
            messages.warning(request, "No files were found for " + str(nofile_found_counter) + " systems.")
    if reportitems_created_counter > 0:
        if reportitems_created_counter  == 1:
            messages.success(request, str(reportitems_created_counter) + ' reportitem was created.')
        else:
            messages.success(request, str(reportitems_created_counter) + ' reportitems were created.')
    if reportitems_modified_counter > 0:
        if reportitems_modified_counter  == 1:
            messages.success(request, str(reportitems_modified_counter) + ' reportitem was modified.')
        else:
            messages.success(request, str(reportitems_modified_counter) + ' reportitems were modified.')
    if reportitems_deleted_counter > 0:
        if reportitems_deleted_counter  == 1:
            messages.success(request, str(reportitems_deleted_counter) + ' reportitem was deleted.')
        else:
            messages.success(request, str(reportitems_deleted_counter) + ' reportitems were deleted.')

    return redirect(reverse('system_list'))
