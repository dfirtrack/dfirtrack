from django import forms
from dfirtrack_artifacts.models import Artifactstatus

class ArtifactExporterSpreadsheetCsvForm(forms.Form):

    # create empty list for available artifactstatus
    artifactstatus_choices = []
    # get all artifactstatus
    artifactstatus_all = Artifactstatus.objects.order_by('artifactstatus_id')
    # prepare choices (append tupel consisting of artifactstatus_id and artifactstatus_name to list (therefore double brackets))
    for artifactstatus in artifactstatus_all:
        artifactstatus_choices.append((artifactstatus.artifactstatus_id, artifactstatus.artifactstatus_name))
    # create field
    artifactlist_choice_artifactstatus = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple(),
        label = 'Export only artifacts with this artifactstatus',
        choices = artifactstatus_choices,
    )

    artifactlist_artifact_id = forms.BooleanField(
        required = False,
        label = 'Export artifact ID',
    )

    artifactlist_system_id = forms.BooleanField(
        required = False,
        label = 'Export system ID',
    )

    artifactlist_system_name = forms.BooleanField(
        required = False,
        label = 'Export system name',
    )

    artifactlist_artifactstatus = forms.BooleanField(
        required = False,
        label = 'Export artifactstatus',
    )

    artifactlist_artifacttype = forms.BooleanField(
        required = False,
        label = 'Export artifacttype',
    )

    artifactlist_artifact_source_path = forms.BooleanField(
        required = False,
        label = 'Export source path',
    )

    artifactlist_artifact_storage_path = forms.BooleanField(
        required = False,
        label = 'Export storage path',
    )

    artifactlist_artifact_note = forms.BooleanField(
        required = False,
        label = 'Export note',
    )

    artifactlist_artifact_md5 = forms.BooleanField(
        required = False,
        label = 'Export MD5',
    )

    artifactlist_artifact_sha1 = forms.BooleanField(
        required = False,
        label = 'Export SHA1',
    )

    artifactlist_artifact_sha256 = forms.BooleanField(
        required = False,
        label = 'Export SHA256',
    )

    artifactlist_artifact_create_time = forms.BooleanField(
        required = False,
        label = 'Export create time',
    )

    artifactlist_artifact_modify_time = forms.BooleanField(
        required = False,
        label = 'Export modify time',
    )


class ArtifactExporterSpreadsheetXlsForm(ArtifactExporterSpreadsheetCsvForm):

    artifactlist_worksheet_artifactstatus = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain artifactstatus',
    )

    artifactlist_worksheet_artifacttype = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain artifacttype',
    )
