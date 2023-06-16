from rest_framework import serializers

from dfirtrack_artifacts.models import (
    Artifact,
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)


class ArtifactprioritySerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = Artifactpriority
        # attributes made available for api
        fields = (
            'artifactpriority_id',
            'artifactpriority_name',
        )


class ArtifactstatusSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = Artifactstatus
        # attributes made available for api
        fields = (
            'artifactstatus_id',
            'artifactstatus_name',
        )


class ArtifacttypeSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = Artifacttype
        # attributes made available for api
        fields = (
            'artifacttype_id',
            'artifacttype_name',
        )


class ArtifactSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

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
            'artifact_assigned_to_user_id',
        )
        read_only_fields = (
            'artifact_uuid',
            'artifact_storage_path',
        )
