from rest_framework import serializers
from dfirtrack_main.models import System, Systemtype

class SystemtypeSerializer(serializers.ModelSerializer):

    """ create serializer for systemtype (needed because of foreignkey relationsship) """

    class Meta:
        model = Systemtype
        # attributes made available for api
        fields = (
            'systemtype_name',
        )

class SystemSerializer(serializers.ModelSerializer):

    """ create serializer for system """

    # get serializer for systemtype (needed because of foreignkey relationsship)
    systemtype = SystemtypeSerializer(many=False, read_only=True)

    class Meta:
        model = System
        # attributes made available for api
        fields = (
            'system_id',
            'system_uuid',
            'system_name',
            'systemtype',
        )
