from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_config.forms import ArtifactExporterSpreadsheetXlsConfigForm
from dfirtrack_config.models import ArtifactExporterSpreadsheetXlsConfigModel

@login_required(login_url="/login")
def artifact_exporter_spreadsheet_xls_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = ArtifactExporterSpreadsheetXlsConfigForm(request.POST)
        model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(artifact_exporter_spreadsheet_xls_config_name = 'ArtifactExporterSpreadsheetXlsConfig')

        if form.is_valid():

            # assign values
            # TODO: find an alternative for the selection
            #model.artifactlist_xls_choice_artifactstatus = form.cleaned_data['artifactlist_choice_artifactstatus']
            model.artifactlist_xls_artifact_id = form.cleaned_data['artifactlist_artifact_id']
            model.artifactlist_xls_system_id = form.cleaned_data['artifactlist_system_id']
            model.artifactlist_xls_system_name = form.cleaned_data['artifactlist_system_name']
            model.artifactlist_xls_artifactstatus = form.cleaned_data['artifactlist_artifactstatus']
            model.artifactlist_xls_artifacttype = form.cleaned_data['artifactlist_artifacttype']
            model.artifactlist_xls_artifact_source_path = form.cleaned_data['artifactlist_artifact_source_path']
            model.artifactlist_xls_artifact_storage_path = form.cleaned_data['artifactlist_artifact_storage_path']
            model.artifactlist_xls_artifact_note = form.cleaned_data['artifactlist_artifact_note']
            model.artifactlist_xls_artifact_md5 = form.cleaned_data['artifactlist_artifact_md5']
            model.artifactlist_xls_artifact_sha1 = form.cleaned_data['artifactlist_artifact_sha1']
            model.artifactlist_xls_artifact_sha256 = form.cleaned_data['artifactlist_artifact_sha256']
            model.artifactlist_xls_artifact_create_time = form.cleaned_data['artifactlist_artifact_create_time']
            model.artifactlist_xls_artifact_modify_time = form.cleaned_data['artifactlist_artifact_modify_time']
            model.artifactlist_xls_worksheet_artifactstatus = form.cleaned_data['artifactlist_worksheet_artifactstatus']
            model.artifactlist_xls_worksheet_artifacttype = form.cleaned_data['artifactlist_worksheet_artifacttype']
            model.save()

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # get config model
        model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(artifact_exporter_spreadsheet_xls_config_name = 'ArtifactExporterSpreadsheetXlsConfig')
        # submit existing values to form
        form = ArtifactExporterSpreadsheetXlsConfigForm(
            initial = {
                # TODO: find an alternative for the selection
                #'artifactlist_choice_artifactstatus': model.artifactlist_xls_choice_artifactstatus,
                'artifactlist_artifact_id': model.artifactlist_xls_artifact_id,
                'artifactlist_system_id': model.artifactlist_xls_system_id,
                'artifactlist_system_name': model.artifactlist_xls_system_name,
                'artifactlist_artifactstatus': model.artifactlist_xls_artifactstatus,
                'artifactlist_artifacttype': model.artifactlist_xls_artifacttype,
                'artifactlist_artifact_source_path': model.artifactlist_xls_artifact_source_path,
                'artifactlist_artifact_storage_path': model.artifactlist_xls_artifact_storage_path,
                'artifactlist_artifact_note': model.artifactlist_xls_artifact_note,
                'artifactlist_artifact_md5': model.artifactlist_xls_artifact_md5,
                'artifactlist_artifact_sha1': model.artifactlist_xls_artifact_sha1,
                'artifactlist_artifact_sha256': model.artifactlist_xls_artifact_sha256,
                'artifactlist_artifact_create_time': model.artifactlist_xls_artifact_create_time,
                'artifactlist_artifact_modify_time': model.artifactlist_xls_artifact_modify_time,
                'artifactlist_worksheet_artifactstatus': model.artifactlist_xls_worksheet_artifactstatus,
                'artifactlist_worksheet_artifacttype': model.artifactlist_xls_worksheet_artifacttype,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_config/artifact/artifact_exporter_spreadsheet_xls_config_popup.html',
        {
            'form': form,
        }
    )
