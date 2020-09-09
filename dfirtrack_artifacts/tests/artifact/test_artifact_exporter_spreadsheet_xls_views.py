from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class ArtifactExporterSpreadsheetXlsViewTestCase(TestCase):
    """ artifact exporter spreadsheet XLS view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact_exporter_spreadsheet_xls', password='LTzoNHIdxiJydsaJKf1G')

    def test_artifact_exporter_spreadsheet_xls_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/artifacts/artifact/exporter/spreadsheet/xls/artifact/', safe='')
        # get response
        response = self.client.get('/artifacts/artifact/exporter/spreadsheet/xls/artifact/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_exporter_spreadsheet_xls_logged_in(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls', password='LTzoNHIdxiJydsaJKf1G')
        # get response
        response = self.client.get('/artifacts/artifact/exporter/spreadsheet/xls/artifact/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_exporter_spreadsheet_xls_redirect(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_artifact_exporter_spreadsheet_xls', password='LTzoNHIdxiJydsaJKf1G')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/exporter/spreadsheet/xls/artifact/', safe='/')
        # get response
        response = self.client.get('/artifacts/artifact/exporter/spreadsheet/xls/artifact', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
