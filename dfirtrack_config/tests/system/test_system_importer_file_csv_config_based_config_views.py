from django.contrib.auth.models import User
from django.test import TestCase
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
        destination = '/login/?next=' + urllib.parse.quote('/system/importer/file/csv/configbased/config/', safe='')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_config_based_config_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/config/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_config_based_config_template(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv_config_based_config_popup.html')

    def test_system_importer_file_csv_config_based_config_get_user_context(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_config_based_config')

    def test_system_importer_file_csv_config_based_config_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based_config', password='sBH771ZCj2Y5rjfCPtVC')
        # create url
        destination = urllib.parse.quote('/system/importer/file/csv/configbased/config/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/config', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
