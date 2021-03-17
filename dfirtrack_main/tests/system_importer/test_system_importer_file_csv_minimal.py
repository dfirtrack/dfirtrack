from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.importer.file.csv import system_cron
from dfirtrack_main.models import Analysisstatus, Domain, System, Systemstatus
from dfirtrack_main.tests.system_importer.config_functions import set_csv_import_filename, set_csv_import_path
from mock import patch
import os
import urllib.parse


def compare_messages_csv(self, messages):
    """ compare messages """

    # compare - messages
    self.assertEqual(messages[0].message, '3 systems were created.')
    self.assertEqual(messages[0].level_tag, 'success')

    # return to test function
    return self

def compare_system_and_attributes_csv(self, file_number):
    """ compare systems and associated attributes """

    # get objects
    analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
    systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')

    # compare - existence of objects
    self.assertTrue(System.objects.filter(system_name=f'system_csv_{file_number}_001').exists())
    self.assertTrue(System.objects.filter(system_name=f'system_csv_{file_number}_002').exists())
    self.assertTrue(System.objects.filter(system_name=f'system_csv_{file_number}_003').exists())
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_001').analysisstatus, analysisstatus_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_002').analysisstatus, analysisstatus_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_003').analysisstatus, analysisstatus_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_001').systemstatus, systemstatus_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_002').systemstatus, systemstatus_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_003').systemstatus, systemstatus_1)

    # return to test function
    return self

def compare_delimiter_specific(self, file_number):
    """ compare delimiter specific results  """

    # compare domain (delimiter specific)
    self.assertTrue(Domain.objects.filter(domain_name=f'domain_{file_number}_1').exists())
    domain_1 = Domain.objects.get(domain_name=f'domain_{file_number}_1')
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_001').domain, domain_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_002').domain, domain_1)
    self.assertEqual(System.objects.get(system_name=f'system_csv_{file_number}_003').domain, domain_1)

    # return to test function
    return self

class SystemImporterFileCsvMinimalViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):
        """ one-time setup """

        # create user
        User.objects.create_user(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        User.objects.create_user(username='message_user', password='UFPntl9kU9vYkXwAo9SS')

        # create objects
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_2')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_2')

    @classmethod
    def setUp(cls):
        """ setup in advance of every test """

        # get user
        test_user = User.objects.get(username='testuser_system_importer_file_csv_minimal')

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        analysisstatus_2 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_2')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')

        # build local path with test files
        set_csv_import_path(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/'))

        # TODO: [maintenance] upload_post related
        #csv_import_path = '/tmp'
        #csv_import_filename = 'system.csv'

        # restore config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_column_system = 1
        system_importer_file_csv_config_model.csv_skip_existing_system = True
        system_importer_file_csv_config_model.csv_headline = False
        system_importer_file_csv_config_model.csv_import_username = test_user
        system_importer_file_csv_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_config_model.csv_default_tagfree_systemstatus = systemstatus_2
        system_importer_file_csv_config_model.csv_default_tagfree_analysisstatus = analysisstatus_2
        system_importer_file_csv_config_model.csv_tag_lock_systemstatus = 'LOCK_SYSTEMSTATUS'
        system_importer_file_csv_config_model.csv_tag_lock_analysisstatus = 'LOCK_ANALYSISSTATUS'
        system_importer_file_csv_config_model.csv_remove_tag = 'tag_remove_prefix'
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_text_quote = 'text_double_quotation_marks'
        system_importer_file_csv_config_model.csv_ip_delimiter = 'ip_semicolon'
        system_importer_file_csv_config_model.csv_tag_delimiter = 'tag_space'
        system_importer_file_csv_config_model.save()

    def test_system_importer_file_csv_cron_minimal_double_quotation(self):
        """ test importer view """

        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_01_minimal_double_quotation.csv')

        # mock timezone.now()
        t_1 = datetime(2021, 3, 6, 17, 28, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # execute cron job / scheduled task
            system_cron()

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 1
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_minimal')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:28:00 - 2021-03-06 17:28:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='UFPntl9kU9vYkXwAo9SS')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 2
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:28:00 - 2021-03-06 17:28:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '01')

    def test_system_importer_file_csv_instant_minimal_double_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_01_minimal_double_quotation.csv')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '01')

    def test_system_importer_file_csv_upload_post_minimal_double_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_01_minimal_double_quotation.csv'), 'r')
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
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '01')

    def test_system_importer_file_csv_cron_minimal_single_quotation(self):
        """ test importer view """

        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_02_minimal_single_quotation.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_text_quote = 'text_single_quotation_marks'
        system_importer_file_csv_config_model.save()

        # mock timezone.now()
        t_2 = datetime(2021, 3, 6, 17, 55, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_2):

            # execute cron job / scheduled task
            system_cron()

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 1
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_minimal')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:55:00 - 2021-03-06 17:55:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='UFPntl9kU9vYkXwAo9SS')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 2
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:55:00 - 2021-03-06 17:55:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '02')

    def test_system_importer_file_csv_instant_minimal_single_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_02_minimal_single_quotation.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_text_quote = 'text_single_quotation_marks'
        system_importer_file_csv_config_model.save()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '02')

    def test_system_importer_file_csv_upload_post_minimal_single_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_text_quote = 'text_single_quotation_marks'
        system_importer_file_csv_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_02_minimal_single_quotation.csv'), 'r')
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
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '02')

    def test_system_importer_file_csv_cron_minimal_headline(self):
        """ test importer view """

        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_03_minimal_headline.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_headline = True
        system_importer_file_csv_config_model.save()

        # mock timezone.now()
        t_3 = datetime(2021, 3, 6, 18, 7, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_3):

            # execute cron job / scheduled task
            system_cron()

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 1
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_minimal')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 18:07:00 - 2021-03-06 18:07:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='UFPntl9kU9vYkXwAo9SS')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 2
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 18:07:00 - 2021-03-06 18:07:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '03')

    def test_system_importer_file_csv_instant_minimal_headline(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_03_minimal_headline.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_headline = True
        system_importer_file_csv_config_model.save()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '03')

    def test_system_importer_file_csv_upload_post_minimal_headline(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_headline = True
        system_importer_file_csv_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_03_minimal_headline.csv'), 'r')
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
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '03')

    def test_system_importer_file_csv_cron_minimal_comma(self):
        """ test importer view """

        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_21_minimal_comma.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
        system_importer_file_csv_config_model.save()

        # mock timezone.now()
        t_5 = datetime(2021, 3, 7, 21, 12, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_5):

            # execute cron job / scheduled task
            system_cron()

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 1
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_minimal')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:12:00 - 2021-03-07 21:12:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='UFPntl9kU9vYkXwAo9SS')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 2
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:12:00 - 2021-03-07 21:12:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '21')
        # compare domain (delimiter specific)
        compare_delimiter_specific(self, '21')

    def test_system_importer_file_csv_instant_minimal_comma(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_21_minimal_comma.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
        system_importer_file_csv_config_model.save()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '21')
        # compare domain (delimiter specific)
        compare_delimiter_specific(self, '21')

    def test_system_importer_file_csv_upload_post_minimal_minimal_comma(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
        system_importer_file_csv_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_21_minimal_comma.csv'), 'r')
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
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '21')
        # compare domain (delimiter specific)
        compare_delimiter_specific(self, '21')

    def test_system_importer_file_csv_cron_minimal_semicolon(self):
        """ test importer view """

        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_22_minimal_semicolon.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_semicolon'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
        system_importer_file_csv_config_model.save()

        # mock timezone.now()
        t_6 = datetime(2021, 3, 7, 21, 17, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_6):

            # execute cron job / scheduled task
            system_cron()

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 1
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_minimal')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:17:00 - 2021-03-07 21:17:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='UFPntl9kU9vYkXwAo9SS')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - user 2
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:17:00 - 2021-03-07 21:17:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '22')
        # compare domain (delimiter specific)
        compare_delimiter_specific(self, '22')

    def test_system_importer_file_csv_instant_minimal_semicolon(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        set_csv_import_filename('system_importer_file_csv_testfile_22_minimal_semicolon.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_semicolon'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
        system_importer_file_csv_config_model.save()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '22')
        # compare domain (delimiter specific)
        compare_delimiter_specific(self, '22')

    def test_system_importer_file_csv_upload_post_minimal_minimal_semicolon(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_minimal', password='H6mM7kq9sEZLvm6CyOaW')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_semicolon'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
        system_importer_file_csv_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_22_minimal_semicolon.csv'), 'r')
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
        # compare - meta
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        # compare - messages
        compare_messages_csv(self, messages)
        # compare - systems / attributes
        compare_system_and_attributes_csv(self, '22')
        # compare domain (delimiter specific)
        compare_delimiter_specific(self, '22')
