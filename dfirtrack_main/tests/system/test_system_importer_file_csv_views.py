from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemImporterFileCsvViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv', password='dWPkpsI6NodS9xIdS0BK')

    def test_system_importer_file_csv_not_logged_in(self):
        """ test importer view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/importer/file/csv/', safe='')
        # get response
        response = self.client.get('/system/importer/file/csv/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_logged_in(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv', password='dWPkpsI6NodS9xIdS0BK')
        # get response
        response = self.client.get('/system/importer/file/csv/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_template(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv', password='dWPkpsI6NodS9xIdS0BK')
        # get response
        response = self.client.get('/system/importer/file/csv/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv.html')

    def test_system_importer_file_csv_get_user_context(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv', password='dWPkpsI6NodS9xIdS0BK')
        # get response
        response = self.client.get('/system/importer/file/csv/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv')

    def test_system_importer_file_csv_redirect(self):
        """ test importer view """

        # login testuser
        login = self.client.login(username='testuser_system_importer_file_csv', password='dWPkpsI6NodS9xIdS0BK')
        # create url
        destination = urllib.parse.quote('/system/importer/file/csv/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
