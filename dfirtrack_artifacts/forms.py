from django import forms
from django.utils.translation import gettext_lazy
from dfirtrack_main.models import Case, System
from dfirtrack_artifacts.models import Artifact, Artifacttype


class ArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        # this HTML forms are shown
        fields = [
            'artifact_name',
            'artifactstatus',
            'artifacttype',
            'artifact_storage_path',
            'system',
            'case',
            'artifact_requested_time',
            'artifact_acquisition_time',
            'artifact_md5',
            'artifact_sha1',
            'artifact_sha256',
            'artifact_description',
        ]
        # non default form labeling
        labels = {
            'artifact_name': gettext_lazy('Artifact name (*)'),
            'artifactstatus': gettext_lazy('Artifactstatus (*)'),
            'artifacttype': gettext_lazy('Artifacttype (*)'),
            'system': gettext_lazy('System (*)'),
            'artifact_requested_time': gettext_lazy('Artifact requested time (YYYY-MM-DD HH:MM:SS)'),
            'artifact_acquisition_time': gettext_lazy('Artifact acquisition time (YYYY-MM-DD HH:MM:SS)'),
            'artifact_md5': gettext_lazy('MD5'),
            'artifact_sha1': gettext_lazy('SHA1'),
            'artifact_sha256': gettext_lazy('SHA256'),
            'artifact_description': gettext_lazy('Description'),
        }
        # special form type or option
        widgets = {
            'artifact_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
            'artifact_md5': forms.TextInput(attrs={'size': '32'}),
            'artifact_sha1': forms.TextInput(attrs={'size': '40'}),
            'artifact_sha256': forms.TextInput(attrs={'size': '64'}),
        }

class ArtifacttypeForm(forms.ModelForm):
    class Meta:
        model = Artifacttype
        # this HTML forms are shown
        fields = [
            'artifacttype_name',
            'artifacttype_description',
        ]
        # non default form labeling
        labels = {
            'artifacttype_name': gettext_lazy('Artifacttype name (*)'),
        }
        # special form type or option
        widgets = {
            'artifacttype_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }
