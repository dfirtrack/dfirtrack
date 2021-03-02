from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.models import Analysisstatus, Systemstatus
import urllib.parse


class SystemImporterFileCsvUploadGetViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_system_importer_file_csv_upload_get', password='39gE1C0nA1hmlcoxZjAd')

        # create objects
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')

    @classmethod
    def setUp(cls):

        # get user
        test_user = User.objects.get(username='testuser_system_importer_file_csv_upload_get')

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')

        # set default values
        csv_import_path = '/tmp'
        csv_import_filename = 'system.csv'

        # restore config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_column_system = 1
        system_importer_file_csv_config_model.csv_skip_existing_system = True
        system_importer_file_csv_config_model.csv_headline = False
        system_importer_file_csv_config_model.csv_import_path = csv_import_path
        system_importer_file_csv_config_model.csv_import_filename = csv_import_filename
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

    def test_system_importer_file_csv_upload_get_not_logged_in(self):
        """ test importer view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/importer/file/csv/upload/', safe='')
        # get response
        response = self.client.get('/system/importer/file/csv/upload/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_upload_get_logged_in(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_get', password='39gE1C0nA1hmlcoxZjAd')
        # get response
        response = self.client.get('/system/importer/file/csv/upload/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_upload_get_template(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_get', password='39gE1C0nA1hmlcoxZjAd')
        # get response
        response = self.client.get('/system/importer/file/csv/upload/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv.html')

    def test_system_importer_file_csv_upload_get_get_user_context(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_get', password='39gE1C0nA1hmlcoxZjAd')
        # get response
        response = self.client.get('/system/importer/file/csv/upload/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_upload_get')

    def test_system_importer_file_csv_upload_get_redirect(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_get', password='39gE1C0nA1hmlcoxZjAd')
        # create url
        destination = urllib.parse.quote('/system/importer/file/csv/upload/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/upload', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_importer_file_csv_upload_get_skip_warning(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_get', password='39gE1C0nA1hmlcoxZjAd')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_skip_existing_system = False
        system_importer_file_csv_config_model.save()
        # get response
        response = self.client.get('/system/importer/file/csv/upload/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertEqual(messages[0].message, 'WARNING: Existing systems will be updated!')
        self.assertEqual(messages[0].level_tag, 'warning')

    # TODO: [code] add tests for config checks 'check_config_attributes' called in 'csv.system_upload' GET method
        # redirect to system_list
        # all messages --> generic tests for all functions ('system_cron', 'system_create_cron', 'system_upload', 'system_instant')

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_get_bad_config(self):
#        """ test importer view """
#
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
#        self.assertEqual(str(messages[1]), '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
#        self.assertEqual(str(messages[2]), 'Nothing was changed.')
