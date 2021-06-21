from dfirtrack_artifacts.models import Artifact
from dfirtrack_artifacts.models import Artifactpriority
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_artifacts.models import Artifacttype
from rest_framework import serializers


class ArtifactpriorityFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Artifactpriority
        # attributes made available for api
        fields = (
            'artifactpriority_name',
        )

class ArtifactstatusFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Artifactstatus
        # attributes made available for api
        fields = (
            'artifactstatus_name',
        )

class ArtifacttypeFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Artifacttype
        # attributes made available for api
        fields = (
            'artifacttype_name',
        )

class ArtifactFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Artifact
        # attributes made available for api
        fields = (
            'artifact_id',
            'artifact_name',
        )
