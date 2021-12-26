from datetime import datetime
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack_config.models import (
    ArtifactExporterSpreadsheetXlsConfigModel,
    MainConfigModel,
    Statushistory,
    SystemExporterMarkdownConfigModel,
    SystemExporterSpreadsheetCsvConfigModel,
    SystemExporterSpreadsheetXlsConfigModel,
    SystemImporterFileCsvConfigModel,
    UserConfigModel,
)


class ConfigModelTestCase(TestCase):
    """model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(
            username='testuser_config_model', password='4APmzkPrXbUV3p3WV5HN'
        )

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
        pass

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

    def test_statushistory_model_string(self):
        """test string representation"""

        # mock timezone.now()
        t_1 = datetime(2020, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # create object
            statushistory = Statushistory.objects.create()
            # compare
            self.assertEqual(str(statushistory), '2020-01-02 03:04')

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
