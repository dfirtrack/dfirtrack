from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemImporterFileCsvFormbasedViewTestCase(TestCase):
    """ system importer file CSV form-based view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_form_based', password='h3v1BVjsdpJu6sAnSP7e')

    def test_system_importer_file_csv_form_based_not_logged_in(self):
        """ test importer view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/importer/file/csv/formbased/', safe='')
        # get response
        response = self.client.get('/system/importer/file/csv/formbased/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_form_based_logged_in(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_form_based', password='h3v1BVjsdpJu6sAnSP7e')
        # get response
        response = self.client.get('/system/importer/file/csv/formbased/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_form_based_template(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_form_based', password='h3v1BVjsdpJu6sAnSP7e')
        # get response
        response = self.client.get('/system/importer/file/csv/formbased/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv_form_based.html')

    def test_system_importer_file_csv_form_based_get_user_context(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_form_based', password='h3v1BVjsdpJu6sAnSP7e')
        # get response
        response = self.client.get('/system/importer/file/csv/formbased/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_form_based')

    def test_system_importer_file_csv_form_based_redirect(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_form_based', password='h3v1BVjsdpJu6sAnSP7e')
        # create url
        destination = urllib.parse.quote('/system/importer/file/csv/formbased/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/formbased', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
