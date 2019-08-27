from django import forms
from dfirtrack_main.models import Case, System
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype


class ArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = [
            'artifact_name',
            'artifact_description',
            'artifacttype',
            'artifactstatus',
            'artifact_storage_path',
            'system',
            'case',
            'artifact_acquisition_time',
        ]

class ArtifactstatusForm(forms.ModelForm):
    class Meta:
        model = Artifactstatus
        fields = [
            'artifactstatus_name',
            'artifactstatus_description',
        ]

class ArtifacttypeForm(forms.ModelForm):
    class Meta:
        model = Artifacttype
        fields = [
            'artifacttype_name',
            'artifacttype_description',
        ]
