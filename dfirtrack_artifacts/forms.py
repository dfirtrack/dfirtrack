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
            'artifact_description',
            'artifacttype',
            'artifactstatus',
            'artifact_storage_path',
            'system',
            'case',
            'artifact_requested_time',
            'artifact_acquisition_time',
        ]
        # non default form labeling
        labels = {
            'artifact_name': gettext_lazy('Artifact name (*)'),
            'artifact_description': gettext_lazy('Description'),
            'artifacttype': gettext_lazy('Artifacttype (*)'),
            'artifactstatus': gettext_lazy('Artifactstatus (*)'),
            'system': gettext_lazy('System (*)'),
            'artifact_requested_time': gettext_lazy('Artifact requested time (YYYY-MM-DD HH:MM:SS)'),
            'artifact_acquisition_time': gettext_lazy('Artifact acquisition time (YYYY-MM-DD HH:MM:SS)'),
        }
        # special form type or option
        widgets = {
            'artifact_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
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
