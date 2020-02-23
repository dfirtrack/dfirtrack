from dfirtrack_main.models import Analysisstatus, Case, Company, Contact, Domain, Dnsname, Ip, Location, Os, Osarch, Reason, Recommendation, Serviceprovider, System, Systemstatus, Systemtype, Tag
from django.contrib.auth.models import User
from rest_framework import serializers

class AnalysisstatusSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Analysisstatus
        # attributes made available for api
        fields = (
            'analysisstatus_name',
        )

class CaseSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Case
        # attributes made available for api
        fields = (
            'case_name',
            'case_is_incident',
        )

class CompanySerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Company
        # attributes made available for api
        fields = (
            'company_name',
        )

class ContactSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Contact
        # attributes made available for api
        fields = (
            'contact_name',
        )

class DnsnameSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Dnsname
        # attributes made available for api
        fields = (
            'dnsname_name',
        )

class DomainSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Domain
        # attributes made available for api
        fields = (
            'domain_name',
        )

class HostSystemSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = System
        # attributes made available for api
        fields = (
            'system_name',
        )

class IpSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Ip
        # attributes made available for api
        fields = (
            'ip_ip',
        )

class LocationSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Location
        # attributes made available for api
        fields = (
            'location_name',
        )

class OsSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Os
        # attributes made available for api
        fields = (
            'os_name',
        )

class OsarchSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Osarch
        # attributes made available for api
        fields = (
            'osarch_name',
        )

class ReasonSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Reason
        # attributes made available for api
        fields = (
            'reason_name',
        )

class RecommendationSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Recommendation
        # attributes made available for api
        fields = (
            'recommendation_name',
        )

class ServiceproviderSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Serviceprovider
        # attributes made available for api
        fields = (
            'serviceprovider_name',
        )

class SystemstatusSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Systemstatus
        # attributes made available for api
        fields = (
            'systemstatus_name',
        )

class SystemtypeSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Systemtype
        # attributes made available for api
        fields = (
            'systemtype_name',
        )

class TagSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = Tag
        # attributes made available for api
        fields = (
            'tag_name',
        )

class SystemSerializer(serializers.ModelSerializer):
    """ create serializer for system """

    # get serializers of foreignkey relationsships
    systemstatus = SystemstatusSerializer(many=False, read_only=True)
    analysisstatus = AnalysisstatusSerializer(many=False, read_only=True)
    reason = ReasonSerializer(many=False, read_only=True)
    recommendation = RecommendationSerializer(many=False, read_only=True)
    systemtype = SystemtypeSerializer(many=False, read_only=True)
    ip = IpSerializer(many=True, read_only=True)
    domain = DomainSerializer(many=False, read_only=True)
    dnsname = DnsnameSerializer(many=False, read_only=True)
    os = OsSerializer(many=False, read_only=True)
    osarch = OsarchSerializer(many=False, read_only=True)
    host_system = HostSystemSerializer(many=False, read_only=True)
    company = CompanySerializer(many=True, read_only=True)
    location = LocationSerializer(many=False, read_only=True)
    serviceprovider = ServiceproviderSerializer(many=False, read_only=True)
    contact = ContactSerializer(many=False, read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    case = CaseSerializer(many=True, read_only=True)

    # redefine representation
    def to_representation(self, instance):

        # get exsiting to_representation
        representation = super(SystemSerializer, self).to_representation(instance)

        # change mandatory time strings
        representation['system_create_time'] = instance.system_create_time.strftime('%Y-%m-%dT%H:%M')
        representation['system_modify_time'] = instance.system_modify_time.strftime('%Y-%m-%dT%H:%M')

        # change optional time strings
        if instance.system_install_time:
            representation['system_install_time'] = instance.system_install_time.strftime('%Y-%m-%dT%H:%M')
        if instance.system_lastbooted_time:
            representation['system_lastbooted_time'] = instance.system_lastbooted_time.strftime('%Y-%m-%dT%H:%M')
        if instance.system_deprecated_time:
            representation['system_deprecated_time'] = instance.system_deprecated_time.strftime('%Y-%m-%dT%H:%M')

        # get usernames
        representation['system_created_by_user_id'] = instance.system_created_by_user_id.username
        representation['system_modified_by_user_id'] = instance.system_modified_by_user_id.username

        return representation

    class Meta:
        model = System
        # attributes made available for api
        fields = (
            'system_id',
            'system_uuid',
            'system_name',
            'domain',
            'dnsname',
            'systemstatus',
            'analysisstatus',
            'reason',
            'recommendation',
            'systemtype',
            'ip',
            'os',
            'osarch',
            'system_install_time',
            'system_lastbooted_time',
            'system_deprecated_time',
            'system_is_vm',
            'host_system',
            'company',
            'location',
            'serviceprovider',
            'contact',
            'tag',
            'case',
            'system_api_time',
            'system_create_time',
            'system_created_by_user_id',
            'system_modify_time',
            'system_modified_by_user_id',
            'system_export_markdown',
            'system_export_spreadsheet',
        )
