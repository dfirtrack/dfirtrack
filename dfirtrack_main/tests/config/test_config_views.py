from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterSpreadsheetCsvViewTestCase(TestCase):
    """ config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_spread_csv_config', password='LnbsOcjhzW5ARpWFuj9I')

    def test_system_exporter_spreadsheet_csv_config_popup_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/csv/config/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_csv_config_popup_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_csv_config', password='LnbsOcjhzW5ARpWFuj9I')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/config/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_csv_config_popup_template(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_csv_config', password='LnbsOcjhzW5ARpWFuj9I')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_exporter_spreadsheet_csv_config_popup.html')

    def test_system_exporter_spreadsheet_csv_config_popup_get_user_context(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_csv_config', password='LnbsOcjhzW5ARpWFuj9I')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_spread_csv_config')

    def test_system_exporter_spreadsheet_csv_config_popup_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_csv_config', password='LnbsOcjhzW5ARpWFuj9I')
        # create url
        destination = urllib.parse.quote('/system/exporter/spreadsheet/csv/config/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/config', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

class SystemExporterSpreadsheetXlsViewTestCase(TestCase):
    """ config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_spread_xls_config', password='i4UU1axOcfcV5ldmJrHh')

    def test_system_exporter_spreadsheet_xls_config_popup_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/xls/config/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_config_popup_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_xls_config', password='i4UU1axOcfcV5ldmJrHh')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_xls_config_popup_template(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_xls_config', password='i4UU1axOcfcV5ldmJrHh')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_exporter_spreadsheet_xls_config_popup.html')

    def test_system_exporter_spreadsheet_xls_config_popup_get_user_context(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_xls_config', password='i4UU1axOcfcV5ldmJrHh')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_spread_xls_config')

    def test_system_exporter_spreadsheet_xls_config_popup_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_spread_xls_config', password='i4UU1axOcfcV5ldmJrHh')
        # create url
        destination = urllib.parse.quote('/system/exporter/spreadsheet/xls/config/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
