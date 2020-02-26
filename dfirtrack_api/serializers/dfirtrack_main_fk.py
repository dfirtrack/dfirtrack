from dfirtrack_main.models import Case, System
from rest_framework import serializers

# special serializers for foreignkey relationsships

class CaseFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Case
        # attributes made available for api
        fields = (
            'case_name',
        )

class HostSystemFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = System
        # attributes made available for api
        fields = (
            'system_name',
        )
