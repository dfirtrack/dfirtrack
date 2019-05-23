from django import forms
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype


class ArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = ['artifact_id', 'artifact_name', 'artifact_description', 'artifact_storage_path', 'artifacttype', 'case', 'system']

class ArtifactstatusForm(forms.ModelForm):
    class Meta:
        model = Artifactstatus
        fields = ['artifactstatus_id', 'artifactstatus_name', 'artifactstatus_description']

class ArtifacttypeForm(forms.ModelForm):
    class Meta:
        model = Artifacttype
        fields = ['artifacttype_id', 'artifacttype_name', 'artifactstatus_description']

