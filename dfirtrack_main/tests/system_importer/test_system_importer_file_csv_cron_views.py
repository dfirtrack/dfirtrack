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


class SystemImporterFileCsvCronViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):
        """ one-time setup """

        # create user
        User.objects.create_user(username='testuser_system_importer_file_csv_cron', password='bt2z3OlVFcjmqt2ItuEt')
        User.objects.create_user(username='message_user', password='DsaygmEY9owS4KEA55Gt')

        # create objects
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_2')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_2')

    @classmethod
    def setUp(cls):
        """ setup in advance of every test """

        # get user
        test_user = User.objects.get(username='testuser_system_importer_file_csv_cron')

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        analysisstatus_2 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_2')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')

        # build local path with test files
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/')
        set_csv_import_path(csv_import_path)

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

        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_01_minimal_double_quotation.csv'
        # change config
        set_csv_import_filename(csv_import_filename)

        # mock timezone.now()
        t_1 = datetime(2021, 3, 6, 17, 28, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # execute cron job / scheduled task
            system_cron()

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # compare
        self.assertTrue(System.objects.filter(system_name='system_csv_01_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_01_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_01_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_01_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_003').systemstatus, systemstatus_1)
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_cron', password='bt2z3OlVFcjmqt2ItuEt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_cron')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:28:00 - 2021-03-06 17:28:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='DsaygmEY9owS4KEA55Gt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:28:00 - 2021-03-06 17:28:00]')
        self.assertEqual(messages[0].level_tag, 'success')

    def test_system_importer_file_csv_cron_minimal_single_quotation(self):
        """ test importer view """

        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_02_minimal_single_quotation.csv'
        # change config
        set_csv_import_filename(csv_import_filename)
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_text_quote = 'text_single_quotation_marks'
        system_importer_file_csv_config_model.save()

        # mock timezone.now()
        t_2 = datetime(2021, 3, 6, 17, 55, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_2):

            # execute cron job / scheduled task
            system_cron()

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # compare
        self.assertTrue(System.objects.filter(system_name='system_csv_02_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_02_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_02_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_02_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_003').systemstatus, systemstatus_1)
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_cron', password='bt2z3OlVFcjmqt2ItuEt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_cron')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:55:00 - 2021-03-06 17:55:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='DsaygmEY9owS4KEA55Gt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 17:55:00 - 2021-03-06 17:55:00]')
        self.assertEqual(messages[0].level_tag, 'success')

    def test_system_importer_file_csv_cron_minimal_headline(self):
        """ test importer view """

        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_03_minimal_headline.csv'
        # change config
        set_csv_import_filename(csv_import_filename)
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_headline = True
        system_importer_file_csv_config_model.save()

        # mock timezone.now()
        t_3 = datetime(2021, 3, 6, 18, 7, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_3):

            # execute cron job / scheduled task
            system_cron()

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # compare
        self.assertTrue(System.objects.filter(system_name='system_csv_03_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_03_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_03_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_03_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_003').systemstatus, systemstatus_1)
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_cron', password='bt2z3OlVFcjmqt2ItuEt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_cron')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 18:07:00 - 2021-03-06 18:07:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='DsaygmEY9owS4KEA55Gt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-06 18:07:00 - 2021-03-06 18:07:00]')
        self.assertEqual(messages[0].level_tag, 'success')

    def test_system_importer_file_csv_cron_minimal_comma(self):
        """ test importer view """

        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_21_minimal_comma.csv'
        # change config
        set_csv_import_filename(csv_import_filename)
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

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # compare
        self.assertTrue(System.objects.filter(system_name='system_csv_21_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_21_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_21_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_21_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_003').systemstatus, systemstatus_1)
        # compare domain (delimiter specific)
        self.assertTrue(Domain.objects.filter(domain_name='domain_21_1').exists())
        domain_1 = Domain.objects.get(domain_name='domain_21_1')
        self.assertEqual(System.objects.get(system_name='system_csv_21_001').domain, domain_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_002').domain, domain_1)
        self.assertEqual(System.objects.get(system_name='system_csv_21_003').domain, domain_1)
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_cron', password='bt2z3OlVFcjmqt2ItuEt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_cron')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:12:00 - 2021-03-07 21:12:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='DsaygmEY9owS4KEA55Gt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:12:00 - 2021-03-07 21:12:00]')
        self.assertEqual(messages[0].level_tag, 'success')

    def test_system_importer_file_csv_cron_minimal_semicolon(self):
        """ test importer view """

        # set file system attributes
        csv_import_filename = 'system_importer_file_csv_testfile_22_minimal_semicolon.csv'
        # change config
        set_csv_import_filename(csv_import_filename)
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

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # compare
        self.assertTrue(System.objects.filter(system_name='system_csv_22_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_22_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_22_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_22_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_003').systemstatus, systemstatus_1)
        # compare domain (delimiter specific)
        self.assertTrue(Domain.objects.filter(domain_name='domain_22_1').exists())
        domain_1 = Domain.objects.get(domain_name='domain_22_1')
        self.assertEqual(System.objects.get(system_name='system_csv_22_001').domain, domain_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_002').domain, domain_1)
        self.assertEqual(System.objects.get(system_name='system_csv_22_003').domain, domain_1)
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_cron', password='bt2z3OlVFcjmqt2ItuEt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_cron')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:17:00 - 2021-03-07 21:17:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='DsaygmEY9owS4KEA55Gt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 0 | multiple: 0 [2021-03-07 21:17:00 - 2021-03-07 21:17:00]')
        self.assertEqual(messages[0].level_tag, 'success')
