from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class ArtifactExporterSpreadsheetXlsConfigViewTestCase(TestCase):
    """ artifact exporter spreadsheet XLS config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')

    def test_artifact_exporter_spreadsheet_xls_config_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/artifact/exporter/spreadsheet/xls/', safe='')
        # get response
        response = self.client.get('/config/artifact/exporter/spreadsheet/xls/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_exporter_spreadsheet_xls_config_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')
        # get response
        response = self.client.get('/config/artifact/exporter/spreadsheet/xls/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_exporter_spreadsheet_xls_config_template(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')
        # get response
        response = self.client.get('/config/artifact/exporter/spreadsheet/xls/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/artifact/artifact_exporter_spreadsheet_xls_config_popup.html')

    def test_artifact_exporter_spreadsheet_xls_config_get_user_context(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')
        # get response
        response = self.client.get('/config/artifact/exporter/spreadsheet/xls/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact_exporter_spreadsheet_xls_config')

    def test_artifact_exporter_spreadsheet_xls_config_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')
        # create url
        destination = urllib.parse.quote('/config/artifact/exporter/spreadsheet/xls/', safe='/')
        # get response
        response = self.client.get('/config/artifact/exporter/spreadsheet/xls', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_artifact_exporter_spreadsheet_xls_config_post_invalid_reload(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/config/artifact/exporter/spreadsheet/xls/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_exporter_spreadsheet_xls_config_post_invalid_template(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls_config', password='i3jLLnbrAEgel24sGs9i')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/config/artifact/exporter/spreadsheet/xls/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/artifact/artifact_exporter_spreadsheet_xls_config_popup.html')
