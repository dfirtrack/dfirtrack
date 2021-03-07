from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.importer.file.csv import system_cron
from dfirtrack_main.models import Analysisstatus, Systemstatus
from dfirtrack_main.tests.system_importer.config_functions import change_csv_import_filename
from mock import patch
import os


def set_csv_skip_existing_system(csv_skip_existing_system):
    """ set csv_skip_existing_system """

    # restore config
    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
    system_importer_file_csv_config_model.csv_skip_existing_system = csv_skip_existing_system
    system_importer_file_csv_config_model.save()

    # return to test function
    return

class SystemImporterFileCsvMessagesViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):
        """ one-time setup """

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_messages', password='a9aZU5mlnXbVv4TTgcMW')
        User.objects.create_user(username='message_user', password='uNQIBX9woW0M834mJWex')

        # create objects
        analysisstatus_1 = Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        analysisstatus_2 = Analysisstatus.objects.create(analysisstatus_name='analysisstatus_2')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.create(systemstatus_name='systemstatus_2')

        # build local path with test files
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/')

        # restore config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_column_system = 1
        system_importer_file_csv_config_model.csv_headline = False
        system_importer_file_csv_config_model.csv_import_path = csv_import_path
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

    def test_system_importer_file_csv_messages_cron_single_system(self):
        """ test importer view """

        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_11_single_system.csv'
        # change config
        change_csv_import_filename(csv_import_filename)

        """ single system / created """

        # change config
        set_csv_skip_existing_system(True)

        # mock timezone.now()
        t_1 = datetime(2021, 3, 7, 10, 45, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # execute cron job / scheduled task
            system_cron()

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_messages', password='a9aZU5mlnXbVv4TTgcMW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_messages')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 1 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 10:45:00 - 2021-03-07 10:45:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='uNQIBX9woW0M834mJWex')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 1 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 10:45:00 - 2021-03-07 10:45:00]')
        self.assertEqual(messages[0].level_tag, 'success')

# TODO: [debug] does not work as expected

#        """ single system / updated """
#
#        # change config
#        set_csv_skip_existing_system(False)
#
#        # mock timezone.now()
#        t_2 = datetime(2021, 3, 7, 10, 50, tzinfo=timezone.utc)
#        with patch.object(timezone, 'now', return_value=t_2):
#
#            # execute cron job / scheduled task
#            system_cron()
#
#        # login testuser
#        self.client.login(username='testuser_system_importer_file_csv_messages', password='a9aZU5mlnXbVv4TTgcMW')
#        # get response
#        response = self.client.get('/system/')
#        # get messages
#        messages = list(get_messages(response.wsgi_request))
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_messages')
#        self.assertEqual(messages[0].message, 'System CSV importer: created: 0 | updated: 1 | skipped: 0 | multiple: 0 [2021-03-07 10:50:00 - 2021-03-07 10:50:00]')
#        self.assertEqual(messages[0].level_tag, 'success')
#        # switch user context
#        self.client.logout()
#        self.client.login(username='message_user', password='uNQIBX9woW0M834mJWex')
#        # get response
#        response = self.client.get('/system/')
#        # get messages
#        messages = list(get_messages(response.wsgi_request))
#        # compare
#        self.assertEqual(str(response.context['user']), 'message_user')
#        self.assertEqual(messages[0].message, 'System CSV importer: created: 0 | updated: 1 | skipped: 0 | multiple: 0 [2021-03-07 10:50:00 - 2021-03-07 10:50:00]')
#        self.assertEqual(messages[0].level_tag, 'success')

# TODO: [debug] does not work as expected

#        """ single system / skipped """
#
#        # change config
#        set_csv_skip_existing_system(True)
#
#        # mock timezone.now()
#        t_3 = datetime(2021, 3, 7, 10, 55, tzinfo=timezone.utc)
#        with patch.object(timezone, 'now', return_value=t_3):
#
#            # execute cron job / scheduled task
#            system_cron()
#
#        # login testuser
#        self.client.login(username='testuser_system_importer_file_csv_messages', password='a9aZU5mlnXbVv4TTgcMW')
#        # get response
#        response = self.client.get('/system/')
#        # get messages
#        messages = list(get_messages(response.wsgi_request))
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_messages')
#        self.assertEqual(messages[0].message, 'System CSV importer: created: 0 | updated: 0 | skipped: 1 | multiple: 0 [2021-03-07 10:55:00 - 2021-03-07 10:55:00]')
#        self.assertEqual(messages[0].level_tag, 'success')
#        # switch user context
#        self.client.logout()
#        self.client.login(username='message_user', password='uNQIBX9woW0M834mJWex')
#        # get response
#        response = self.client.get('/system/')
#        # get messages
#        messages = list(get_messages(response.wsgi_request))
#        # compare
#        self.assertEqual(str(response.context['user']), 'message_user')
#        self.assertEqual(messages[0].message, 'System CSV importer: created: 0 | updated: 0 | skipped: 1 | multiple: 0 [2021-03-07 10:55:00 - 2021-03-07 10:55:00]')
#        self.assertEqual(messages[0].level_tag, 'success')

    def test_system_importer_file_csv_messages_instant_single_system(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_messages', password='a9aZU5mlnXbVv4TTgcMW')
        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_11_single_system.csv'
        # change config
        change_csv_import_filename(csv_import_filename)

        """ single system / created """

        # change config
        set_csv_skip_existing_system(True)
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(messages[0].message, '1 system was created.')
        self.assertEqual(messages[0].level_tag, 'success')

        """ single system / updated """

        # change config
        set_csv_skip_existing_system(False)
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(messages[0].message, '1 system was updated.')
        self.assertEqual(messages[0].level_tag, 'success')

        """ single system / skipped """

        # change config
        set_csv_skip_existing_system(True)
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(messages[0].message, '1 system was skipped.')
        self.assertEqual(messages[0].level_tag, 'success')

    def test_system_importer_file_csv_messages_upload_post_single_system(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_messages', password='a9aZU5mlnXbVv4TTgcMW')
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_11_single_system.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }

        """ single system / created """

        # change config
        set_csv_skip_existing_system(True)
        # get response
        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(messages[0].message, '1 system was created.')
        self.assertEqual(messages[0].level_tag, 'success')

# TODO: [debug] does not work as expected

#        """ single system / updated """
#
#        # change config
#        set_csv_skip_existing_system(False)
#        # get response
#        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
#        # get messages
#        messages = list(get_messages(response.wsgi_request))
#        # compare
#        self.assertEqual(messages[0].message, '1 system was updated.')
#        self.assertEqual(messages[0].level_tag, 'success')

# TODO: [debug] does not work as expected

#        """ single system / skipped """
#
#        # change config
#        set_csv_skip_existing_system(True)
#        # get response
#        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
#        # get messages
#        messages = list(get_messages(response.wsgi_request))
#        # compare
#        self.assertEqual(messages[0].message, '1 system was skipped.')
#        self.assertEqual(messages[0].level_tag, 'success')

        # close file
        systemcsv.close()
