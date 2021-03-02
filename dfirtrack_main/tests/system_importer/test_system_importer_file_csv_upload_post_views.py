from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.models import Analysisstatus, Case, Company, Domain, Dnsname, Ip, Location, Os, Reason, System, Systemstatus, Systemtype, Tag, Tagcolor
import os
import urllib.parse


class SystemImporterFileCsvUploadPostViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')

        # create objects for post_complete test
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')
#        case_1 = Case.objects.create(
#            case_name='case_1',
#            case_is_incident=True,
#            case_created_by_user_id=test_user,
#        )
#        Case.objects.create(
#            case_name='case_2',
#            case_is_incident=False,
#            case_created_by_user_id=test_user,
#        )
#        Case.objects.create(
#            case_name='case_3',
#            case_is_incident=False,
#            case_created_by_user_id=test_user,
#        )
#        company_1 = Company.objects.create(company_name='company_1')
#        Company.objects.create(company_name='company_2')
#        Company.objects.create(company_name='company_3')
#        Dnsname.objects.create(dnsname_name='dnsname_1')
#        Domain.objects.create(domain_name='domain_1')
#        Os.objects.create(os_name='os_1')
#        Location.objects.create(location_name='location_1')
#        Reason.objects.create(reason_name='reason_1')
#        Systemtype.objects.create(systemtype_name='systemtype_1')
#        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
#        tag_1 = Tag.objects.create(
#            tag_name='tag_1',
#            tagcolor=tagcolor_1,
#        )
#        Tag.objects.create(
#            tag_name='tag_2',
#            tagcolor=tagcolor_1,
#        )
#        Tag.objects.create(
#            tag_name='tag_3',
#            tagcolor=tagcolor_1,
#        )
#        # create objects / mandatory attributes for all tests
#        Systemstatus.objects.create(systemstatus_name='systemstatus_2')
#        # create system objects - post_double test
#        System.objects.create(
#            system_name = 'system_double',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        System.objects.create(
#            system_name = 'system_double',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        # create system objects - post_skip test
#        ip_skip_1 = Ip.objects.create(ip_ip='127.1.1.1')
#        system_skip_1 = System.objects.create(
#            system_name = 'system_skip_1',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_skip_1.ip.add(ip_skip_1)
#        ip_skip_2 = Ip.objects.create(ip_ip='127.3.3.3')
#        system_skip_2 = System.objects.create(
#            system_name = 'system_skip_2',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_skip_2.ip.add(ip_skip_2)
#        # create system objects - post_update_discard_manytomany test
#        ip_update_discard_manytomany_1 = Ip.objects.create(ip_ip='10.1.1.1')
#        ip_update_discard_manytomany_2 = Ip.objects.create(ip_ip='10.2.2.2')
#        system_update_discard_manytomany_1 = System.objects.create(
#            system_name = 'system_update_discard_manytomany_1',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_update_discard_manytomany_2 = System.objects.create(
#            system_name = 'system_update_discard_manytomany_2',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_update_discard_manytomany_1.case.add(case_1)
#        system_update_discard_manytomany_1.company.add(company_1)
#        system_update_discard_manytomany_1.ip.add(ip_update_discard_manytomany_1)
#        system_update_discard_manytomany_1.tag.add(tag_1)
#        system_update_discard_manytomany_2.ip.add(ip_update_discard_manytomany_2)
#        # create system objects - post_update_keep_manytomany test
#        ip_update_keep_manytomany_1 = Ip.objects.create(ip_ip='10.5.5.5')
#        ip_update_keep_manytomany_2 = Ip.objects.create(ip_ip='10.6.6.6')
#        system_update_keep_manytomany_1 = System.objects.create(
#            system_name = 'system_update_keep_manytomany_1',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_update_keep_manytomany_2 = System.objects.create(
#            system_name = 'system_update_keep_manytomany_2',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_update_keep_manytomany_1.case.add(case_1)
#        system_update_keep_manytomany_1.company.add(company_1)
#        system_update_keep_manytomany_1.ip.add(ip_update_keep_manytomany_1)
#        system_update_keep_manytomany_1.tag.add(tag_1)
#        system_update_keep_manytomany_2.ip.add(ip_update_keep_manytomany_2)
#        # create system objects - post_update_single test
#        ip_update_single_1 = Ip.objects.create(ip_ip='127.2.3.41')
#        system_update_single_1 = System.objects.create(
#            system_name = 'system_update_single_1',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_update_single_1.ip.add(ip_update_single_1)
#        # create system objects - post_skip_single test
#        ip_skip_single_1 = Ip.objects.create(ip_ip='127.3.4.51')
#        system_skip_single_1 = System.objects.create(
#            system_name = 'system_skip_single_1',
#            systemstatus = systemstatus_1,
#            system_modify_time = timezone.now(),
#            system_created_by_user_id = test_user,
#            system_modified_by_user_id = test_user,
#        )
#        system_skip_single_1.ip.add(ip_skip_single_1)

    @classmethod
    def setUp(cls):

        # get user
        test_user = User.objects.get(username='testuser_system_importer_file_csv_upload_post')

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

    # TODO: [code] add tests for config checks 'check_config_attributes' called in 'csv.system_upload' GET method
        # redirect to system_list

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_bad_config(self):
#        """ test importer view """
#
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
#        self.assertEqual(str(messages[1]), '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
#        self.assertEqual(str(messages[2]), 'Nothing was changed.')

    def test_system_importer_file_csv_upload_post_no_file_submitted(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv.html')

    # TODO: [rebuild] not 'upload' specific

    def test_system_importer_file_csv_upload_post_minimal_double_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
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

    # TODO: [rebuild] not 'upload' specific

    def test_system_importer_file_csv_upload_post_minimal_single_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_text_quote = 'text_single_quotation_marks'
        system_importer_file_csv_config_model.save()
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
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

    # TODO: [rebuild] not 'upload' specific

    def test_system_importer_file_csv_upload_post_minimal_headline(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_headline = True
        system_importer_file_csv_config_model.save()
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
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

    # TODO: [rebuild] not 'upload' specific

    def test_system_importer_file_csv_upload_post_wrong_type(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')
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

    # TODO: [rebuild] not 'upload' specific

    def test_system_importer_file_csv_upload_post_corrupted(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_upload_post', password='8BhDTbU9qMSQ4NGhkfyc')
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

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_double(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_double.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(len(System.objects.filter(system_name='system_double')), 2)
#        self.assertEqual(str(messages[0]), 'System system_double already exists multiple times. Nothing was changed for this system.')
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_wrong(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_wrong.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), 'Value for system in row 1 was an empty string. System not created.')
#        self.assertEqual(str(messages[1]), 'Value for system in row 2 was too long. System not created.')
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_skip(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_skip.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '2 systems were skipped.')
#        self.assertEqual(system_skip_1.analysisstatus, None)
#        self.assertEqual(system_skip_1.systemstatus, systemstatus_1)
#        self.assertTrue(system_skip_1.ip.filter(ip_ip='127.1.1.1').exists())
#        self.assertFalse(system_skip_1.ip.filter(ip_ip='127.2.2.2').exists())
#        self.assertEqual(system_skip_2.analysisstatus, None)
#        self.assertEqual(system_skip_2.systemstatus, systemstatus_1)
#        self.assertTrue(system_skip_2.ip.filter(ip_ip='127.3.3.3').exists())
#        self.assertFalse(system_skip_2.ip.filter(ip_ip='127.4.4.4').exists())

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_update_discard_manytomany(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_discard_manytomany.csv'), 'r')
#        # compare - general
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '2 systems were updated.')
#        # compare - system_update_discard_manytomany_1
#        self.assertFalse(system_update_discard_manytomany_1.case.filter(case_name='case_1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.case.filter(case_name='case_2').exists())
#        self.assertFalse(system_update_discard_manytomany_1.company.filter(company_name='company_1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.company.filter(company_name='company_2').exists())
#        self.assertFalse(system_update_discard_manytomany_1.ip.filter(ip_ip='10.1.1.1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.ip.filter(ip_ip='10.3.3.3').exists())
#        self.assertEqual(system_update_discard_manytomany_1.systemstatus, systemstatus_2)
#        self.assertFalse(system_update_discard_manytomany_1.tag.filter(tag_name='tag_1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.tag.filter(tag_name='tag_2').exists())
#        # compare - system_update_discard_manytomany_2
#        self.assertTrue(system_update_discard_manytomany_2.case.filter(case_name='case_2').exists())
#        self.assertTrue(system_update_discard_manytomany_2.company.filter(company_name='company_2').exists())
#        self.assertFalse(system_update_discard_manytomany_2.ip.filter(ip_ip='10.2.2.2').exists())
#        self.assertTrue(system_update_discard_manytomany_2.ip.filter(ip_ip='10.4.4.4').exists())
#        self.assertEqual(system_update_discard_manytomany_2.systemstatus, systemstatus_2)
#        self.assertTrue(system_update_discard_manytomany_2.tag.filter(tag_name='tag_2').exists())
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_update_keep_manytomany(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_keep_manytomany.csv'), 'r')
#        # compare - general
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '2 systems were updated.')
#        # compare - system_update_keep_manytomany_1
#        self.assertTrue(system_update_keep_manytomany_1.case.filter(case_name='case_1').exists())
#        self.assertTrue(system_update_keep_manytomany_1.case.filter(case_name='case_2').exists())
#        self.assertTrue(system_update_keep_manytomany_1.company.filter(company_name='company_1').exists())
#        self.assertTrue(system_update_keep_manytomany_1.company.filter(company_name='company_2').exists())
#        self.assertTrue(system_update_keep_manytomany_1.ip.filter(ip_ip='10.5.5.5').exists())
#        self.assertTrue(system_update_keep_manytomany_1.ip.filter(ip_ip='10.7.7.7').exists())
#        self.assertEqual(system_update_keep_manytomany_1.systemstatus, systemstatus_2)
#        self.assertTrue(system_update_keep_manytomany_1.tag.filter(tag_name='tag_1').exists())
#        self.assertTrue(system_update_keep_manytomany_1.tag.filter(tag_name='tag_2').exists())
#        # compare - system_update_keep_manytomany_2
#        self.assertTrue(system_update_keep_manytomany_2.case.filter(case_name='case_2').exists())
#        self.assertTrue(system_update_keep_manytomany_2.company.filter(company_name='company_2').exists())
#        self.assertTrue(system_update_keep_manytomany_2.ip.filter(ip_ip='10.6.6.6').exists())
#        self.assertTrue(system_update_keep_manytomany_2.ip.filter(ip_ip='10.8.8.8').exists())
#        self.assertEqual(system_update_keep_manytomany_2.systemstatus, systemstatus_2)
#        self.assertTrue(system_update_keep_manytomany_2.tag.filter(tag_name='tag_2').exists())

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_create_single(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_create_single.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '1 system was created.')
#        self.assertTrue(System.objects.filter(system_name='system_create_single_1').exists())
#        self.assertFalse(system_1.ip.filter(ip_ip='127.1.2.31').exists())
#        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_1.systemstatus, systemstatus_1)
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_update_single(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_single.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '1 system was updated.')
#        self.assertTrue(System.objects.filter(system_name='system_update_single_1').exists())
#        self.assertTrue(system_1.ip.filter(ip_ip='127.2.3.41').exists())
#        self.assertTrue(system_1.ip.filter(ip_ip='127.2.3.42').exists())
#        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_1.systemstatus, systemstatus_2)
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_skip_single(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_skip_single.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '1 system was skipped.')
#        self.assertTrue(System.objects.filter(system_name='system_skip_single_1').exists())
#        self.assertTrue(system_1.ip.filter(ip_ip='127.3.4.51').exists())
#        self.assertFalse(system_1.ip.filter(ip_ip='127.3.4.52').exists())
#        self.assertEqual(system_1.analysisstatus, None)
#        self.assertEqual(system_1.systemstatus, systemstatus_1)
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_invalid_ip(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_invalid_ip.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), 'Value for ip address in row 1 was not a valid IP address.')
#        self.assertEqual(str(messages[1]), '1 system was created.')
#        self.assertTrue(System.objects.filter(system_name='system_invalid_ip_1').exists())
#        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_1.systemstatus, systemstatus_1)
