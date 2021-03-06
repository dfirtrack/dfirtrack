from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.importer.file.csv import system_cron
import os
import urllib.parse


def change_csv_import_path(csv_import_path):
    """ set csv_import_path """

    # change config
    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
    system_importer_file_csv_config_model.csv_import_path = csv_import_path
    system_importer_file_csv_config_model.save()

    # return to test function
    return

def change_csv_import_filename(csv_import_filename):
    """ set csv_import_filename """

    # change config
    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
    system_importer_file_csv_config_model.csv_import_filename = csv_import_filename
    system_importer_file_csv_config_model.save()

    # return to test function
    return

class SystemImporterFileCsvCheckContentFileTypeViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create users
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        User.objects.create_user(username='message_user', password='a3ZEI74fr0lmA3pSh96b')

        # restore config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_import_username = test_user
        system_importer_file_csv_config_model.save()

    def test_system_importer_file_csv_upload_post_no_file_submitted(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv.html')

    def test_system_importer_file_csv_cron_wrong_type(self):
        """ test importer view """

        # set file system attributes
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files')
        csv_import_filename = 'system_importer_file_csv_testfile_04_wrong_type.png'
        # change config
        change_csv_import_path(csv_import_path)
        change_csv_import_filename(csv_import_filename)
        # execute cron job / scheduled task
        system_cron()
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_check_content_file_type')
        self.assertEqual(messages[0].message, '[Scheduled task CSV system importer] Wrong file type for CSV import. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='a3ZEI74fr0lmA3pSh96b')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, '[Scheduled task CSV system importer] Wrong file type for CSV import. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_importer_file_csv_instant_wrong_type(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # set file system attributes
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files')
        csv_import_filename = 'system_importer_file_csv_testfile_04_wrong_type.png'
        # change config
        change_csv_import_path(csv_import_path)
        change_csv_import_filename(csv_import_filename)
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, 'Wrong file type for CSV import. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_importer_file_csv_upload_post_wrong_type(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_04_wrong_type.png'), 'rb')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, 'Wrong file type for CSV import. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_importer_file_csv_cron_corrupted(self):
        """ test importer view """

        # set file system attributes
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files')
        csv_import_filename = 'system_importer_file_csv_testfile_05_corrupted.csv'
        # change config
        change_csv_import_path(csv_import_path)
        change_csv_import_filename(csv_import_filename)
        # execute cron job / scheduled task
        system_cron()
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_check_content_file_type')
        self.assertEqual(messages[0].message, '[Scheduled task CSV system importer] File is corrupted. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='a3ZEI74fr0lmA3pSh96b')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, '[Scheduled task CSV system importer] File is corrupted. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_importer_file_csv_instant_corrupted(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # set file system attributes
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files')
        csv_import_filename = 'system_importer_file_csv_testfile_05_corrupted.csv'
        # change config
        change_csv_import_path(csv_import_path)
        change_csv_import_filename(csv_import_filename)
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, 'File is corrupted. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_importer_file_csv_upload_post_corrupted(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_content_file_type', password='3oKsgNPVdlmNPneLhdr9')
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_05_corrupted.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, 'File is corrupted. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')
