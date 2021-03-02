from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.models import Analysisstatus, Systemstatus
import os
import urllib.parse


def set_column_fields_numeric_values():

    # get config
    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')

    # set numeric values for column fields out of range
    system_importer_file_csv_config_model.csv_column_system = 100
    system_importer_file_csv_config_model.csv_column_ip = 101
    system_importer_file_csv_config_model.csv_column_dnsname = 102
    system_importer_file_csv_config_model.csv_column_domain = 103
    system_importer_file_csv_config_model.csv_column_location = 104
    system_importer_file_csv_config_model.csv_column_os = 105
    system_importer_file_csv_config_model.csv_column_reason = 106
    system_importer_file_csv_config_model.csv_column_recommendation = 107
    system_importer_file_csv_config_model.csv_column_serviceprovider = 108
    system_importer_file_csv_config_model.csv_column_systemtype = 109
    system_importer_file_csv_config_model.csv_column_case = 110
    system_importer_file_csv_config_model.csv_column_company = 111
    system_importer_file_csv_config_model.csv_column_tag = 112

    # save config
    system_importer_file_csv_config_model.save()

    # return to column fields numeric values test function
    return

class SystemImporterFileCsvCheckConfigAttributesViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_check_config_attributes', password='VgnTh4qkYZH61F5YArC7')

        # create objects for post_complete test
        analysisstatus_1 = Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # build local path with test files
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/')
        csv_import_filename = 'system_importer_file_csv_testfile_01_minimal_double_quotation.csv'

        # set mandatory config values
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

        # save config
        system_importer_file_csv_config_model.save()

    def test_system_importer_file_csv_check_config_attributes_create_cron_column_fields_numeric_values(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_config_attributes', password='VgnTh4qkYZH61F5YArC7')
        # change config
        set_column_fields_numeric_values()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/cron/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')
        self.assertEqual(messages[1].message, '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
        self.assertEqual(messages[1].level_tag, 'error')
        self.assertEqual(messages[2].message, '`CSV_COLUMN_DNSNAME` is outside the allowed range. Check config!')
        self.assertEqual(messages[2].level_tag, 'error')
        self.assertEqual(messages[3].message, '`CSV_COLUMN_DOMAIN` is outside the allowed range. Check config!')
        self.assertEqual(messages[3].level_tag, 'error')
        self.assertEqual(messages[4].message, '`CSV_COLUMN_LOCATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[4].level_tag, 'error')
        self.assertEqual(messages[5].message, '`CSV_COLUMN_OS` is outside the allowed range. Check config!')
        self.assertEqual(messages[5].level_tag, 'error')
        self.assertEqual(messages[6].message, '`CSV_COLUMN_REASON` is outside the allowed range. Check config!')
        self.assertEqual(messages[6].level_tag, 'error')
        self.assertEqual(messages[7].message, '`CSV_COLUMN_RECOMMENDATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[7].level_tag, 'error')
        self.assertEqual(messages[8].message, '`CSV_COLUMN_SERVICEPROVIDER` is outside the allowed range. Check config!')
        self.assertEqual(messages[8].level_tag, 'error')
        self.assertEqual(messages[9].message, '`CSV_COLUMN_SYSTEMTYPE` is outside the allowed range. Check config!')
        self.assertEqual(messages[9].level_tag, 'error')
        self.assertEqual(messages[10].message, '`CSV_COLUMN_CASE` is outside the allowed range. Check config!')
        self.assertEqual(messages[10].level_tag, 'error')
        self.assertEqual(messages[11].message, '`CSV_COLUMN_COMPANY` is outside the allowed range. Check config!')
        self.assertEqual(messages[11].level_tag, 'error')
        self.assertEqual(messages[12].message, '`CSV_COLUMN_TAG` is outside the allowed range. Check config!')
        self.assertEqual(messages[12].level_tag, 'error')

    # TODO: [code] add test for cron view (without GET request)

    def test_system_importer_file_csv_check_config_attributes_instant_column_fields_numeric_values(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_config_attributes', password='VgnTh4qkYZH61F5YArC7')
        # change config
        set_column_fields_numeric_values()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/instant/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')
        self.assertEqual(messages[1].message, '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
        self.assertEqual(messages[1].level_tag, 'error')
        self.assertEqual(messages[2].message, '`CSV_COLUMN_DNSNAME` is outside the allowed range. Check config!')
        self.assertEqual(messages[2].level_tag, 'error')
        self.assertEqual(messages[3].message, '`CSV_COLUMN_DOMAIN` is outside the allowed range. Check config!')
        self.assertEqual(messages[3].level_tag, 'error')
        self.assertEqual(messages[4].message, '`CSV_COLUMN_LOCATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[4].level_tag, 'error')
        self.assertEqual(messages[5].message, '`CSV_COLUMN_OS` is outside the allowed range. Check config!')
        self.assertEqual(messages[5].level_tag, 'error')
        self.assertEqual(messages[6].message, '`CSV_COLUMN_REASON` is outside the allowed range. Check config!')
        self.assertEqual(messages[6].level_tag, 'error')
        self.assertEqual(messages[7].message, '`CSV_COLUMN_RECOMMENDATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[7].level_tag, 'error')
        self.assertEqual(messages[8].message, '`CSV_COLUMN_SERVICEPROVIDER` is outside the allowed range. Check config!')
        self.assertEqual(messages[8].level_tag, 'error')
        self.assertEqual(messages[9].message, '`CSV_COLUMN_SYSTEMTYPE` is outside the allowed range. Check config!')
        self.assertEqual(messages[9].level_tag, 'error')
        self.assertEqual(messages[10].message, '`CSV_COLUMN_CASE` is outside the allowed range. Check config!')
        self.assertEqual(messages[10].level_tag, 'error')
        self.assertEqual(messages[11].message, '`CSV_COLUMN_COMPANY` is outside the allowed range. Check config!')
        self.assertEqual(messages[11].level_tag, 'error')
        self.assertEqual(messages[12].message, '`CSV_COLUMN_TAG` is outside the allowed range. Check config!')
        self.assertEqual(messages[12].level_tag, 'error')

    def test_system_importer_file_csv_check_config_attributes_upload_get_column_fields_numeric_values(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_config_attributes', password='VgnTh4qkYZH61F5YArC7')
        # change config
        set_column_fields_numeric_values()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/upload/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')
        self.assertEqual(messages[1].message, '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
        self.assertEqual(messages[1].level_tag, 'error')
        self.assertEqual(messages[2].message, '`CSV_COLUMN_DNSNAME` is outside the allowed range. Check config!')
        self.assertEqual(messages[2].level_tag, 'error')
        self.assertEqual(messages[3].message, '`CSV_COLUMN_DOMAIN` is outside the allowed range. Check config!')
        self.assertEqual(messages[3].level_tag, 'error')
        self.assertEqual(messages[4].message, '`CSV_COLUMN_LOCATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[4].level_tag, 'error')
        self.assertEqual(messages[5].message, '`CSV_COLUMN_OS` is outside the allowed range. Check config!')
        self.assertEqual(messages[5].level_tag, 'error')
        self.assertEqual(messages[6].message, '`CSV_COLUMN_REASON` is outside the allowed range. Check config!')
        self.assertEqual(messages[6].level_tag, 'error')
        self.assertEqual(messages[7].message, '`CSV_COLUMN_RECOMMENDATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[7].level_tag, 'error')
        self.assertEqual(messages[8].message, '`CSV_COLUMN_SERVICEPROVIDER` is outside the allowed range. Check config!')
        self.assertEqual(messages[8].level_tag, 'error')
        self.assertEqual(messages[9].message, '`CSV_COLUMN_SYSTEMTYPE` is outside the allowed range. Check config!')
        self.assertEqual(messages[9].level_tag, 'error')
        self.assertEqual(messages[10].message, '`CSV_COLUMN_CASE` is outside the allowed range. Check config!')
        self.assertEqual(messages[10].level_tag, 'error')
        self.assertEqual(messages[11].message, '`CSV_COLUMN_COMPANY` is outside the allowed range. Check config!')
        self.assertEqual(messages[11].level_tag, 'error')
        self.assertEqual(messages[12].message, '`CSV_COLUMN_TAG` is outside the allowed range. Check config!')
        self.assertEqual(messages[12].level_tag, 'error')

    def test_system_importer_file_csv_check_config_attributes_upload_post_column_fields_numeric_values(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_config_attributes', password='VgnTh4qkYZH61F5YArC7')
        # change config
        set_column_fields_numeric_values()
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
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')
        self.assertEqual(messages[1].message, '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
        self.assertEqual(messages[1].level_tag, 'error')
        self.assertEqual(messages[2].message, '`CSV_COLUMN_DNSNAME` is outside the allowed range. Check config!')
        self.assertEqual(messages[2].level_tag, 'error')
        self.assertEqual(messages[3].message, '`CSV_COLUMN_DOMAIN` is outside the allowed range. Check config!')
        self.assertEqual(messages[3].level_tag, 'error')
        self.assertEqual(messages[4].message, '`CSV_COLUMN_LOCATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[4].level_tag, 'error')
        self.assertEqual(messages[5].message, '`CSV_COLUMN_OS` is outside the allowed range. Check config!')
        self.assertEqual(messages[5].level_tag, 'error')
        self.assertEqual(messages[6].message, '`CSV_COLUMN_REASON` is outside the allowed range. Check config!')
        self.assertEqual(messages[6].level_tag, 'error')
        self.assertEqual(messages[7].message, '`CSV_COLUMN_RECOMMENDATION` is outside the allowed range. Check config!')
        self.assertEqual(messages[7].level_tag, 'error')
        self.assertEqual(messages[8].message, '`CSV_COLUMN_SERVICEPROVIDER` is outside the allowed range. Check config!')
        self.assertEqual(messages[8].level_tag, 'error')
        self.assertEqual(messages[9].message, '`CSV_COLUMN_SYSTEMTYPE` is outside the allowed range. Check config!')
        self.assertEqual(messages[9].level_tag, 'error')
        self.assertEqual(messages[10].message, '`CSV_COLUMN_CASE` is outside the allowed range. Check config!')
        self.assertEqual(messages[10].level_tag, 'error')
        self.assertEqual(messages[11].message, '`CSV_COLUMN_COMPANY` is outside the allowed range. Check config!')
        self.assertEqual(messages[11].level_tag, 'error')
        self.assertEqual(messages[12].message, '`CSV_COLUMN_TAG` is outside the allowed range. Check config!')
        self.assertEqual(messages[12].level_tag, 'error')
