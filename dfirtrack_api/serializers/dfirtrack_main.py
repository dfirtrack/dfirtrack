from rest_framework import serializers

from dfirtrack_main import models as dfirtrack_main_models


class AnalysisstatusSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Analysisstatus
        # attributes made available for api
        fields = (
            'analysisstatus_id',
            'analysisstatus_name',
        )


class CaseSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Case
        # attributes made available for api
        fields = (
            'case_id',
            'case_id_external',
            'case_name',
            'casepriority',
            'casestatus',
            'casetype',
            'tag',
            'case_is_incident',
            'case_start_time',
            'case_end_time',
            'case_created_by_user_id',
            'case_create_time',
            'case_modified_by_user_id',
            'case_modify_time',
            'case_assigned_to_user_id',
        )


class CaseprioritySerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Casepriority
        # attributes made available for api
        fields = (
            'casepriority_id',
            'casepriority_name',
        )


class CasestatusSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Casestatus
        # attributes made available for api
        fields = (
            'casestatus_id',
            'casestatus_name',
        )


class CasetypeSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Casetype
        # attributes made available for api
        fields = (
            'casetype_id',
            'casetype_name',
        )


class CompanySerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Company
        # attributes made available for api
        fields = (
            'company_id',
            'company_name',
            'division',
        )


class ContactSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Contact
        # attributes made available for api
        fields = (
            'contact_id',
            'contact_name',
            'contact_email',
            'contact_phone',
        )


class DivisionSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Division
        # attributes made available for api
        fields = (
            'division_id',
            'division_name',
        )


class DnsnameSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Dnsname
        # attributes made available for api
        fields = (
            'dnsname_id',
            'dnsname_name',
            'domain',
        )


class DomainSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Domain
        # attributes made available for api
        fields = (
            'domain_id',
            'domain_name',
        )


class DomainuserSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Domainuser
        # attributes made available for api
        fields = (
            'domainuser_id',
            'domainuser_name',
            'domain',
            'domainuser_is_domainadmin',
        )


class HeadlineSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Headline
        # attributes made available for api
        fields = (
            'headline_id',
            'headline_name',
        )


class IpSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Ip
        # attributes made available for api
        fields = (
            'ip_id',
            'ip_ip',
        )


class LocationSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Location
        # attributes made available for api
        fields = (
            'location_id',
            'location_name',
        )


class NoteSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Note
        # attributes made available for api
        fields = (
            'note_id',
            'note_title',
            'note_content',
            'note_version',
            'case',
            'notestatus',
            'tag',
            'note_create_time',
            'note_created_by_user_id',
            'note_modify_time',
            'note_modified_by_user_id',
            'note_assigned_to_user_id',
        )


class NotestatusSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Notestatus
        # attributes made available for api
        fields = (
            'notestatus_id',
            'notestatus_name',
        )


class OsSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Os
        # attributes made available for api
        fields = (
            'os_id',
            'os_name',
        )


class OsarchSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Osarch
        # attributes made available for api
        fields = (
            'osarch_id',
            'osarch_name',
        )


class ReasonSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Reason
        # attributes made available for api
        fields = (
            'reason_id',
            'reason_name',
        )


class RecommendationSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Recommendation
        # attributes made available for api
        fields = (
            'recommendation_id',
            'recommendation_name',
        )


class ReportitemSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Reportitem
        # attributes made available for api
        fields = (
            'reportitem_id',
            'case',
            'headline',
            'notestatus',
            'system',
            'tag',
            'reportitem_subheadline',
            'reportitem_note',
            'reportitem_create_time',
            'reportitem_created_by_user_id',
            'reportitem_modify_time',
            'reportitem_modified_by_user_id',
            'reportitem_assigned_to_user_id',
        )


class ServiceproviderSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Serviceprovider
        # attributes made available for api
        fields = (
            'serviceprovider_id',
            'serviceprovider_name',
        )


class SystemSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.System
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
            # TODO: change after model rebuild
            #'system_install_time',
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
            'system_create_time',
            'system_created_by_user_id',
            'system_modify_time',
            'system_modified_by_user_id',
            'system_assigned_to_user_id',
            'system_export_markdown',
            'system_export_spreadsheet',
        )


class SystemstatusSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Systemstatus
        # attributes made available for api
        fields = (
            'systemstatus_id',
            'systemstatus_name',
        )


class SystemtypeSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Systemtype
        # attributes made available for api
        fields = (
            'systemtype_id',
            'systemtype_name',
        )


class SystemuserSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Systemuser
        # attributes made available for api
        fields = (
            'systemuser_id',
            'systemuser_name',
            'system',
            'systemuser_lastlogon_time',
            'systemuser_is_systemadmin',
        )


class TagSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Tag
        # attributes made available for api
        fields = (
            'tag_id',
            'tag_name',
            'tagcolor',
            'tag_assigned_to_user_id',
        )


class TagcolorSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Tagcolor
        # attributes made available for api
        fields = (
            'tagcolor_id',
            'tagcolor_name',
        )


class TaskSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Task
        # attributes made available for api
        fields = (
            'task_id',
            'parent_task',
            'taskname',
            'taskpriority',
            'taskstatus',
            'artifact',
            'case',
            'system',
            'task_assigned_to_user_id',
            'tag',
            'task_scheduled_time',
            'task_started_time',
            'task_finished_time',
            'task_due_time',
            'task_create_time',
            'task_modify_time',
            'task_created_by_user_id',
            'task_modified_by_user_id',
        )


class TasknameSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Taskname
        # attributes made available for api
        fields = (
            'taskname_id',
            'taskname_name',
        )


class TaskprioritySerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Taskpriority
        # attributes made available for api
        fields = (
            'taskpriority_id',
            'taskpriority_name',
        )


class TaskstatusSerializer(serializers.ModelSerializer):
    """create serializer for model instance"""

    class Meta:
        model = dfirtrack_main_models.Taskstatus
        # attributes made available for api
        fields = (
            'taskstatus_id',
            'taskstatus_name',
        )
