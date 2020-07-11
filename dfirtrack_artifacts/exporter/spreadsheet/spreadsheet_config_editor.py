from constance import config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_artifacts.config_forms import ArtifactExporterSpreadsheetXlsForm

@login_required(login_url="/login")
def artifact_exporter_spreadsheet_xls_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = ArtifactExporterSpreadsheetXlsForm(request.POST)

        if form.is_valid():

            # assign values
            config.ARTIFACTLIST_ARTIFACT_ID = form.cleaned_data['artifactlist_artifact_id']
            config.ARTIFACTLIST_SYSTEM_ID = form.cleaned_data['artifactlist_system_id']
            config.ARTIFACTLIST_SYSTEM_NAME = form.cleaned_data['artifactlist_system_name']
            config.ARTIFACTLIST_ARTIFACTSTATUS = form.cleaned_data['artifactlist_artifactstatus']
            config.ARTIFACTLIST_ARTIFACTTYPE = form.cleaned_data['artifactlist_artifacttype']
            config.ARTIFACTLIST_ARTIFACT_SOURCE_PATH = form.cleaned_data['artifactlist_artifact_source_path']
            config.ARTIFACTLIST_ARTIFACT_STORAGE_PATH = form.cleaned_data['artifactlist_artifact_storage_path']
            config.ARTIFACTLIST_ARTIFACT_NOTE = form.cleaned_data['artifactlist_artifact_note']
            config.ARTIFACTLIST_ARTIFACT_MD5 = form.cleaned_data['artifactlist_artifact_md5']
            config.ARTIFACTLIST_ARTIFACT_SHA1 = form.cleaned_data['artifactlist_artifact_sha1']
            config.ARTIFACTLIST_ARTIFACT_SHA256 = form.cleaned_data['artifactlist_artifact_sha256']
            config.ARTIFACTLIST_ARTIFACT_CREATE_TIME = form.cleaned_data['artifactlist_artifact_create_time']
            config.ARTIFACTLIST_ARTIFACT_MODIFY_TIME = form.cleaned_data['artifactlist_artifact_modify_time']
            config.ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS = form.cleaned_data['artifactlist_worksheet_artifactstatus']
            config.ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE = form.cleaned_data['artifactlist_worksheet_artifacttype']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = ArtifactExporterSpreadsheetXlsForm(
            initial = {
                'artifactlist_artifact_id': config.ARTIFACTLIST_ARTIFACT_ID,
                'artifactlist_system_id': config.ARTIFACTLIST_SYSTEM_ID,
                'artifactlist_system_name': config.ARTIFACTLIST_SYSTEM_NAME,
                'artifactlist_artifactstatus': config.ARTIFACTLIST_ARTIFACTSTATUS,
                'artifactlist_artifacttype': config.ARTIFACTLIST_ARTIFACTTYPE,
                'artifactlist_artifact_source_path': config.ARTIFACTLIST_ARTIFACT_SOURCE_PATH,
                'artifactlist_artifact_storage_path': config.ARTIFACTLIST_ARTIFACT_STORAGE_PATH,
                'artifactlist_artifact_note': config.ARTIFACTLIST_ARTIFACT_NOTE,
                'artifactlist_artifact_md5': config.ARTIFACTLIST_ARTIFACT_MD5,
                'artifactlist_artifact_sha1': config.ARTIFACTLIST_ARTIFACT_SHA1,
                'artifactlist_artifact_sha256': config.ARTIFACTLIST_ARTIFACT_SHA256,
                'artifactlist_artifact_create_time': config.ARTIFACTLIST_ARTIFACT_CREATE_TIME,
                'artifactlist_artifact_modify_time': config.ARTIFACTLIST_ARTIFACT_MODIFY_TIME,
                'artifactlist_worksheet_artifactstatus': config.ARTIFACTLIST_WORKSHEET_ARTIFACTSTATUS,
                'artifactlist_worksheet_artifacttype': config.ARTIFACTLIST_WORKSHEET_ARTIFACTTYPE,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_artifacts/artifact/artifact_exporter_spreadsheet_xls_config_popup.html',
        {
            'form': form,
        }
    )
