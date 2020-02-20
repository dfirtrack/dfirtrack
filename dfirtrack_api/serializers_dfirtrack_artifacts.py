from dfirtrack_artifacts.models import Artifact
from django.contrib.auth.models import User
from rest_framework import serializers

#class DomainSerializer(serializers.ModelSerializer):
#    """ create serializer for foreignkey relationsship """
#
#    class Meta:
#        model = Domain
#        # attributes made available for api
#        fields = (
#            'domain_name',
#        )

class ArtifactSerializer(serializers.ModelSerializer):
    """ create serializer for artifact """

    # get serializers of foreignkey relationsships
    #domain = DomainSerializer(many=False, read_only=True)

    # redefine representation
    def to_representation(self, instance):

        # get exsiting to_representation
        representation = super(ArtifactSerializer, self).to_representation(instance)

        ## change mandatory time strings
        #representation['system_create_time'] = instance.system_create_time.strftime('%Y-%m-%dT%H:%M')
        #representation['system_modify_time'] = instance.system_modify_time.strftime('%Y-%m-%dT%H:%M')

        ## change optional time strings
        #if instance.system_install_time:
        #    representation['system_install_time'] = instance.system_install_time.strftime('%Y-%m-%dT%H:%M')
        #if instance.system_lastbooted_time:
        #    representation['system_lastbooted_time'] = instance.system_lastbooted_time.strftime('%Y-%m-%dT%H:%M')
        #if instance.system_deprecated_time:
        #    representation['system_deprecated_time'] = instance.system_deprecated_time.strftime('%Y-%m-%dT%H:%M')

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
        )
