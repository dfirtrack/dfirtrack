from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterSpreadsheetXlsConfigViewTestCase(TestCase):
    """ system exporter spreadsheet XLS config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_spreadsheet_xls_config', password='dNpRr2hEnnj147CgNhWM')

    def test_system_exporter_spreadsheet_xls_config_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/xls/config/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_config_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls_config', password='dNpRr2hEnnj147CgNhWM')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_xls_config_template(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls_config', password='dNpRr2hEnnj147CgNhWM')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_exporter_spreadsheet_xls_config_popup.html')

    def test_system_exporter_spreadsheet_xls_config_get_user_context(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls_config', password='dNpRr2hEnnj147CgNhWM')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_spreadsheet_xls_config')

    def test_system_exporter_spreadsheet_xls_config_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_xls_config', password='dNpRr2hEnnj147CgNhWM')
        # create url
        destination = urllib.parse.quote('/system/exporter/spreadsheet/xls/config/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/config', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
