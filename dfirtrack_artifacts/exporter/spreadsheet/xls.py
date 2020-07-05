from constance import config as constance_config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_main.exporter.spreadsheet.xls import style_default, style_headline, write_row
from dfirtrack_main.logger.default_logger import info_logger, warning_logger
from .spreadsheet_check_data import check_config, check_worksheet, check_artifactstatus
from time import strftime
import xlwt

@login_required(login_url="/login")
def artifact(request):

    # check_config
    stop_artifact_exporter_spreadsheet = check_config(request)

    # check_config regarding worksheet variables (only xls exporter)
    stop_artifact_exporter_spreadsheet_worksheet = check_worksheet(request)

    # check_config regarding choosen artifactstatus
    stop_artifact_exporter_spreadsheet_artifactstatus = check_artifactstatus(request)

    # leave artifact_exporter_spreadsheet_xls if variables caused errors
    if stop_artifact_exporter_spreadsheet or stop_artifact_exporter_spreadsheet_worksheet or stop_artifact_exporter_spreadsheet_artifactstatus:

        # call logger
        warning_logger(str(request.user), " ARTIFACT_EXPORTER_SPREADSHEET_XLS_END_WITH_ERRORS")
        return redirect(reverse('artifacts_artifact_list'))

    """ prepare file including formatting """

    # create xls MIME type object
    artifactlist = HttpResponse(content_type='application/ms-excel')

    # define filename
    artifactlist['Content-Disposition'] = 'attachment; filename="artifactlist.xls"'

    # create workbook object with UTF-8 encoding
    workbook = xlwt.Workbook(encoding='utf-8')
    # define name of worksheet within file
    worksheet_artifact = workbook.add_sheet('artifacts')

    # define styling for headline
    style = style_headline()

    """ start with headline """

    # set counter
    row_num = 0

    # create empty list
    headline = []

    # check for attribute id
    if constance_config.ARTIFACTLIST_ARTIFACT_ID:
        headline.append('Artifact ID')

    # append mandatory attribute
    headline.append('Artifact')

    # check for remaining attributes
    if constance_config.ARTIFACTLIST_SYSTEM_ID:
        headline.append('System ID')
    if constance_config.ARTIFACTLIST_SYSTEM_NAME:
        headline.append('System')
    if constance_config.ARTIFACTLIST_ARTIFACTSTATUS:
        headline.append('Artifactstatus')
    if constance_config.ARTIFACTLIST_ARTIFACTTYPE:
        headline.append('Artifacttype')
    if constance_config.ARTIFACTLIST_ARTIFACT_SOURCE_PATH:
        headline.append('Source path')
    if constance_config.ARTIFACTLIST_ARTIFACT_STORAGE_PATH:
        headline.append('Storage path')
    if constance_config.ARTIFACTLIST_ARTIFACT_NOTE:
        headline.append('Note')
    if constance_config.ARTIFACTLIST_ARTIFACT_MD5:
        headline.append('MD5')
    if constance_config.ARTIFACTLIST_ARTIFACT_SHA1:
        headline.append('SHA1')
    if constance_config.ARTIFACTLIST_ARTIFACT_SHA256:
        headline.append('SHA256')
    if constance_config.ARTIFACTLIST_ARTIFACT_CREATE_TIME:
        headline.append('Created')
    if constance_config.ARTIFACTLIST_ARTIFACT_MODIFY_TIME:
        headline.append('Modified')

    # write headline
    worksheet_artifact = write_row(worksheet_artifact, headline, row_num, style)

    # clear styling to default
    style = style_default()

    """ append artifacts """

    # get all Artifact objects ordered by system name (fk) and artifact id
    artifacts = Artifact.objects.all().order_by("system__system_name", "artifact_id")

    # iterate over artifacts
    for artifact in artifacts:

        # autoincrement row counter
        row_num += 1

        # set column counter
        col_num = 1

        # create empty list for line
        entryline = []

        """ check for attribute """

        # artifact id
        if constance_config.ARTIFACTLIST_ARTIFACT_ID:
            entryline.append(artifact.artifact_id)

        """ append mandatory attribute """

        # artifact name
        entryline.append(artifact.artifact_name)

        """ check for remaining attributes """

        # system id
        if constance_config.ARTIFACTLIST_SYSTEM_ID:
            entryline.append(artifact.system.system_id)
        # system name
        if constance_config.ARTIFACTLIST_SYSTEM_NAME:
            entryline.append(artifact.system.system_name)
        # artifactstatus
        if constance_config.ARTIFACTLIST_ARTIFACTSTATUS:
            entryline.append(artifact.artifactstatus.artifactstatus_name)
        # artifacttype
        if constance_config.ARTIFACTLIST_ARTIFACTTYPE:
            entryline.append(artifact.artifacttype.artifacttype_name)
        # artifact source path
        if constance_config.ARTIFACTLIST_ARTIFACT_SOURCE_PATH:
            if artifact.artifact_source_path == None:
                artifact_source_path = ''
            else:
                artifact_source_path = artifact.artifact_source_path
            entryline.append(artifact_source_path)
        # artifact storage path
        if constance_config.ARTIFACTLIST_ARTIFACT_STORAGE_PATH:
            if artifact.artifact_storage_path == None:
                artifact_storage_path = ''
            else:
                artifact_storage_path = artifact.artifact_storage_path
            entryline.append(artifact_storage_path)
        # artifact note
        if constance_config.ARTIFACTLIST_ARTIFACT_NOTE:
            if artifact.artifact_note == None:
                artifact_note = ''
            else:
                artifact_note = artifact.artifact_note
            entryline.append(artifact_note)
        # artifact md5
        if constance_config.ARTIFACTLIST_ARTIFACT_MD5:
            if artifact.artifact_md5 == None:
                artifact_md5 = ''
            else:
                artifact_md5 = artifact.artifact_md5
            entryline.append(artifact_md5)
        # artifact sha1
        if constance_config.ARTIFACTLIST_ARTIFACT_SHA1:
            if artifact.artifact_sha1 == None:
                artifact_sha1 = ''
            else:
                artifact_sha1 = artifact.artifact_sha1
            entryline.append(artifact_sha1)
        # artifact sha256
        if constance_config.ARTIFACTLIST_ARTIFACT_SHA256:
            if artifact.artifact_sha256 == None:
                artifact_sha256 = ''
            else:
                artifact_sha256 = artifact.artifact_sha256
            entryline.append(artifact_sha256)
        # artifact create time
        if constance_config.ARTIFACTLIST_ARTIFACT_CREATE_TIME:
            artifact_create_time = artifact.artifact_create_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(artifact_create_time)
        # artifact modify time
        if constance_config.ARTIFACTLIST_ARTIFACT_MODIFY_TIME:
            artifact_modify_time = artifact.artifact_modify_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(artifact_modify_time)

        # write line for artifact
        worksheet_artifact = write_row(worksheet_artifact, entryline, row_num, style)

    # write an empty row
    row_num += 2

    # write meta information for file creation
    actualtime = strftime('%Y-%m-%d %H:%M')
    worksheet_artifact.write(row_num, 0, 'Artifactlist created:', style)
    worksheet_artifact.write(row_num, 1, actualtime, style)
    row_num += 1
    creator = str(request.user)
    worksheet_artifact.write(row_num, 0, 'Created by:', style)
    worksheet_artifact.write(row_num, 1, creator, style)

    """ add worksheet for artifactstatus """

    # check all conditions
    if constance_config.ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS and constance_config.ARTIFACTLIST_ARTIFACTSTATUS and Artifactstatus.objects.count() != 0:

        # define name of worksheet within file
        worksheet_artifactstatus = workbook.add_sheet('artifactstatus')

        # create empty list
        headline_artifactstatus = []

        # append attributes
        headline_artifactstatus.append('ID')
        headline_artifactstatus.append('Artifactstatus')
        headline_artifactstatus.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_artifactstatus = write_row(worksheet_artifactstatus, headline_artifactstatus, row_num, style)

        # clear styling to default
        style = style_default()

        """ append artifactstatus """

        # get all Artifactstatus objects ordered by artifactstatus_id
        artifactstatuss = Artifactstatus.objects.all().order_by("artifactstatus_id")

        # iterate over artifactstatus
        for artifactstatus in artifactstatuss:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_artifactstatus = []

            entryline_artifactstatus.append(artifactstatus.artifactstatus_id)
            entryline_artifactstatus.append(artifactstatus.artifactstatus_name)
            # add placeholder if artifactstatus note does not exist
            if artifactstatus.artifactstatus_note:
                entryline_artifactstatus.append(artifactstatus.artifactstatus_note)
            else:
                entryline_artifactstatus.append('---')

            # write line for artifactstatus
            worksheet_artifactstatus = write_row(worksheet_artifactstatus, entryline_artifactstatus, row_num, style)

    """ add worksheet for artifacttype """

    # check all conditions
    if constance_config.ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE and constance_config.ARTIFACTLIST_ARTIFACTTYPE and Artifacttype.objects.count() != 0:

        # define name of worksheet within file
        worksheet_artifacttype = workbook.add_sheet('artifacttype')

        # create empty list
        headline_artifacttype = []

        # append attributes
        headline_artifacttype.append('ID')
        headline_artifacttype.append('Artifacttype')
        headline_artifacttype.append('Note')

        # define styling for headline
        style = style_headline()

        # set counter
        row_num = 0

        # write headline
        worksheet_artifacttype = write_row(worksheet_artifacttype, headline_artifacttype, row_num, style)

        # clear styling to default
        style = style_default()

        """ append artifacttype """

        # get all Artifacttype objects ordered by artifacttype_name
        artifacttypes = Artifacttype.objects.all().order_by("artifacttype_name")

        # iterate over artifacttype
        for artifacttype in artifacttypes:

            # autoincrement row counter
            row_num += 1

            # set column counter
            col_num = 1

            # create empty list for line
            entryline_artifacttype = []

            entryline_artifacttype.append(artifacttype.artifacttype_id)
            entryline_artifacttype.append(artifacttype.artifacttype_name)
            # add placeholder if artifacttype note does not exist
            if artifacttype.artifacttype_note:
                entryline_artifacttype.append(artifacttype.artifacttype_note)
            else:
                entryline_artifacttype.append('---')

            # write line for artifacttype
            worksheet_artifacttype = write_row(worksheet_artifacttype, entryline_artifacttype, row_num, style)

    # close file
    workbook.save(artifactlist)

    # call logger
    info_logger(str(request.user), " ARTIFACT_XLS_CREATED")

    # return xls object
    return artifactlist
