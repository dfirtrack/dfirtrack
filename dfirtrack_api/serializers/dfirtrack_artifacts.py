from dfirtrack_api.serializers.dfirtrack_artifacts_fk import ArtifactpriorityFkSerializer
from dfirtrack_api.serializers.dfirtrack_artifacts_fk import ArtifactstatusFkSerializer
from dfirtrack_api.serializers.dfirtrack_artifacts_fk import ArtifacttypeFkSerializer
from dfirtrack_api.serializers.dfirtrack_main_fk import CaseFkSerializer
from dfirtrack_api.serializers.dfirtrack_main_fk import SystemFkSerializer
from dfirtrack_api.serializers.dfirtrack_main_fk import TagFkSerializer
from dfirtrack_artifacts.models import Artifact
from dfirtrack_artifacts.models import Artifactpriority
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_artifacts.models import Artifacttype
from rest_framework import serializers


class ArtifactprioritySerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Artifactpriority
        # attributes made available for api
        fields = (
            'artifactpriority_id',
            'artifactpriority_name',
        )

class ArtifactstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Artifactstatus
        # attributes made available for api
        fields = (
            'artifactstatus_id',
            'artifactstatus_name',
        )

class ArtifacttypeSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Artifacttype
        # attributes made available for api
        fields = (
            'artifacttype_id',
            'artifacttype_name',
        )

class ArtifactSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # get serializers of foreignkey relationsships
        self.fields['artifactpriority'] = ArtifactpriorityFkSerializer(many=False, read_only=True)
        self.fields['artifactstatus'] = ArtifactstatusFkSerializer(many=False, read_only=True)
        self.fields['artifacttype'] = ArtifacttypeFkSerializer(many=False, read_only=True)
        self.fields['case'] = CaseFkSerializer(many=False, read_only=True)
        self.fields['system'] = SystemFkSerializer(many=False, read_only=True)
        self.fields['tag'] = TagFkSerializer(many=True, read_only=True)

        # get existing to_representation
        representation = super().to_representation(instance)

        # change mandatory time strings
        representation['artifact_create_time'] = instance.artifact_create_time.strftime('%Y-%m-%dT%H:%M')
        representation['artifact_modify_time'] = instance.artifact_modify_time.strftime('%Y-%m-%dT%H:%M')

        # change optional time strings
        if instance.artifact_acquisition_time:
            representation['artifact_acquisition_time'] = instance.artifact_acquisition_time.strftime('%Y-%m-%dT%H:%M')
        if instance.artifact_requested_time:
            representation['artifact_requested_time'] = instance.artifact_requested_time.strftime('%Y-%m-%dT%H:%M')

        return representation

    class Meta:
        model = Artifact
        # attributes made available for api
        fields = (
            'artifact_id',
            'artifact_uuid',
            'artifact_name',
            'artifactpriority',
            'artifactstatus',
            'artifacttype',
            'case',
            'system',
            'tag',
            'artifact_md5',
            'artifact_sha1',
            'artifact_sha256',
            'artifact_source_path',
            'artifact_storage_path',
            'artifact_acquisition_time',
            'artifact_requested_time',
            'artifact_create_time',
            'artifact_created_by_user_id',
            'artifact_modify_time',
            'artifact_modified_by_user_id',
        )
        read_only_fields = (
            'artifact_uuid',
            'artifact_storage_path',
        )
