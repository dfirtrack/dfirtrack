from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterSpreadsheetCsvViewTestCase(TestCase):
    """ system exporter spreadsheet CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_spreadsheet_csv', password='XJzSzgX2q39OUWluwxoj')

    def test_system_exporter_spreadsheet_csv_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/csv/system/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_csv_logged_in(self):
        """ test exporter view """

        # login testuser
        self.client.login(username='testuser_system_exporter_spreadsheet_csv', password='XJzSzgX2q39OUWluwxoj')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_csv_redirect(self):
        """ test exporter view """

        # login testuser
        self.client.login(username='testuser_system_exporter_spreadsheet_csv', password='XJzSzgX2q39OUWluwxoj')
        # create url
        destination = urllib.parse.quote('/system/exporter/spreadsheet/csv/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/system', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
