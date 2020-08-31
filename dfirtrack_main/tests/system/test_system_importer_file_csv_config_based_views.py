from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemImporterFileCsvConfigbasedViewTestCase(TestCase):
    """ system importer file CSV config-based view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')

    def test_system_importer_file_csv_config_based_not_logged_in(self):
        """ test importer view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/importer/file/csv/configbased/', safe='')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_config_based_logged_in(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_config_based_template(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv_config_based.html')

    def test_system_importer_file_csv_config_based_get_user_context(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_config_based')

    def test_system_importer_file_csv_config_based_redirect(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # create url
        destination = urllib.parse.quote('/system/importer/file/csv/configbased/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
