from dfirtrack_api.serializers.dfirtrack_main_fk import CaseFkSerializer, SystemFkSerializer
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_main.models import Case, System
from django.contrib.auth.models import User
from rest_framework import serializers

class ArtifactstatusSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Artifactstatus
        # attributes made available for api
        fields = (
            'artifactstatus_name',
        )

class ArtifacttypeSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Artifacttype
        # attributes made available for api
        fields = (
            'artifacttype_name',
        )

class ArtifactSerializer(serializers.ModelSerializer):
    """ create serializer for artifact """

    # get serializers of foreignkey relationsships
    artifactstatus = ArtifactstatusSerializer(many=False, read_only=True)
    artifacttype = ArtifacttypeSerializer(many=False, read_only=True)
    case = CaseFkSerializer(many=False, read_only=True)
    system = SystemFkSerializer(many=False, read_only=True)

    # redefine representation
    def to_representation(self, instance):

        # get exsiting to_representation
        representation = super(ArtifactSerializer, self).to_representation(instance)

        # change mandatory time strings
        representation['artifact_create_time'] = instance.artifact_create_time.strftime('%Y-%m-%dT%H:%M')
        representation['artifact_modify_time'] = instance.artifact_modify_time.strftime('%Y-%m-%dT%H:%M')

        # change optional time strings
        if instance.artifact_acquisition_time:
            representation['artifact_acquisition_time'] = instance.artifact_acquisition_time.strftime('%Y-%m-%dT%H:%M')
        if instance.artifact_requested_time:
            representation['artifact_requested_time'] = instance.artifact_requested_time.strftime('%Y-%m-%dT%H:%M')

        # get usernames
        representation['artifact_created_by_user_id'] = instance.artifact_created_by_user_id.username
        representation['artifact_modified_by_user_id'] = instance.artifact_modified_by_user_id.username

        return representation

    class Meta:
        model = Artifact
        # attributes made available for api
        fields = (
            'artifact_id',
            'artifact_uuid',
            'artifact_name',
            'artifactstatus',
            'artifacttype',
            'case',
            'system',
            'artifact_note',
            'artifact_md5',
            'artifact_sha1',
            'artifact_sha256',
            'artifact_slug',
            'artifact_source_path',
            'artifact_storage_path',
            'artifact_acquisition_time',
            'artifact_requested_time',
            'artifact_create_time',
            'artifact_created_by_user_id',
            'artifact_modify_time',
            'artifact_modified_by_user_id',
        )
