from datetime import datetime
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack_artifacts.models import (
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)
from dfirtrack_config.models import (
    ArtifactExporterSpreadsheetXlsConfigModel,
    MainConfigModel,
    Statushistory,
    StatushistoryEntry,
    SystemExporterMarkdownConfigModel,
    SystemExporterSpreadsheetCsvConfigModel,
    SystemExporterSpreadsheetXlsConfigModel,
    SystemImporterFileCsvConfigModel,
    UserConfigModel,
    Workflow,
    WorkflowDefaultArtifactAttributes,
    WorkflowDefaultTasknameAttributes,
)
from dfirtrack_main.models import (
    Taskname,
    Taskstatus,
    Taskpriority,
)


class ConfigModelTestCase(TestCase):
    """model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(
            username='testuser_config_model', password='4APmzkPrXbUV3p3WV5HN'
        )
        # create objects
        Artifactpriority.objects.create(artifactpriority_name='artifactpriority_1')
        Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')
        Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        # create objects
        Taskname.objects.create(taskname_name='taskname_1')
        Taskname.objects.create(taskname_name='taskname_2')
        Taskpriority.objects.create(taskpriority_name='taskpriority_1')
        Taskstatus.objects.create(taskstatus_name='taskstatus_1')

    def test_artifact_exporter_spreadsheet_xls_config_model_string(self):
        """test string representation"""

        # get object
        artifact_exporter_spreadsheet_xls_config_model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(
            artifact_exporter_spreadsheet_xls_config_name='ArtifactExporterSpreadsheetXlsConfig'
        )
        # compare
        self.assertEqual(
            str(artifact_exporter_spreadsheet_xls_config_model),
            'ArtifactExporterSpreadsheetXlsConfig',
        )

    def test_artifact_exporter_spreadsheet_xls_config_model_attribute_labels(self):
        """test attribute labels"""

        # get object
        artifact_exporter_spreadsheet_xls_config_model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(
            artifact_exporter_spreadsheet_xls_config_name='ArtifactExporterSpreadsheetXlsConfig'
        )
        # compare
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifact_exporter_spreadsheet_xls_config_name').verbose_name,'artifact exporter spreadsheet xls config name')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_choice_artifactstatus').verbose_name,'artifactlist xls choice artifactstatus')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_id').verbose_name,'artifactlist xls artifact id')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_system_id').verbose_name,'artifactlist xls system id')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_system_name').verbose_name,'artifactlist xls system name')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifactstatus').verbose_name,'artifactlist xls artifactstatus')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifactpriority').verbose_name,'artifactlist xls artifactpriority')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifacttype').verbose_name,'artifactlist xls artifacttype')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_source_path').verbose_name,'artifactlist xls artifact source path')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_storage_path').verbose_name,'artifactlist xls artifact storage path')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_note_internal').verbose_name,'artifactlist xls artifact note internal')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_note_external').verbose_name,'artifactlist xls artifact note external')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_note_analysisresult').verbose_name,'artifactlist xls artifact note analysisresult')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_md5').verbose_name,'artifactlist xls artifact md5')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_sha1').verbose_name,'artifactlist xls artifact sha1')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_sha256').verbose_name,'artifactlist xls artifact sha256')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_create_time').verbose_name,'artifactlist xls artifact create time')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_artifact_modify_time').verbose_name,'artifactlist xls artifact modify time')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_worksheet_artifactstatus').verbose_name,'artifactlist xls worksheet artifactstatus')
        self.assertEqual(artifact_exporter_spreadsheet_xls_config_model._meta.get_field('artifactlist_xls_worksheet_artifacttype').verbose_name,'artifactlist xls worksheet artifacttype')

    def test_main_config_model_string(self):
        """test string representation"""

        # get object
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # compare
        self.assertEqual(str(main_config_model), 'MainConfig')

    def test_main_config_model_attribute_labels(self):
        """test attribute labels"""

        # get object
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # compare
        self.assertEqual(main_config_model._meta.get_field('main_config_name').verbose_name,'main config name')
        self.assertEqual(main_config_model._meta.get_field('system_name_editable').verbose_name,'system name editable')
        self.assertEqual(main_config_model._meta.get_field('artifactstatus_open').verbose_name,'artifactstatus open')
        self.assertEqual(main_config_model._meta.get_field('artifactstatus_requested').verbose_name,'artifactstatus requested')
        self.assertEqual(main_config_model._meta.get_field('artifactstatus_acquisition').verbose_name,'artifactstatus acquisition')
        self.assertEqual(main_config_model._meta.get_field('casestatus_open').verbose_name,'casestatus open')
        self.assertEqual(main_config_model._meta.get_field('casestatus_start').verbose_name,'casestatus start')
        self.assertEqual(main_config_model._meta.get_field('casestatus_end').verbose_name,'casestatus end')
        self.assertEqual(main_config_model._meta.get_field('statushistory_entry_numbers').verbose_name,'statushistory entry numbers')
        self.assertEqual(main_config_model._meta.get_field('cron_export_path').verbose_name,'cron export path')
        self.assertEqual(main_config_model._meta.get_field('cron_username').verbose_name,'cron username')
        self.assertEqual(main_config_model._meta.get_field('main_overview').verbose_name,'main overview')
        self.assertEqual(main_config_model._meta.get_field('capitalization').verbose_name,'capitalization')

    def test_system_exporter_markdown_config_model_string(self):
        """test string representation"""

        # get object
        system_exporter_markdown_config_model = (
            SystemExporterMarkdownConfigModel.objects.get(
                system_exporter_markdown_config_name='SystemExporterMarkdownConfig'
            )
        )
        # compare
        self.assertEqual(
            str(system_exporter_markdown_config_model), 'SystemExporterMarkdownConfig'
        )

    def test_system_exporter_markdown_config_model_labels(self):
        """test attribute labels"""

        # get object
        system_exporter_markdown_config_model = (
            SystemExporterMarkdownConfigModel.objects.get(
                system_exporter_markdown_config_name='SystemExporterMarkdownConfig'
            )
        )
        # compare
        self.assertEqual(system_exporter_markdown_config_model._meta.get_field('system_exporter_markdown_config_name').verbose_name,'system exporter markdown config name')
        self.assertEqual(system_exporter_markdown_config_model._meta.get_field('markdown_path').verbose_name,'markdown path')
        self.assertEqual(system_exporter_markdown_config_model._meta.get_field('markdown_sorting').verbose_name,'markdown sorting')

    def test_system_exporter_spreadsheet_csv_config_model_string(self):
        """test string representation"""

        # get object
        system_exporter_spreadsheet_csv_config_model = SystemExporterSpreadsheetCsvConfigModel.objects.get(
            system_exporter_spreadsheet_csv_config_name='SystemExporterSpreadsheetCsvConfig'
        )
        # compare
        self.assertEqual(
            str(system_exporter_spreadsheet_csv_config_model),
            'SystemExporterSpreadsheetCsvConfig',
        )

    def test_system_exporter_spreadsheet_csv_config_model_labels(self):
        """test attribute labels"""

        # get object
        system_exporter_spreadsheet_csv_config_model = SystemExporterSpreadsheetCsvConfigModel.objects.get(
            system_exporter_spreadsheet_csv_config_name='SystemExporterSpreadsheetCsvConfig'
        )
        # compare
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('system_exporter_spreadsheet_csv_config_name').verbose_name,'system exporter spreadsheet csv config name')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_system_id').verbose_name,'spread csv system id')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_dnsname').verbose_name,'spread csv dnsname')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_domain').verbose_name,'spread csv domain')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_systemstatus').verbose_name,'spread csv systemstatus')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_analysisstatus').verbose_name,'spread csv analysisstatus')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_reason').verbose_name,'spread csv reason')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_recommendation').verbose_name,'spread csv recommendation')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_systemtype').verbose_name,'spread csv systemtype')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_ip').verbose_name,'spread csv ip')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_os').verbose_name,'spread csv os')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_company').verbose_name,'spread csv company')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_location').verbose_name,'spread csv location')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_serviceprovider').verbose_name,'spread csv serviceprovider')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_tag').verbose_name,'spread csv tag')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_case').verbose_name,'spread csv case')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_system_create_time').verbose_name,'spread csv system create time')
        self.assertEqual(system_exporter_spreadsheet_csv_config_model._meta.get_field('spread_csv_system_modify_time').verbose_name,'spread csv system modify time')

    def test_system_exporter_spreadsheet_xls_config_model_string(self):
        """test string representation"""

        # get object
        system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel.objects.get(
            system_exporter_spreadsheet_xls_config_name='SystemExporterSpreadsheetXlsConfig'
        )
        # compare
        self.assertEqual(
            str(system_exporter_spreadsheet_xls_config_model),
            'SystemExporterSpreadsheetXlsConfig',
        )

    def test_system_exporter_spreadsheet_xls_config_model_labels(self):
        """test attribute labels"""

        # get object
        system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel.objects.get(
            system_exporter_spreadsheet_xls_config_name='SystemExporterSpreadsheetXlsConfig'
        )
        # compare
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('system_exporter_spreadsheet_xls_config_name').verbose_name,'system exporter spreadsheet xls config name')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_system_id').verbose_name,'spread xls system id')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_dnsname').verbose_name,'spread xls dnsname')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_domain').verbose_name,'spread xls domain')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_systemstatus').verbose_name,'spread xls systemstatus')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_analysisstatus').verbose_name,'spread xls analysisstatus')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_reason').verbose_name,'spread xls reason')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_recommendation').verbose_name,'spread xls recommendation')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_systemtype').verbose_name,'spread xls systemtype')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_ip').verbose_name,'spread xls ip')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_os').verbose_name,'spread xls os')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_company').verbose_name,'spread xls company')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_location').verbose_name,'spread xls location')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_serviceprovider').verbose_name,'spread xls serviceprovider')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_tag').verbose_name,'spread xls tag')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_case').verbose_name,'spread xls case')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_system_create_time').verbose_name,'spread xls system create time')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_system_modify_time').verbose_name,'spread xls system modify time')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_worksheet_systemstatus').verbose_name,'spread xls worksheet systemstatus')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_worksheet_analysisstatus').verbose_name,'spread xls worksheet analysisstatus')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_worksheet_reason').verbose_name,'spread xls worksheet reason')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_worksheet_recommendation').verbose_name,'spread xls worksheet recommendation')
        self.assertEqual(system_exporter_spreadsheet_xls_config_model._meta.get_field('spread_xls_worksheet_tag').verbose_name,'spread xls worksheet tag')

    def test_system_importer_file_csv_config_model_string(self):
        """test string representation"""

        # get object
        system_importer_file_csv_config_model = (
            SystemImporterFileCsvConfigModel.objects.get(
                system_importer_file_csv_config_name='SystemImporterFileCsvConfig'
            )
        )
        # compare
        self.assertEqual(
            str(system_importer_file_csv_config_model), 'SystemImporterFileCsvConfig'
        )

    def test_system_importer_file_csv_config_model_labels(self):
        """test attribute labels"""

        # get object
        system_importer_file_csv_config_model = (
            SystemImporterFileCsvConfigModel.objects.get(
                system_importer_file_csv_config_name='SystemImporterFileCsvConfig'
            )
        )
        # compare
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('system_importer_file_csv_config_name').verbose_name,'system importer file csv config name')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_system').verbose_name,'csv column system')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_skip_existing_system').verbose_name,'csv skip existing system')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_headline').verbose_name,'csv headline')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_import_path').verbose_name,'csv import path')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_import_filename').verbose_name,'csv import filename')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_import_username').verbose_name,'csv import username')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_systemstatus').verbose_name,'csv default systemstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_systemstatus').verbose_name,'csv remove systemstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_analysisstatus').verbose_name,'csv default analysisstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_analysisstatus').verbose_name,'csv remove analysisstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_tagfree_systemstatus').verbose_name,'csv choice tagfree systemstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_tagfree_systemstatus').verbose_name,'csv default tagfree systemstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_tagfree_analysisstatus').verbose_name,'csv choice tagfree analysisstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_tagfree_analysisstatus').verbose_name,'csv default tagfree analysisstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_tag_lock_systemstatus').verbose_name,'csv tag lock systemstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_tag_lock_analysisstatus').verbose_name,'csv tag lock analysisstatus')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_ip').verbose_name,'csv choice ip')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_ip').verbose_name,'csv column ip')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_ip').verbose_name,'csv remove ip')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_dnsname').verbose_name,'csv choice dnsname')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_dnsname').verbose_name,'csv column dnsname')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_dnsname').verbose_name,'csv default dnsname')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_dnsname').verbose_name,'csv remove dnsname')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_domain').verbose_name,'csv choice domain')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_domain').verbose_name,'csv column domain')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_domain').verbose_name,'csv default domain')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_domain').verbose_name,'csv remove domain')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_location').verbose_name,'csv choice location')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_location').verbose_name,'csv column location')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_location').verbose_name,'csv default location')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_location').verbose_name,'csv remove location')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_os').verbose_name,'csv choice os')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_os').verbose_name,'csv column os')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_os').verbose_name,'csv default os')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_os').verbose_name,'csv remove os')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_reason').verbose_name,'csv choice reason')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_reason').verbose_name,'csv column reason')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_reason').verbose_name,'csv default reason')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_reason').verbose_name,'csv remove reason')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_recommendation').verbose_name,'csv choice recommendation')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_recommendation').verbose_name,'csv column recommendation')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_recommendation').verbose_name,'csv default recommendation')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_recommendation').verbose_name,'csv remove recommendation')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_serviceprovider').verbose_name,'csv choice serviceprovider')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_serviceprovider').verbose_name,'csv column serviceprovider')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_serviceprovider').verbose_name,'csv default serviceprovider')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_serviceprovider').verbose_name,'csv remove serviceprovider')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_systemtype').verbose_name,'csv choice systemtype')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_systemtype').verbose_name,'csv column systemtype')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_systemtype').verbose_name,'csv default systemtype')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_systemtype').verbose_name,'csv remove systemtype')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_case').verbose_name,'csv choice case')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_case').verbose_name,'csv column case')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_case').verbose_name,'csv default case')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_case').verbose_name,'csv remove case')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_company').verbose_name,'csv choice company')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_company').verbose_name,'csv column company')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_company').verbose_name,'csv default company')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_company').verbose_name,'csv remove company')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_choice_tag').verbose_name,'csv choice tag')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_column_tag').verbose_name,'csv column tag')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_default_tag').verbose_name,'csv default tag')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_remove_tag').verbose_name,'csv remove tag')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_tag_prefix').verbose_name,'csv tag prefix')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_tag_prefix_delimiter').verbose_name,'csv tag prefix delimiter')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_field_delimiter').verbose_name,'csv field delimiter')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_text_quote').verbose_name,'csv text quote')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_ip_delimiter').verbose_name,'csv ip delimiter')
        self.assertEqual(system_importer_file_csv_config_model._meta.get_field('csv_tag_delimiter').verbose_name,'csv tag delimiter')

    def test_statushistory_model_string(self):
        """test string representation"""

        # mock timezone.now()
        t_1 = datetime(2020, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # create object
            statushistory = Statushistory.objects.create()

        # compare
        self.assertEqual(str(statushistory), '2020-01-02 03:04')

    def test_statushistory_model_absolute_url(self):
        """test absolute URL"""

        # mock timezone.now()
        t_3 = datetime(2021, 12, 31, 1, 2, 3, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_3):

            # create object
            statushistory = Statushistory.objects.create()

        # compare
        self.assertEqual(statushistory.get_absolute_url(), f'/config/status/{statushistory.statushistory_id}/')

    def test_statushistory_model_labels(self):
        """test attribute labels"""

        # mock timezone.now()
        t_2 = datetime(2021, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_2):

            # create object
            statushistory = Statushistory.objects.create()

        # compare
        self.assertEqual(str(statushistory), '2021-01-02 03:04')
        self.assertEqual(statushistory._meta.get_field('statushistory_id').verbose_name,'statushistory id')
        self.assertEqual(statushistory._meta.get_field('statushistory_time').verbose_name,'statushistory time')

    def test_statushistory_entry_model_labels(self):
        """test attribute labels"""

        # create object
        statushistory = Statushistory.objects.create()
        # create object
        statushistory_entry = StatushistoryEntry.objects.create(
            statushistory=statushistory,
            statushistoryentry_model_name='statushistoryentry_model_name_1',
            statushistoryentry_model_key='statushistoryentry_model_key_1',
            statushistoryentry_model_value=42,
        )
        # compare
        self.assertEqual(statushistory_entry._meta.get_field('statushistoryentry_id').verbose_name,'statushistoryentry id')
        self.assertEqual(statushistory_entry._meta.get_field('statushistory').verbose_name,'statushistory')
        self.assertEqual(statushistory_entry._meta.get_field('statushistoryentry_model_name').verbose_name,'statushistoryentry model name')
        self.assertEqual(statushistory_entry._meta.get_field('statushistoryentry_model_key').verbose_name,'statushistoryentry model key')
        self.assertEqual(statushistory_entry._meta.get_field('statushistoryentry_model_value').verbose_name,'statushistoryentry model value')

    def test_user_config_model_string(self):
        """test string representation"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # create config model object
        user_config_model = UserConfigModel.objects.create(
            user_config_username=test_user,
        )
        # compare
        self.assertEqual(str(user_config_model), 'User config testuser_config_model')

    def test_user_config_model_labels(self):
        """test attribute labels"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # create config model object
        user_config_model = UserConfigModel.objects.create(
            user_config_username=test_user,
        )
        # compare
        self.assertEqual(user_config_model._meta.get_field('user_config_username').verbose_name,'user config username')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_keep').verbose_name,'filter assignment view keep')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_case').verbose_name,'filter assignment view case')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_tag').verbose_name,'filter assignment view tag')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_user').verbose_name,'filter assignment view user')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_artifact').verbose_name,'filter assignment view show artifact')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_case').verbose_name,'filter assignment view show case')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_note').verbose_name,'filter assignment view show note')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_reportitem').verbose_name,'filter assignment view show reportitem')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_system').verbose_name,'filter assignment view show system')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_tag').verbose_name,'filter assignment view show tag')
        self.assertEqual(user_config_model._meta.get_field('filter_assignment_view_show_task').verbose_name,'filter assignment view show task')
        self.assertEqual(user_config_model._meta.get_field('filter_documentation_list_keep').verbose_name,'filter documentation list keep')
        self.assertEqual(user_config_model._meta.get_field('filter_documentation_list_case').verbose_name,'filter documentation list case')
        self.assertEqual(user_config_model._meta.get_field('filter_documentation_list_notestatus').verbose_name,'filter documentation list notestatus')
        self.assertEqual(user_config_model._meta.get_field('filter_documentation_list_tag').verbose_name,'filter documentation list tag')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_artifact').verbose_name,'filter system detail show artifact')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_artifact_closed').verbose_name,'filter system detail show artifact closed')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_task').verbose_name,'filter system detail show task')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_task_closed').verbose_name,'filter system detail show task closed')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_technical_information').verbose_name,'filter system detail show technical information')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_timeline').verbose_name,'filter system detail show timeline')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_virtualization_information').verbose_name,'filter system detail show virtualization information')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_company_information').verbose_name,'filter system detail show company information')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_systemuser').verbose_name,'filter system detail show systemuser')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_analystmemo').verbose_name,'filter system detail show analystmemo')
        self.assertEqual(user_config_model._meta.get_field('filter_system_detail_show_reportitem').verbose_name,'filter system detail show reportitem')
        self.assertEqual(user_config_model._meta.get_field('filter_system_list_keep').verbose_name,'filter system list keep')
        self.assertEqual(user_config_model._meta.get_field('filter_system_list_case').verbose_name,'filter system list case')
        self.assertEqual(user_config_model._meta.get_field('filter_system_list_tag').verbose_name,'filter system list tag')

    def test_workflow_model_string(self):
        """test string representation"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # create object
        workflow = Workflow.objects.create(
            workflow_name='workflow_string',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )
        # compare
        self.assertEqual(str(workflow),'workflow_string')

    def test_workflow_model_labels(self):
        """test attribute labels"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # create object
        workflow = Workflow.objects.create(
            workflow_name='workflow_labels',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )
        # compare
        self.assertEqual(workflow._meta.get_field('workflow_id').verbose_name,'workflow id')
        self.assertEqual(workflow._meta.get_field('tasknames').verbose_name,'tasknames')
        self.assertEqual(workflow._meta.get_field('artifacttypes').verbose_name,'artifacttypes')
        self.assertEqual(workflow._meta.get_field('workflow_name').verbose_name,'workflow name')
        self.assertEqual(workflow._meta.get_field('workflow_create_time').verbose_name,'workflow create time')
        self.assertEqual(workflow._meta.get_field('workflow_modify_time').verbose_name,'workflow modify time')
        self.assertEqual(workflow._meta.get_field('workflow_created_by_user_id').verbose_name,'workflow created by user id')
        self.assertEqual(workflow._meta.get_field('workflow_modified_by_user_id').verbose_name,'workflow modified by user id')

    def test_workflow_default_artifact_attributes_model_string(self):
        """test string representation"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='artifactpriority_1')
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # create object
        workflow = Workflow.objects.create(
            workflow_name='workflow_default_artifact_string',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )
        # create object
        default_artifact = WorkflowDefaultArtifactAttributes.objects.create(
            workflow=workflow,
            artifact_default_priority=artifactpriority_1,
            artifact_default_status=artifactstatus_1,
            artifacttype=artifacttype_1,
            artifact_default_name='artifact_default_name_1',
        )
        # compare
        self.assertEqual(str(default_artifact),'artifact_default_name_1')

    def test_workflow_default_artifact_attributes_model_labels(self):
        """test attribute labels"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='artifactpriority_1')
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # create object
        workflow = Workflow.objects.create(
            workflow_name='workflow_default_artifact_labels',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )
        # create object
        default_artifact = WorkflowDefaultArtifactAttributes.objects.create(
            workflow=workflow,
            artifact_default_priority=artifactpriority_1,
            artifact_default_status=artifactstatus_1,
            artifacttype=artifacttype_1,
            artifact_default_name='artifact_default_name_2',
        )
        # compare
        self.assertEqual(default_artifact._meta.get_field('workflow_default_artifactname_id').verbose_name,'workflow default artifactname id')
        self.assertEqual(default_artifact._meta.get_field('workflow').verbose_name,'workflow')
        self.assertEqual(default_artifact._meta.get_field('artifact_default_priority').verbose_name,'artifact default priority')
        self.assertEqual(default_artifact._meta.get_field('artifact_default_status').verbose_name,'artifact default status')
        self.assertEqual(default_artifact._meta.get_field('artifacttype').verbose_name,'artifacttype')
        self.assertEqual(default_artifact._meta.get_field('artifact_default_name').verbose_name,'artifact default name')

    def test_workflow_default_taskname_attributes_model_string(self):
        """test string representation"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # get objects
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='taskpriority_1')
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # create object
        workflow = Workflow.objects.create(
            workflow_name='workflow_default_taskname_string',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )
        # create object
        default_taskname = WorkflowDefaultTasknameAttributes.objects.create(
            workflow=workflow,
            taskname=taskname_1,
            task_default_priority=taskpriority_1,
            task_default_status=taskstatus_1,
        )
        # compare
        self.assertEqual(str(default_taskname),'taskname_1')

    def test_workflow_default_taskname_attributes_model_labels(self):
        """test attribute labels"""

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # get objects
        taskname_2 = Taskname.objects.get(taskname_name='taskname_2')
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='taskpriority_1')
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # create object
        workflow = Workflow.objects.create(
            workflow_name='workflow_default_taskname_labels',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )
        # create object
        default_taskname = WorkflowDefaultTasknameAttributes.objects.create(
            workflow=workflow,
            taskname=taskname_2,
            task_default_priority=taskpriority_1,
            task_default_status=taskstatus_1,
        )
        # compare
        self.assertEqual(default_taskname._meta.get_field('workflow_default_taskname_id').verbose_name,'workflow default taskname id')
        self.assertEqual(default_taskname._meta.get_field('workflow').verbose_name,'workflow')
        self.assertEqual(default_taskname._meta.get_field('taskname').verbose_name,'taskname')
        self.assertEqual(default_taskname._meta.get_field('task_default_priority').verbose_name,'task default priority')
        self.assertEqual(default_taskname._meta.get_field('task_default_status').verbose_name,'task default status')
