from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.models import Analysisstatus, Ip, System, Systemstatus, Tag
import os
import urllib.parse


class SystemImporterFileCsvInstantViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')

        # create objects
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')

    @classmethod
    def setUp(cls):

        # get user
        test_user = User.objects.get(username='testuser_system_importer_file_csv_instant')

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')

        # build local path with test files
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/')

        # restore config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_column_system = 1
        system_importer_file_csv_config_model.csv_skip_existing_system = True
        system_importer_file_csv_config_model.csv_headline = False
        system_importer_file_csv_config_model.csv_import_path = csv_import_path
        system_importer_file_csv_config_model.csv_import_username = test_user
        system_importer_file_csv_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_config_model.csv_default_tagfree_systemstatus = systemstatus_1
        system_importer_file_csv_config_model.csv_default_tagfree_analysisstatus = analysisstatus_1
        system_importer_file_csv_config_model.csv_tag_lock_systemstatus = 'LOCK_SYSTEMSTATUS'
        system_importer_file_csv_config_model.csv_tag_lock_analysisstatus = 'LOCK_ANALYSISSTATUS'
        system_importer_file_csv_config_model.csv_remove_tag = 'tag_remove_prefix'
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_text_quote = 'text_double_quotation_marks'
        system_importer_file_csv_config_model.csv_ip_delimiter = 'ip_semicolon'
        system_importer_file_csv_config_model.csv_tag_delimiter = 'tag_space'
        system_importer_file_csv_config_model.save()

    def test_system_importer_file_csv_instant_minimal_double_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_import_filename = 'system_importer_file_csv_testfile_01_minimal_double_quotation.csv'
        system_importer_file_csv_config_model.save()
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '3 systems were created.')
        self.assertEqual(messages[0].level_tag, 'success')
        self.assertTrue(System.objects.filter(system_name='system_csv_01_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_01_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_01_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_01_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_01_003').systemstatus, systemstatus_1)

    def test_system_importer_file_csv_instant_minimal_single_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_import_filename = 'system_importer_file_csv_testfile_02_minimal_single_quotation.csv'
        system_importer_file_csv_config_model.csv_text_quote = 'text_single_quotation_marks'
        system_importer_file_csv_config_model.save()
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '3 systems were created.')
        self.assertEqual(messages[0].level_tag, 'success')
        self.assertTrue(System.objects.filter(system_name='system_csv_02_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_02_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_02_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_02_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_02_003').systemstatus, systemstatus_1)

    def test_system_importer_file_csv_instant_minimal_headline(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_import_filename = 'system_importer_file_csv_testfile_03_minimal_headline.csv'
        system_importer_file_csv_config_model.csv_headline = True
        system_importer_file_csv_config_model.save()
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '3 systems were created.')
        self.assertEqual(messages[0].level_tag, 'success')
        self.assertTrue(System.objects.filter(system_name='system_csv_03_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_03_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_03_003').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_03_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_03_003').systemstatus, systemstatus_1)

    def test_system_importer_file_csv_instant_complete(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_import_filename = 'system_importer_file_csv_testfile_07_complete.csv'

        system_importer_file_csv_config_model.csv_choice_ip = True
        system_importer_file_csv_config_model.csv_column_ip = 2
        system_importer_file_csv_config_model.csv_choice_tag = True
        system_importer_file_csv_config_model.csv_column_tag = 3

        system_importer_file_csv_config_model.save()
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - generic stuff
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '3 systems were created.')
        self.assertEqual(messages[0].level_tag, 'success')
        # compare - existence of objects
        self.assertTrue(Ip.objects.filter(ip_ip='127.1.0.1').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='127.1.0.2').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='127.1.0.3').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='10.2.0.1').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='10.2.0.2').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='10.2.0.3').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_07_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_07_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_07_003').exists())
        self.assertTrue(Tag.objects.filter(tag_name='tag_1').exists())
        self.assertTrue(Tag.objects.filter(tag_name='tag_2').exists())
        self.assertTrue(Tag.objects.filter(tag_name='tag_3').exists())
        self.assertTrue(Tag.objects.filter(tag_name='tag_4').exists())
        # compare - relations
        self.assertEqual(System.objects.get(system_name='system_csv_07_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_07_002').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_07_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_07_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_07_002').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_07_003').systemstatus, systemstatus_1)
