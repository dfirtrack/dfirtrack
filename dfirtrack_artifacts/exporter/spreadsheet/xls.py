from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_config.models import ArtifactExporterSpreadsheetXlsConfigModel
from dfirtrack_main.exporter.spreadsheet.xls import style_default, style_headline, write_row
from dfirtrack_main.logger.default_logger import info_logger
from time import strftime
import xlwt

@login_required(login_url="/login")
def artifact(request):

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

    # get config model
    model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(artifact_exporter_spreadsheet_xls_config_name = 'ArtifactExporterSpreadsheetXlsConfig')

    """ start with headline """

    # set counter
    row_num = 0

    # create empty list
    headline = []

    # check for attribute id
    if model.artifactlist_xls_artifact_id:
        headline.append('Artifact ID')

    # append mandatory attribute
    headline.append('Artifact')

    # check for remaining attributes
    if model.artifactlist_xls_system_id:
        headline.append('System ID')
    if model.artifactlist_xls_system_name:
        headline.append('System')
    if model.artifactlist_xls_artifactstatus:
        headline.append('Artifactstatus')
    if model.artifactlist_xls_artifacttype:
        headline.append('Artifacttype')
    if model.artifactlist_xls_artifact_source_path:
        headline.append('Source path')
    if model.artifactlist_xls_artifact_storage_path:
        headline.append('Storage path')
    if model.artifactlist_xls_artifact_note:
        headline.append('Note')
    if model.artifactlist_xls_artifact_md5:
        headline.append('MD5')
    if model.artifactlist_xls_artifact_sha1:
        headline.append('SHA1')
    if model.artifactlist_xls_artifact_sha256:
        headline.append('SHA256')
    if model.artifactlist_xls_artifact_create_time:
        headline.append('Created')
    if model.artifactlist_xls_artifact_modify_time:
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

        # leave loop if artifactstatus of this artifact is not configured for export
        if artifact.artifactstatus not in model.artifactlist_xls_choice_artifactstatus.all():
            continue

        # autoincrement row counter
        row_num += 1

        # set column counter
        col_num = 1

        # create empty list for line
        entryline = []

        """ check for attribute """

        # artifact id
        if model.artifactlist_xls_artifact_id:
            entryline.append(artifact.artifact_id)

        """ append mandatory attribute """

        # artifact name
        entryline.append(artifact.artifact_name)

        """ check for remaining attributes """

        # system id
        if model.artifactlist_xls_system_id:
            entryline.append(artifact.system.system_id)
        # system name
        if model.artifactlist_xls_system_name:
            entryline.append(artifact.system.system_name)
        # artifactstatus
        if model.artifactlist_xls_artifactstatus:
            entryline.append(artifact.artifactstatus.artifactstatus_name)
        # artifacttype
        if model.artifactlist_xls_artifacttype:
            entryline.append(artifact.artifacttype.artifacttype_name)
        # artifact source path
        if model.artifactlist_xls_artifact_source_path:
            if artifact.artifact_source_path == None:
                artifact_source_path = ''
            else:
                artifact_source_path = artifact.artifact_source_path
            entryline.append(artifact_source_path)
        # artifact storage path
        if model.artifactlist_xls_artifact_storage_path:
            if artifact.artifact_storage_path == None:
                artifact_storage_path = ''
            else:
                artifact_storage_path = artifact.artifact_storage_path
            entryline.append(artifact_storage_path)
        # artifact note
        if model.artifactlist_xls_artifact_note:
            if artifact.artifact_note == None:
                artifact_note = ''
            else:
                artifact_note = artifact.artifact_note
            entryline.append(artifact_note)
        # artifact md5
        if model.artifactlist_xls_artifact_md5:
            if artifact.artifact_md5 == None:
                artifact_md5 = ''
            else:
                artifact_md5 = artifact.artifact_md5
            entryline.append(artifact_md5)
        # artifact sha1
        if model.artifactlist_xls_artifact_sha1:
            if artifact.artifact_sha1 == None:
                artifact_sha1 = ''
            else:
                artifact_sha1 = artifact.artifact_sha1
            entryline.append(artifact_sha1)
        # artifact sha256
        if model.artifactlist_xls_artifact_sha256:
            if artifact.artifact_sha256 == None:
                artifact_sha256 = ''
            else:
                artifact_sha256 = artifact.artifact_sha256
            entryline.append(artifact_sha256)
        # artifact create time
        if model.artifactlist_xls_artifact_create_time:
            artifact_create_time = artifact.artifact_create_time.strftime('%Y-%m-%d %H:%M')
            entryline.append(artifact_create_time)
        # artifact modify time
        if model.artifactlist_xls_artifact_modify_time:
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
    if model.artifactlist_xls_worksheet_artifactstatus and model.artifactlist_xls_artifactstatus and Artifactstatus.objects.count() != 0:

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
    if model.artifactlist_xls_worksheet_artifacttype and model.artifactlist_xls_artifacttype and Artifacttype.objects.count() != 0:

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
