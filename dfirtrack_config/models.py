import logging

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

stdlogger = logging.getLogger(__name__)


class ArtifactExporterSpreadsheetXlsConfigModel(models.Model):
    """config for artifact spreadsheet XLS exporter, single object for DFIRTrack"""

    # primary key
    artifact_exporter_spreadsheet_xls_config_name = models.CharField(
        max_length=50, primary_key=True, editable=False
    )

    # config fields
    artifactlist_xls_choice_artifactstatus = models.ManyToManyField(
        'dfirtrack_artifacts.Artifactstatus',
        related_name='artifact_exporter_spreadsheet_xls_config_artifactstatus',
    )
    artifactlist_xls_artifact_id = models.BooleanField(default=True)
    artifactlist_xls_system_id = models.BooleanField(default=True)
    artifactlist_xls_system_name = models.BooleanField(default=True)
    artifactlist_xls_artifactstatus = models.BooleanField(default=True)
    artifactlist_xls_artifactpriority = models.BooleanField(default=False)
    artifactlist_xls_artifacttype = models.BooleanField(default=True)
    artifactlist_xls_artifact_source_path = models.BooleanField(default=True)
    artifactlist_xls_artifact_storage_path = models.BooleanField(default=False)
    artifactlist_xls_artifact_note_internal = models.BooleanField(default=False)
    artifactlist_xls_artifact_note_external = models.BooleanField(default=False)
    artifactlist_xls_artifact_note_analysisresult = models.BooleanField(default=False)
    artifactlist_xls_artifact_md5 = models.BooleanField(default=False)
    artifactlist_xls_artifact_sha1 = models.BooleanField(default=False)
    artifactlist_xls_artifact_sha256 = models.BooleanField(default=False)
    artifactlist_xls_artifact_create_time = models.BooleanField(default=False)
    artifactlist_xls_artifact_modify_time = models.BooleanField(default=False)
    artifactlist_xls_worksheet_artifactstatus = models.BooleanField(default=True)
    artifactlist_xls_worksheet_artifacttype = models.BooleanField(default=True)

    # string representation
    def __str__(self):
        return self.artifact_exporter_spreadsheet_xls_config_name


class MainConfigModel(models.Model):
    """main config for DFIRTrack, single object for DFIRTrack"""

    # primary key
    main_config_name = models.CharField(max_length=50, primary_key=True, editable=False)

    # config fields
    system_name_editable = models.BooleanField(default=False)
    artifactstatus_open = models.ManyToManyField(
        'dfirtrack_artifacts.Artifactstatus',
        related_name='main_config_artifactstatus_open',
        blank=True,
    )
    artifactstatus_requested = models.ManyToManyField(
        'dfirtrack_artifacts.Artifactstatus',
        related_name='main_config_artifactstatus_requested',
        blank=True,
    )
    artifactstatus_acquisition = models.ManyToManyField(
        'dfirtrack_artifacts.Artifactstatus',
        related_name='main_config_artifactstatus_acquisition',
        blank=True,
    )
    casestatus_open = models.ManyToManyField(
        'dfirtrack_main.Casestatus',
        related_name='main_config_casestatus_open',
        blank=True,
    )
    casestatus_start = models.ManyToManyField(
        'dfirtrack_main.Casestatus',
        related_name='main_config_casestatus_start',
        blank=True,
    )
    casestatus_end = models.ManyToManyField(
        'dfirtrack_main.Casestatus',
        related_name='main_config_casestatus_end',
        blank=True,
    )
    statushistory_entry_numbers = models.IntegerField(default=10)
    cron_export_path = models.CharField(max_length=4096, default='/tmp')  # nosec
    cron_username = models.CharField(max_length=255, default='cron')

    MAIN_OVERVIEW_ARTIFACT = 'main_overview_artifact'
    MAIN_OVERVIEW_CASE = 'main_overview_case'
    MAIN_OVERVIEW_STATUS = 'main_overview_status'
    MAIN_OVERVIEW_SYSTEM = 'main_overview_system'
    MAIN_OVERVIEW_TAG = 'main_overview_tag'
    MAIN_OVERVIEW_TASK = 'main_overview_task'
    MAIN_OVERVIEW_CHOICES = [
        (MAIN_OVERVIEW_ARTIFACT, 'Artifact'),
        (MAIN_OVERVIEW_CASE, 'Case'),
        (MAIN_OVERVIEW_STATUS, 'Status'),
        (MAIN_OVERVIEW_SYSTEM, 'System'),
        (MAIN_OVERVIEW_TAG, 'Tag'),
        (MAIN_OVERVIEW_TASK, 'Task'),
    ]
    main_overview = models.CharField(
        max_length=50,
        choices=MAIN_OVERVIEW_CHOICES,
        default=MAIN_OVERVIEW_SYSTEM,
    )

    CAPITALIZATION_KEEP = 'capitalization_keep'
    CAPITALIZATION_LOWER = 'capitalization_lower'
    CAPITALIZATION_UPPER = 'capitalization_upper'
    CAPITALIZATION_CHOICES = [
        (CAPITALIZATION_KEEP, 'Keep notation'),
        (CAPITALIZATION_LOWER, 'Convert to lower case'),
        (CAPITALIZATION_UPPER, 'Convert to upper case'),
    ]
    capitalization = models.CharField(
        max_length=50,
        choices=CAPITALIZATION_CHOICES,
        default=CAPITALIZATION_KEEP,
    )

    # string representation
    def __str__(self):
        return self.main_config_name


class SystemExporterMarkdownConfigModel(models.Model):
    """config for system markdown exporter, single object for DFIRTrack"""

    # primary key
    system_exporter_markdown_config_name = models.CharField(
        max_length=50, primary_key=True, editable=False
    )

    # prepare choices
    DOMAINSORTED = 'dom'
    SYSTEMSORTED = 'sys'
    MARKDOWN_SORTING_CHOICES = [
        (DOMAINSORTED, 'Sorted by domain'),
        (SYSTEMSORTED, 'Sorted by system'),
    ]

    # config fields
    markdown_path = models.CharField(
        max_length=4096, blank=False, null=True
    )  # null is allowed for initial creation of config model via migration, blank is not allowed in form
    markdown_sorting = models.CharField(
        max_length=3,
        choices=MARKDOWN_SORTING_CHOICES,
        default=SYSTEMSORTED,
    )

    # string representation
    def __str__(self):
        return self.system_exporter_markdown_config_name


class SystemExporterSpreadsheetCsvConfigModel(models.Model):
    """config for system spreadsheet CSV exporter, single object for DFIRTrack"""

    # primary key
    system_exporter_spreadsheet_csv_config_name = models.CharField(
        max_length=50, primary_key=True, editable=False
    )

    # config fields
    spread_csv_system_id = models.BooleanField(default=True)
    spread_csv_dnsname = models.BooleanField(default=True)
    spread_csv_domain = models.BooleanField(default=True)
    spread_csv_systemstatus = models.BooleanField(default=True)
    spread_csv_analysisstatus = models.BooleanField(default=False)
    spread_csv_reason = models.BooleanField(default=False)
    spread_csv_recommendation = models.BooleanField(default=False)
    spread_csv_systemtype = models.BooleanField(default=True)
    spread_csv_ip = models.BooleanField(default=True)
    spread_csv_os = models.BooleanField(default=False)
    spread_csv_company = models.BooleanField(default=False)
    spread_csv_location = models.BooleanField(default=False)
    spread_csv_serviceprovider = models.BooleanField(default=False)
    spread_csv_tag = models.BooleanField(default=True)
    spread_csv_case = models.BooleanField(default=False)
    spread_csv_system_create_time = models.BooleanField(default=True)
    spread_csv_system_modify_time = models.BooleanField(default=True)

    # string representation
    def __str__(self):
        return self.system_exporter_spreadsheet_csv_config_name


class SystemExporterSpreadsheetXlsConfigModel(models.Model):
    """config for system spreadsheet XLS exporter, single object for DFIRTrack"""

    # primary key
    system_exporter_spreadsheet_xls_config_name = models.CharField(
        max_length=50, primary_key=True, editable=False
    )

    # config fields
    spread_xls_system_id = models.BooleanField(default=True)
    spread_xls_dnsname = models.BooleanField(default=True)
    spread_xls_domain = models.BooleanField(default=True)
    spread_xls_systemstatus = models.BooleanField(default=True)
    spread_xls_analysisstatus = models.BooleanField(default=False)
    spread_xls_reason = models.BooleanField(default=False)
    spread_xls_recommendation = models.BooleanField(default=False)
    spread_xls_systemtype = models.BooleanField(default=True)
    spread_xls_ip = models.BooleanField(default=True)
    spread_xls_os = models.BooleanField(default=False)
    spread_xls_company = models.BooleanField(default=False)
    spread_xls_location = models.BooleanField(default=False)
    spread_xls_serviceprovider = models.BooleanField(default=False)
    spread_xls_tag = models.BooleanField(default=True)
    spread_xls_case = models.BooleanField(default=False)
    spread_xls_system_create_time = models.BooleanField(default=True)
    spread_xls_system_modify_time = models.BooleanField(default=True)
    spread_xls_worksheet_systemstatus = models.BooleanField(default=False)
    spread_xls_worksheet_analysisstatus = models.BooleanField(default=False)
    spread_xls_worksheet_reason = models.BooleanField(default=False)
    spread_xls_worksheet_recommendation = models.BooleanField(default=False)
    spread_xls_worksheet_tag = models.BooleanField(default=False)

    # string representation
    def __str__(self):
        return self.system_exporter_spreadsheet_xls_config_name


class SystemImporterFileCsvConfigModel(models.Model):
    """config for system file CSV importer, single object for DFIRTrack"""

    # primary key
    system_importer_file_csv_config_name = models.CharField(
        max_length=50, primary_key=True, editable=False
    )

    # generic config fields
    csv_column_system = models.IntegerField(default=1)
    csv_skip_existing_system = models.BooleanField(default=False)
    csv_headline = models.BooleanField(default=True)
    csv_import_path = models.CharField(max_length=4096, default='/tmp')  # nosec
    csv_import_filename = models.CharField(max_length=255, default='systems.csv')

    # user context for imports, null is allowed for initial creation of config model via migration, blank is not allowed in form
    csv_import_username = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='csv_import_username',
        blank=False,
        null=True,
    )

    # mandatory foreignkey relations
    csv_default_systemstatus = models.ForeignKey(
        'dfirtrack_main.Systemstatus',
        on_delete=models.PROTECT,
        related_name='system_importer_file_csv_config_systemstatus',
        default=1,
    )
    csv_remove_systemstatus = models.BooleanField(default=False)
    csv_default_analysisstatus = models.ForeignKey(
        'dfirtrack_main.Analysisstatus',
        on_delete=models.PROTECT,
        related_name='system_importer_file_csv_config_analysisstatus',
        default=1,
    )
    csv_remove_analysisstatus = models.BooleanField(default=False)

    # in case of 'csv_choice_tag' a different status can be assigned if the system has no tags
    csv_choice_tagfree_systemstatus = models.BooleanField(default=False)
    csv_default_tagfree_systemstatus = models.ForeignKey(
        'dfirtrack_main.Systemstatus',
        on_delete=models.PROTECT,
        related_name='system_importer_file_csv_config_tagfree_systemstatus',
        default=1,
    )
    csv_choice_tagfree_analysisstatus = models.BooleanField(default=False)
    csv_default_tagfree_analysisstatus = models.ForeignKey(
        'dfirtrack_main.Analysisstatus',
        on_delete=models.PROTECT,
        related_name='system_importer_file_csv_config_tagfree_analysisstatus',
        default=1,
    )

    # character fields to define names for tags to pin analysisstatus and systemstatus
    csv_tag_lock_systemstatus = models.CharField(
        max_length=50, default='LOCK_SYSTEMSTATUS'
    )
    csv_tag_lock_analysisstatus = models.CharField(
        max_length=50, default='LOCK_ANALYSISSTATUS'
    )

    # config fields: either dynamically provided by CSV (...choice... 'True' and ...column...) or nothing provided (fixed value for all systems makes no sense)
    csv_choice_ip = models.BooleanField(default=False)
    csv_column_ip = models.IntegerField(blank=True, null=True)
    csv_remove_ip = models.BooleanField(default=False)

    # config fields (foreignkey relation): either dynamically provided by CSV (...choice... 'True' and ...column...) or fixed value provided by config (...default...)
    csv_choice_dnsname = models.BooleanField(default=False)
    csv_column_dnsname = models.IntegerField(blank=True, null=True)
    csv_default_dnsname = models.ForeignKey(
        'dfirtrack_main.Dnsname',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_dnsname',
        blank=True,
        null=True,
    )
    csv_remove_dnsname = models.BooleanField(default=False)

    csv_choice_domain = models.BooleanField(default=False)
    csv_column_domain = models.IntegerField(blank=True, null=True)
    csv_default_domain = models.ForeignKey(
        'dfirtrack_main.Domain',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_domain',
        blank=True,
        null=True,
    )
    csv_remove_domain = models.BooleanField(default=False)

    csv_choice_location = models.BooleanField(default=False)
    csv_column_location = models.IntegerField(blank=True, null=True)
    csv_default_location = models.ForeignKey(
        'dfirtrack_main.Location',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_location',
        blank=True,
        null=True,
    )
    csv_remove_location = models.BooleanField(default=False)

    csv_choice_os = models.BooleanField(default=False)
    csv_column_os = models.IntegerField(blank=True, null=True)
    csv_default_os = models.ForeignKey(
        'dfirtrack_main.Os',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_os',
        blank=True,
        null=True,
    )
    csv_remove_os = models.BooleanField(default=False)

    csv_choice_reason = models.BooleanField(default=False)
    csv_column_reason = models.IntegerField(blank=True, null=True)
    csv_default_reason = models.ForeignKey(
        'dfirtrack_main.Reason',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_reason',
        blank=True,
        null=True,
    )
    csv_remove_reason = models.BooleanField(default=False)

    csv_choice_recommendation = models.BooleanField(default=False)
    csv_column_recommendation = models.IntegerField(blank=True, null=True)
    csv_default_recommendation = models.ForeignKey(
        'dfirtrack_main.Recommendation',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_recommendation',
        blank=True,
        null=True,
    )
    csv_remove_recommendation = models.BooleanField(default=False)

    csv_choice_serviceprovider = models.BooleanField(default=False)
    csv_column_serviceprovider = models.IntegerField(blank=True, null=True)
    csv_default_serviceprovider = models.ForeignKey(
        'dfirtrack_main.Serviceprovider',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_serviceprovider',
        blank=True,
        null=True,
    )
    csv_remove_serviceprovider = models.BooleanField(default=False)

    csv_choice_systemtype = models.BooleanField(default=False)
    csv_column_systemtype = models.IntegerField(blank=True, null=True)
    csv_default_systemtype = models.ForeignKey(
        'dfirtrack_main.Systemtype',
        on_delete=models.SET_NULL,
        related_name='system_importer_file_csv_config_systemtype',
        blank=True,
        null=True,
    )
    csv_remove_systemtype = models.BooleanField(default=False)

    # config fields (many to many relation): same as above but additional choice to remove existing relations
    csv_choice_case = models.BooleanField(default=False)
    csv_column_case = models.IntegerField(blank=True, null=True)
    csv_default_case = models.ManyToManyField(
        'dfirtrack_main.Case',
        related_name='system_importer_file_csv_config_case',
        blank=True,
    )
    csv_remove_case = models.BooleanField(default=False)

    csv_choice_company = models.BooleanField(default=False)
    csv_column_company = models.IntegerField(blank=True, null=True)
    csv_default_company = models.ManyToManyField(
        'dfirtrack_main.Company',
        related_name='system_importer_file_csv_config_company',
        blank=True,
    )
    csv_remove_company = models.BooleanField(default=False)

    csv_choice_tag = models.BooleanField(default=False)
    csv_column_tag = models.IntegerField(blank=True, null=True)
    csv_default_tag = models.ManyToManyField(
        'dfirtrack_main.Tag',
        related_name='system_importer_file_csv_config_tag',
        blank=True,
    )

    # how to deal with manual and automatic tags (first remove all tags, only those with a prefix or none)
    TAG_REMOVE_ALL = 'tag_remove_all'
    TAG_REMOVE_PREFIX = 'tag_remove_prefix'
    TAG_REMOVE_NONE = 'tag_remove_none'
    CSV_REMOVE_TAG_CHOICES = [
        (TAG_REMOVE_ALL, 'Remove all tags'),
        (TAG_REMOVE_PREFIX, 'Remove tags with prefix'),
        (TAG_REMOVE_NONE, 'Keep all tags'),
    ]
    csv_remove_tag = models.CharField(
        max_length=50,
        choices=CSV_REMOVE_TAG_CHOICES,
        default=TAG_REMOVE_PREFIX,
    )

    # (optional) marking for tags added via CSV file
    csv_tag_prefix = models.CharField(
        max_length=50, default='AUTO', blank=True, null=True
    )
    TAG_PREFIX_UNDERSCORE = 'tag_prefix_underscore'
    TAG_PREFIX_HYPHEN = 'tag_prefix_hyphen'
    TAG_PREFIX_PERIOD = 'tag_prefix_period'
    CSV_TAG_PREFIX_DELIMITER_CHOICES = [
        (TAG_PREFIX_UNDERSCORE, 'Underscore'),
        (TAG_PREFIX_HYPHEN, 'Hyphen'),
        (TAG_PREFIX_PERIOD, 'Period'),
    ]
    csv_tag_prefix_delimiter = models.CharField(
        max_length=50,
        choices=CSV_TAG_PREFIX_DELIMITER_CHOICES,
        default=TAG_PREFIX_UNDERSCORE,
        blank=True,
        null=True,
    )

    """ CSV format fields """

    # CSV field delimiter
    FIELD_COMMA = 'field_comma'
    FIELD_SEMICOLON = 'field_semicolon'
    CSV_FIELD_DELIMITER_CHOICES = [
        (FIELD_COMMA, 'Comma'),
        (FIELD_SEMICOLON, 'Semicolon'),
    ]
    csv_field_delimiter = models.CharField(
        max_length=50,
        choices=CSV_FIELD_DELIMITER_CHOICES,
        default=FIELD_COMMA,
    )

    # CSV quote character
    TEXT_DOUBLE_QUOTATION_MARKS = 'text_double_quotation_marks'
    TEXT_SINGLE_QUOTATION_MARKS = 'text_single_quotation_marks'
    CSV_TEXT_QUOTE_CHOICES = [
        (TEXT_DOUBLE_QUOTATION_MARKS, 'Double quotation marks'),
        (TEXT_SINGLE_QUOTATION_MARKS, 'Single quotation marks'),
    ]
    csv_text_quote = models.CharField(
        max_length=50,
        choices=CSV_TEXT_QUOTE_CHOICES,
        default=TEXT_DOUBLE_QUOTATION_MARKS,
    )

    # IP field format
    IP_COMMA = 'ip_comma'
    IP_SEMICOLON = 'ip_semicolon'
    IP_SPACE = 'ip_space'
    CSV_IP_DELIMITER_CHOICES = [
        (IP_COMMA, 'Comma'),
        (IP_SEMICOLON, 'Semicolon'),
        (IP_SPACE, 'Space'),
    ]
    csv_ip_delimiter = models.CharField(
        max_length=50,
        choices=CSV_IP_DELIMITER_CHOICES,
        default=IP_SEMICOLON,
    )

    # tag field format
    TAG_COMMA = 'tag_comma'
    TAG_SEMICOLON = 'tag_semicolon'
    TAG_SPACE = 'tag_space'
    CSV_TAG_DELIMITER_CHOICES = [
        (TAG_COMMA, 'Comma'),
        (TAG_SEMICOLON, 'Semicolon'),
        (TAG_SPACE, 'Space'),
    ]
    csv_tag_delimiter = models.CharField(
        max_length=50,
        choices=CSV_TAG_DELIMITER_CHOICES,
        default=TAG_SPACE,
    )

    # string representation
    def __str__(self):
        return self.system_importer_file_csv_config_name


class Statushistory(models.Model):
    """status history, multiple objects for DFIRTrack"""

    # primary key
    statushistory_id = models.AutoField(primary_key=True)

    # config fields
    statushistory_time = models.DateTimeField(auto_now_add=True)

    # string representation
    def __str__(self):
        return self.statushistory_time.strftime('%Y-%m-%d %H:%M')

    def get_absolute_url(self):
        return reverse('status_detail', args=(self.pk,))


class StatushistoryEntry(models.Model):
    """status history entries, multiple objects for status history"""

    # primary key
    statushistoryentry_id = models.AutoField(primary_key=True)

    # foreign key(s)
    statushistory = models.ForeignKey(
        'Statushistory', on_delete=models.CASCADE, editable=False
    )

    # config fields
    statushistoryentry_model_name = models.CharField(max_length=255, editable=False)
    statushistoryentry_model_key = models.CharField(
        max_length=255, blank=True, editable=False
    )
    statushistoryentry_model_value = models.IntegerField(editable=False)


class UserConfigModel(models.Model):
    """user config, single object per user"""

    # user / primary key
    user_config_username = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='filter_username', primary_key=True
    )

    # filter settings - assignment view
    filter_assignment_view_keep = models.BooleanField(default=True)
    filter_assignment_view_case = models.ForeignKey(
        'dfirtrack_main.Case',
        related_name='filter_assignment_view_case',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    filter_assignment_view_tag = models.ForeignKey(
        'dfirtrack_main.Tag',
        related_name='filter_assignment_view_tag',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    filter_assignment_view_user = models.OneToOneField(
        User,
        related_name='filter_assignment_view_tag',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    filter_assignment_view_show_artifact = models.BooleanField(default=True)
    filter_assignment_view_show_case = models.BooleanField(default=True)
    filter_assignment_view_show_note = models.BooleanField(default=True)
    filter_assignment_view_show_reportitem = models.BooleanField(default=True)
    filter_assignment_view_show_system = models.BooleanField(default=True)
    filter_assignment_view_show_tag = models.BooleanField(default=True)
    filter_assignment_view_show_task = models.BooleanField(default=True)

    # filter settings - documentation list
    filter_documentation_list_keep = models.BooleanField(default=True)
    filter_documentation_list_case = models.ForeignKey(
        'dfirtrack_main.Case',
        related_name='filter_documentation_list_case',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    filter_documentation_list_notestatus = models.ForeignKey(
        'dfirtrack_main.Notestatus',
        related_name='filter_documentation_list_notestatus',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    filter_documentation_list_tag = models.ForeignKey(
        'dfirtrack_main.Tag',
        related_name='filter_documentation_list_tag',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # filter settings - system detail
    filter_system_detail_show_artifact = models.BooleanField(default=True)
    filter_system_detail_show_artifact_closed = models.BooleanField(default=False)
    filter_system_detail_show_task = models.BooleanField(default=True)
    filter_system_detail_show_task_closed = models.BooleanField(default=False)
    filter_system_detail_show_technical_information = models.BooleanField(default=False)
    filter_system_detail_show_timeline = models.BooleanField(default=False)
    filter_system_detail_show_virtualization_information = models.BooleanField(
        default=False
    )
    filter_system_detail_show_company_information = models.BooleanField(default=False)
    filter_system_detail_show_systemuser = models.BooleanField(default=False)
    filter_system_detail_show_analystmemo = models.BooleanField(default=False)
    filter_system_detail_show_reportitem = models.BooleanField(default=False)

    # filter settings - system list
    filter_system_list_keep = models.BooleanField(default=True)
    filter_system_list_case = models.ForeignKey(
        'dfirtrack_main.Case',
        related_name='filter_system_list_case',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    filter_system_list_tag = models.ForeignKey(
        'dfirtrack_main.Tag',
        related_name='filter_system_list_tag',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # string representation
    def __str__(self):
        return f'User config {self.user_config_username}'


class Workflow(models.Model):
    """workflow to create tasks and artifacts for systems, multiple objects for DFIRTrack"""

    # primary key
    workflow_id = models.AutoField(primary_key=True)

    # foreign key
    tasknames = models.ManyToManyField(
        'dfirtrack_main.Taskname',
        related_name='main_config_workflow_taskname',
        through='WorkflowDefaultTasknameAttributes',
        blank=True,
    )
    artifacttypes = models.ManyToManyField(
        'dfirtrack_artifacts.Artifacttype',
        related_name='main_config_workflow_artifacttype',
        through='WorkflowDefaultArtifactAttributes',
        blank=True,
    )

    # main entity information
    workflow_name = models.CharField(max_length=50, unique=True)

    # meta information
    workflow_create_time = models.DateTimeField(auto_now_add=True)
    workflow_modify_time = models.DateTimeField(auto_now=True)
    workflow_created_by_user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='workflow_created_by'
    )
    workflow_modified_by_user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='worklfow_modified_by'
    )

    def __str__(self):
        return self.workflow_name

    def get_absolute_url(self):
        return reverse('workflow_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('workflow_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('workflow_delete', args=[self.pk])

    # define logger
    def logger(workflow, request_user, log_text):
        stdlogger.info(
            "{}{} workflow_id: {}|workflow_name:{}".format(
                request_user, log_text, workflow.workflow_id, workflow.workflow_name
            )
        )

    def apply(workflows, system, user):
        errors = 0
        for workflow_id in workflows:
            try:
                workflow = Workflow.objects.get(pk=workflow_id)
                # create tasks based on taskname
                for mapping in WorkflowDefaultTasknameAttributes.objects.filter(
                    workflow=workflow
                ):
                    # avoid circular imports - TODO: needs maintenance
                    from dfirtrack_main.models import Task

                    new_task = Task(taskname=mapping.taskname)
                    new_task.task_created_by_user_id = user
                    new_task.task_modified_by_user_id = user
                    new_task.taskstatus = mapping.task_default_status
                    new_task.taskpriority = mapping.task_default_priority
                    new_task.system = system
                    new_task.save()
                    new_task.logger(str(user), f' CREATED_BY_WORKFLOW_{workflow_id}')
                # create artifact based on artifacttype and artifact default name
                for mapping in WorkflowDefaultArtifactAttributes.objects.filter(
                    workflow=workflow
                ):
                    # avoid circular imports - TODO: needs maintenance
                    from dfirtrack_artifacts.models import Artifact

                    new_artifact = Artifact(
                        artifacttype=mapping.artifacttype,
                        artifact_name=mapping.artifact_default_name,
                    )
                    # new_artifact.artifactpriority = Artifactpriority.objects.get(artifactpriority_name=mapping.artifact_default_priority)
                    new_artifact.artifactpriority = mapping.artifact_default_priority
                    new_artifact.artifactstatus = mapping.artifact_default_status
                    new_artifact.artifact_created_by_user_id = user
                    new_artifact.artifact_modified_by_user_id = user
                    new_artifact.system = system
                    new_artifact.save()
                    new_artifact.logger(
                        str(user), f' CREATED_BY_WORKFLOW_{workflow_id}'
                    )
            except Workflow.DoesNotExist:
                errors += 1
            except ValueError:
                errors += 1
        return errors


class WorkflowDefaultArtifactAttributes(models.Model):
    """artifact assigned to workflow, multiple objects for workflows"""

    # primary key
    workflow_default_artifactname_id = models.AutoField(primary_key=True)

    # foreign key
    artifacttype = models.ForeignKey(
        'dfirtrack_artifacts.Artifacttype',
        on_delete=models.CASCADE,
        related_name='workflow_artifacttype_mapping',
    )
    workflow = models.ForeignKey(
        Workflow, on_delete=models.CASCADE, related_name='workflow_artifactname_mapping'
    )
    artifact_default_priority = models.ForeignKey(
        'dfirtrack_artifacts.Artifactpriority',
        on_delete=models.PROTECT,
        related_name='workflow_default_artifact_priority',
    )
    artifact_default_status = models.ForeignKey(
        'dfirtrack_artifacts.Artifactstatus',
        on_delete=models.PROTECT,
        related_name='workflow_default_artifact_status',
    )

    # main entity
    artifact_default_name = models.CharField(max_length=50)

    def __str__(self):
        return self.artifact_default_name


class WorkflowDefaultTasknameAttributes(models.Model):
    """task assigned to workflow, multiple objects for workflows"""

    # primary key
    workflow_default_taskname_id = models.AutoField(primary_key=True)

    # foreign key
    taskname = models.ForeignKey(
        'dfirtrack_main.Taskname',
        on_delete=models.CASCADE,
        related_name='workflow_taskname_mapping',
    )
    workflow = models.ForeignKey(
        Workflow,
        on_delete=models.CASCADE,
        related_name='workflow_taskattribute_mapping',
    )
    task_default_priority = models.ForeignKey(
        'dfirtrack_main.Taskpriority',
        on_delete=models.PROTECT,
        related_name='workflow_default_task_priority',
    )
    task_default_status = models.ForeignKey(
        'dfirtrack_main.Taskstatus',
        on_delete=models.PROTECT,
        related_name='workflow_default_task_status',
    )

    def __str__(self):
        return self.taskname.taskname_name
