from django import forms
from dfirtrack_main.models import Case, System
from dfirtrack_artifacts.models import Artifact, Artifacttype


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

class ArtifacttypeForm(forms.ModelForm):
    class Meta:
        model = Artifacttype
        fields = [
            'artifacttype_name',
            'artifacttype_description',
        ]
