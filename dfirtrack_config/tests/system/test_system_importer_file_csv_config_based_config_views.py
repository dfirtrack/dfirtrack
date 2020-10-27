from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Analysisstatus, Systemstatus
import urllib.parse

class SystemImporterFileCsvConfigbasedConfigViewTestCase(TestCase):
    """ system importer file CSV config-based config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')

    def test_system_importer_file_csv_config_based_config_not_logged_in(self):
        """ test importer view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/system/importer/file/csv/configbased/', safe='')
        # get response
        response = self.client.get('/config/system/importer/file/csv/configbased/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_config_based_config_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get response
        response = self.client.get('/config/system/importer/file/csv/configbased/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_config_based_config_template(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get response
        response = self.client.get('/config/system/importer/file/csv/configbased/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/system/system_importer_file_csv_config_based_config_popup.html')

    def test_system_importer_file_csv_config_based_config_get_user_context(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get response
        response = self.client.get('/config/system/importer/file/csv/configbased/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_config_based_config')

    def test_system_importer_file_csv_config_based_config_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # create url
        destination = urllib.parse.quote('/config/system/importer/file/csv/configbased/', safe='/')
        # get response
        response = self.client.get('/config/system/importer/file/csv/configbased', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_importer_file_csv_config_based_config_post_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='Unknown').systemstatus_id
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='Needs analysis').analysisstatus_id
        # create post data
        data_dict = {
            'csv_default_systemstatus': systemstatus_id,
            'csv_default_analysisstatus': analysisstatus_id,
            'csv_column_system': 1,
            'csv_column_ip': 2,
        }
        # get response
        response = self.client.post('/config/system/importer/file/csv/configbased/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_config_based_config_post_invalid_reload(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='Unknown').systemstatus_id
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='Needs analysis').analysisstatus_id
        # create post data
        data_dict = {
            'csv_default_systemstatus': systemstatus_id,
            'csv_default_analysisstatus': analysisstatus_id,
            'csv_column_system': 1,
            'csv_column_ip': 1,
        }
        # get response
        response = self.client.post('/config/system/importer/file/csv/configbased/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_config_based_config_post_invalid_template(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='Unknown').systemstatus_id
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='Needs analysis').analysisstatus_id
        # create post data
        data_dict = {
            'csv_default_systemstatus': systemstatus_id,
            'csv_default_analysisstatus': analysisstatus_id,
            'csv_column_system': 2,
            'csv_column_ip': 2,
        }
        # get response
        response = self.client.post('/config/system/importer/file/csv/configbased/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/system/system_importer_file_csv_config_based_config_popup.html')
