from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_config.models import ArtifactExporterSpreadsheetXlsConfigModel
from dfirtrack_config.models import MainConfigModel
from dfirtrack_config.models import SystemExporterMarkdownConfigModel
from dfirtrack_config.models import SystemExporterSpreadsheetCsvConfigModel
from dfirtrack_config.models import SystemExporterSpreadsheetXlsConfigModel
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_config.models import Statushistory
from dfirtrack_config.models import UserConfigModel
from mock import patch


class ConfigModelTestCase(TestCase):
    """ model tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_config_model', password='4APmzkPrXbUV3p3WV5HN')

    def test_artifact_exporter_spreadsheet_xls_config_model_string(self):
        """ test string representation """

        # get object
        artifact_exporter_spreadsheet_xls_config_model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(artifact_exporter_spreadsheet_xls_config_name = 'ArtifactExporterSpreadsheetXlsConfig')
        # compare
        self.assertEqual(str(artifact_exporter_spreadsheet_xls_config_model), 'ArtifactExporterSpreadsheetXlsConfig')

    def test_main_config_model_string(self):
        """ test string representation """

        # get object
        main_config_model = MainConfigModel.objects.get(main_config_name = 'MainConfig')
        # compare
        self.assertEqual(str(main_config_model), 'MainConfig')

    def test_system_exporter_markdown_config_model_string(self):
        """ test string representation """

        # get object
        system_exporter_markdown_config_model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')
        # compare
        self.assertEqual(str(system_exporter_markdown_config_model), 'SystemExporterMarkdownConfig')

    def test_system_exporter_spreadsheet_csv_config_model_string(self):
        """ test string representation """

        # get object
        system_exporter_spreadsheet_csv_config_model = SystemExporterSpreadsheetCsvConfigModel.objects.get(system_exporter_spreadsheet_csv_config_name = 'SystemExporterSpreadsheetCsvConfig')
        # compare
        self.assertEqual(str(system_exporter_spreadsheet_csv_config_model), 'SystemExporterSpreadsheetCsvConfig')

    def test_system_exporter_spreadsheet_xls_config_model_string(self):
        """ test string representation """

        # get object
        system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel.objects.get(system_exporter_spreadsheet_xls_config_name = 'SystemExporterSpreadsheetXlsConfig')
        # compare
        self.assertEqual(str(system_exporter_spreadsheet_xls_config_model), 'SystemExporterSpreadsheetXlsConfig')

    def test_system_importer_file_csv_config_model_string(self):
        """ test string representation """

        # get object
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name = 'SystemImporterFileCsvConfig')
        # compare
        self.assertEqual(str(system_importer_file_csv_config_model), 'SystemImporterFileCsvConfig')

    def test_statushistory_model_string(self):
        """ test string representation """

        # mock timezone.now()
        t_1 = datetime(2020, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # create object
            statushistory = Statushistory.objects.create()
            # compare
            self.assertEqual(str(statushistory), '2020-01-02 03:04')

    def test_user_config_model_string(self):
        """ test string representation """

        # get user
        test_user = User.objects.get(username='testuser_config_model')
        # create config model object
        user_config_model = UserConfigModel.objects.create(
            user_config_username = test_user,
        )
        # compare
        self.assertEqual(str(user_config_model), 'User config testuser_config_model')
