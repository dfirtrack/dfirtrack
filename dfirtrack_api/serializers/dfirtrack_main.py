from dfirtrack_main.models import Analysisstatus, Case, Company, Contact, Division, Dnsname, Domain, Domainuser, Ip, Location, Os, Osarch, Reason, Recommendation, Serviceprovider, System, Systemstatus, Systemtype, Systemuser, Tag, Tagcolor, Taskname, Taskpriority, Taskstatus
from . import dfirtrack_main_fk
from rest_framework import serializers

# model serializers

class AnalysisstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Analysisstatus
        # attributes made available for api
        fields = (
            'analysisstatus_id',
            'analysisstatus_name',
        )

class CaseSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # get exsiting to_representation
        representation = super(CaseSerializer, self).to_representation(instance)

        # change mandatory time strings
        representation['case_create_time'] = instance.case_create_time.strftime('%Y-%m-%dT%H:%M')

        return representation

    class Meta:
        model = Case
        # attributes made available for api
        fields = (
            'case_id',
            'case_name',
            'case_is_incident',
            'case_created_by_user_id',
            'case_create_time',
        )

class CompanySerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['division'] =  dfirtrack_main_fk.DivisionFkSerializer(read_only=True)
        return super(CompanySerializer, self).to_representation(instance)

    class Meta:
        model = Company
        # attributes made available for api
        fields = (
            'company_id',
            'company_name',
            'division',
        )

class ContactSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Contact
        # attributes made available for api
        fields = (
            'contact_id',
            'contact_name',
            'contact_email',
            'contact_phone',
        )

class DivisionSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Division
        # attributes made available for api
        fields = (
            'division_id',
            'division_name',
        )

class DnsnameSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['domain'] =  dfirtrack_main_fk.DomainFkSerializer(read_only=True)
        return super(DnsnameSerializer, self).to_representation(instance)

    class Meta:
        model = Dnsname
        # attributes made available for api
        fields = (
            'dnsname_id',
            'dnsname_name',
            'domain',
        )

class DomainSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Domain
        # attributes made available for api
        fields = (
            'domain_id',
            'domain_name',
        )

class DomainuserSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['domain'] =  dfirtrack_main_fk.DomainFkSerializer(read_only=True)
        return super(DomainuserSerializer, self).to_representation(instance)

    class Meta:
        model = Domainuser
        # attributes made available for api
        fields = (
            'domainuser_id',
            'domainuser_name',
            'domain',
            'domainuser_is_domainadmin',
        )

class IpSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Ip
        # attributes made available for api
        fields = (
            'ip_id',
            'ip_ip',
        )

class LocationSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Location
        # attributes made available for api
        fields = (
            'location_id',
            'location_name',
        )

class OsSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Os
        # attributes made available for api
        fields = (
            'os_id',
            'os_name',
        )

class OsarchSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Osarch
        # attributes made available for api
        fields = (
            'osarch_id',
            'osarch_name',
        )

class ReasonSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Reason
        # attributes made available for api
        fields = (
            'reason_id',
            'reason_name',
        )

class RecommendationSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Recommendation
        # attributes made available for api
        fields = (
            'recommendation_id',
            'recommendation_name',
        )

class ServiceproviderSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Serviceprovider
        # attributes made available for api
        fields = (
            'serviceprovider_id',
            'serviceprovider_name',
        )

class SystemSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    analysisstatus = dfirtrack_main_fk.AnalysisstatusFkSerializer(many=False, read_only=True)
    case = dfirtrack_main_fk.CaseFkSerializer(many=True, read_only=True)
    company = dfirtrack_main_fk.CompanyFkSerializer(many=True, read_only=True)
    contact = dfirtrack_main_fk.ContactFkSerializer(many=False, read_only=True)
    dnsname = dfirtrack_main_fk.DnsnameFkSerializer(many=False, read_only=True)
    domain = dfirtrack_main_fk.DomainFkSerializer(many=False, read_only=True)
    host_system = dfirtrack_main_fk.HostSystemFkSerializer(many=False, read_only=True)
    ip = dfirtrack_main_fk.IpFkSerializer(many=True, read_only=True)
    location = dfirtrack_main_fk.LocationFkSerializer(many=False, read_only=True)
    os = dfirtrack_main_fk.OsFkSerializer(many=False, read_only=True)
    osarch = dfirtrack_main_fk.OsarchFkSerializer(many=False, read_only=True)
    reason = dfirtrack_main_fk.ReasonFkSerializer(many=False, read_only=True)
    recommendation = dfirtrack_main_fk.RecommendationFkSerializer(many=False, read_only=True)
    serviceprovider = dfirtrack_main_fk.ServiceproviderFkSerializer(many=False, read_only=True)
    systemstatus = dfirtrack_main_fk.SystemstatusFkSerializer(many=False, read_only=True)
    systemtype = dfirtrack_main_fk.SystemtypeFkSerializer(many=False, read_only=True)
    tag = dfirtrack_main_fk.TagFkSerializer(many=True, read_only=True)

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
        # attributes made available for api in a sorted fashion
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

class SystemstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Systemstatus
        # attributes made available for api
        fields = (
            'systemstatus_id',
            'systemstatus_name',
        )

class SystemtypeSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Systemtype
        # attributes made available for api
        fields = (
            'systemtype_id',
            'systemtype_name',
        )

class SystemuserSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # change optional time strings
        if instance.systemuser_lastlogon_time:
            representation['systemuser_lastlogon_time'] = instance.systemuser_lastlogon_time.strftime('%Y-%m-%dT%H:%M')

        # get serializers of foreignkey relationsships
        self.fields['system'] =  dfirtrack_main_fk.SystemFkSerializer(read_only=True)
        return super(SystemuserSerializer, self).to_representation(instance)

    class Meta:
        model = Systemuser
        # attributes made available for api
        fields = (
            'systemuser_id',
            'systemuser_name',
            'system',
            'systemuser_lastlogon_time',
            'systemuser_is_systemadmin',
        )

class TagSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['tagcolor'] =  dfirtrack_main_fk.TagcolorFkSerializer(read_only=True)
        return super(TagSerializer, self).to_representation(instance)

    class Meta:
        model = Tag
        # attributes made available for api
        fields = (
            'tag_id',
            'tag_name',
            'tagcolor',
        )

class TagcolorSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Tagcolor
        # attributes made available for api
        fields = (
            'tagcolor_id',
            'tagcolor_name',
        )

class TasknameSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Taskname
        # attributes made available for api
        fields = (
            'taskname_id',
            'taskname_name',
        )

class TaskprioritySerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Taskpriority
        # attributes made available for api
        fields = (
            'taskpriority_id',
            'taskpriority_name',
        )

class TaskstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = Taskstatus
        # attributes made available for api
        fields = (
            'taskstatus_id',
            'taskstatus_name',
        )
