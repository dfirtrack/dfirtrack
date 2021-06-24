from dfirtrack_main import models as dfirtrack_main_models
from rest_framework import serializers


class AnalysisstatusFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Analysisstatus
        # attributes made available for api
        fields = (
            'analysisstatus_name',
        )

class CaseFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = dfirtrack_main_models.Case
        # attributes made available for api
        fields = (
            'case_id',
            'case_name',
        )

class CasepriorityFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Casepriority
        # attributes made available for api
        fields = (
            'casepriority_name',
        )

class CasestatusFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Casestatus
        # attributes made available for api
        fields = (
            'casestatus_name',
        )

class CasetypeFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Casetype
        # attributes made available for api
        fields = (
            'casetype_name',
        )

class CompanyFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Company
        # attributes made available for api
        fields = (
            'company_name',
        )

class ContactFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Contact
        # attributes made available for api
        fields = (
            'contact_email',
        )

class DivisionFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Division
        # attributes made available for api
        fields = (
            'division_name',
        )

class DnsnameFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Dnsname
        # attributes made available for api
        fields = (
            'dnsname_name',
        )

class DomainFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Domain
        # attributes made available for api
        fields = (
            'domain_name',
        )

class HostSystemFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = dfirtrack_main_models.System
        # attributes made available for api
        fields = (
            'system_id',
            'system_name',
        )

class IpFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Ip
        # attributes made available for api
        fields = (
            'ip_ip',
        )

class LocationFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Location
        # attributes made available for api
        fields = (
            'location_name',
        )

class NotestatusFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Notestatus
        # attributes made available for api
        fields = (
            'notestatus_name',
        )

class OsFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Os
        # attributes made available for api
        fields = (
            'os_name',
        )

class OsarchFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Osarch
        # attributes made available for api
        fields = (
            'osarch_name',
        )

class ParentTaskFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = dfirtrack_main_models.Task
        # attributes made available for api
        fields = (
            'task_id',
        )

class ReasonFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Reason
        # attributes made available for api
        fields = (
            'reason_name',
        )

class RecommendationFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Recommendation
        # attributes made available for api
        fields = (
            'recommendation_name',
        )

class ServiceproviderFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Serviceprovider
        # attributes made available for api
        fields = (
            'serviceprovider_name',
        )

class SystemFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.System
        # attributes made available for api
        fields = (
            'system_id',
            'system_name',
        )

class SystemstatusFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Systemstatus
        # attributes made available for api
        fields = (
            'systemstatus_name',
        )

class SystemtypeFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Systemtype
        # attributes made available for api
        fields = (
            'systemtype_name',
        )

class TagFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Tag
        # attributes made available for api
        fields = (
            'tag_id',
            'tag_name',
        )

class TagcolorFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Tagcolor
        # attributes made available for api
        fields = (
            'tagcolor_name',
        )

class TaskFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsship """

    class Meta:
        model = dfirtrack_main_models.Task
        # attributes made available for api
        fields = (
            'task_id',
        )

class TasknameFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Taskname
        # attributes made available for api
        fields = (
            'taskname_name',
        )

class TaskpriorityFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Taskpriority
        # attributes made available for api
        fields = (
            'taskpriority_name',
        )

class TaskstatusFkSerializer(serializers.ModelSerializer):
    """ create serializer for foreignkey relationsships """

    class Meta:
        model = dfirtrack_main_models.Taskstatus
        # attributes made available for api
        fields = (
            'taskstatus_name',
        )
