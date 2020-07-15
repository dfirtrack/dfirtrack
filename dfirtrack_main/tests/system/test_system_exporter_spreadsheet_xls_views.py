from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterSpreadsheetXlsViewTestCase(TestCase):
    """ system exporter spreadsheet XLS view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')

    def test_system_exporter_spreadsheet_xls_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/xls/system/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_logged_in(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_xls_redirect(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
        # create url
        destination = urllib.parse.quote('/system/exporter/spreadsheet/xls/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_config_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/xls/config/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_config_template(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_exporter_spreadsheet_xls_config_popup.html')

    def test_system_exporter_spreadsheet_xls_config_get_user_context(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_spreadsheet_xls')
