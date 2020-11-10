from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigbasedConfigModel
from dfirtrack_main.models import Analysisstatus, Case, Company, Domain, Dnsname, Ip, Location, Os, Reason, System, Systemstatus, Systemtype, Tag, Tagcolor
import os
import urllib.parse


class SystemImporterFileCsvConfigbasedViewTestCase(TestCase):
    """ system importer file CSV config-based view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')

        # create objects for post_complete test
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_2')
        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )
        Case.objects.create(
            case_name='case_2',
            case_is_incident=False,
            case_created_by_user_id=test_user,
        )
        Case.objects.create(
            case_name='case_3',
            case_is_incident=False,
            case_created_by_user_id=test_user,
        )
        company_1 = Company.objects.create(company_name='company_1')
        Company.objects.create(company_name='company_2')
        Company.objects.create(company_name='company_3')
        Dnsname.objects.create(dnsname_name='dnsname_1')
        Domain.objects.create(domain_name='domain_1')
        Os.objects.create(os_name='os_1')
        Location.objects.create(location_name='location_1')
        Reason.objects.create(reason_name='reason_1')
        Systemtype.objects.create(systemtype_name='systemtype_1')
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        tag_1 = Tag.objects.create(
            tag_name='tag_1',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_2',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_3',
            tagcolor=tagcolor_1,
        )
        # create objects / mandatory attributes for all tests
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_2')
        # create system objects - post_double test
        System.objects.create(
            system_name = 'system_double',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        System.objects.create(
            system_name = 'system_double',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # create system objects - post_skip test
        ip_skip_1 = Ip.objects.create(ip_ip='127.1.1.1')
        system_skip_1 = System.objects.create(
            system_name = 'system_skip_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_skip_1.ip.add(ip_skip_1)
        ip_skip_2 = Ip.objects.create(ip_ip='127.3.3.3')
        system_skip_2 = System.objects.create(
            system_name = 'system_skip_2',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_skip_2.ip.add(ip_skip_2)
        # create system objects - post_update_discard_manytomany test
        ip_update_discard_manytomany_1 = Ip.objects.create(ip_ip='10.1.1.1')
        ip_update_discard_manytomany_2 = Ip.objects.create(ip_ip='10.2.2.2')
        system_update_discard_manytomany_1 = System.objects.create(
            system_name = 'system_update_discard_manytomany_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_update_discard_manytomany_2 = System.objects.create(
            system_name = 'system_update_discard_manytomany_2',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_update_discard_manytomany_1.case.add(case_1)
        system_update_discard_manytomany_1.company.add(company_1)
        system_update_discard_manytomany_1.ip.add(ip_update_discard_manytomany_1)
        system_update_discard_manytomany_1.tag.add(tag_1)
        system_update_discard_manytomany_2.ip.add(ip_update_discard_manytomany_2)
        # create system objects - post_update_keep_manytomany test
        ip_update_keep_manytomany_1 = Ip.objects.create(ip_ip='10.5.5.5')
        ip_update_keep_manytomany_2 = Ip.objects.create(ip_ip='10.6.6.6')
        system_update_keep_manytomany_1 = System.objects.create(
            system_name = 'system_update_keep_manytomany_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_update_keep_manytomany_2 = System.objects.create(
            system_name = 'system_update_keep_manytomany_2',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_update_keep_manytomany_1.case.add(case_1)
        system_update_keep_manytomany_1.company.add(company_1)
        system_update_keep_manytomany_1.ip.add(ip_update_keep_manytomany_1)
        system_update_keep_manytomany_1.tag.add(tag_1)
        system_update_keep_manytomany_2.ip.add(ip_update_keep_manytomany_2)
        # create system objects - post_update_single test
        ip_update_single_1 = Ip.objects.create(ip_ip='127.2.3.41')
        system_update_single_1 = System.objects.create(
            system_name = 'system_update_single_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_update_single_1.ip.add(ip_update_single_1)
        # create system objects - post_skip_single test
        ip_skip_single_1 = Ip.objects.create(ip_ip='127.3.4.51')
        system_skip_single_1 = System.objects.create(
            system_name = 'system_skip_single_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_skip_single_1.ip.add(ip_skip_single_1)

    def test_system_importer_file_csv_config_based_not_logged_in(self):
        """ test importer view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/importer/file/csv/configbased/', safe='')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_importer_file_csv_config_based_logged_in(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_importer_file_csv_config_based_template(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv_config_based.html')

    def test_system_importer_file_csv_config_based_get_user_context(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_config_based')

    def test_system_importer_file_csv_config_based_redirect(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # create url
        destination = urllib.parse.quote('/system/importer/file/csv/configbased/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_importer_file_csv_config_based_skip_warning(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = False
        system_importer_file_csv_configbased_config_model.csv_column_system = 256
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 1
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(messages[0]), 'WARNING: Existing systems will be updated!')

    def test_system_importer_file_csv_config_based_bad_config(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 0
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 257
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/importer/file/csv/configbased/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '`CSV_COLUMN_SYSTEM` is outside the allowed range. Check config!')
        self.assertEqual(str(messages[1]), '`CSV_COLUMN_IP` is outside the allowed range. Check config!')
        self.assertEqual(str(messages[2]), 'Nothing was changed.')

    def test_system_importer_file_csv_config_based_post_minimal(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 3
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 4
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_minimal.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_1 = System.objects.get(system_name='systems_csv_minimal_001')
        system_2 = System.objects.get(system_name='systems_csv_minimal_002')
        system_3 = System.objects.get(system_name='systems_csv_minimal_003')
        system_4 = System.objects.get(system_name='systems_csv_minimal_004')
        system_5 = System.objects.get(system_name='systems_csv_minimal_005')
        system_6 = System.objects.get(system_name='systems_csv_minimal_006')
        system_7 = System.objects.get(system_name='systems_csv_minimal_007')
        system_8 = System.objects.get(system_name='systems_csv_minimal_008')
        system_9 = System.objects.get(system_name='systems_csv_minimal_009')
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '9 systems were created.')
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_001').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_002').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_003').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_004').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_005').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_006').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_007').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_008').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_minimal_009').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.0.0.10').exists())
        self.assertTrue(system_2.ip.filter(ip_ip='127.0.0.20').exists())
        self.assertTrue(system_3.ip.filter(ip_ip='127.0.0.30').exists())
        self.assertTrue(system_4.ip.filter(ip_ip='192.168.122.2').exists())
        self.assertTrue(system_5.ip.filter(ip_ip='192.168.122.20').exists())
        self.assertTrue(system_6.ip.filter(ip_ip='192.168.122.200').exists())
        self.assertTrue(system_7.ip.filter(ip_ip='192.168.2.1').exists())
        self.assertTrue(system_8.ip.filter(ip_ip='192.168.2.2').exists())
        self.assertTrue(system_9.ip.filter(ip_ip='::2').exists())
        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
        self.assertEqual(system_2.analysisstatus, analysisstatus_1)
        self.assertEqual(system_3.analysisstatus, analysisstatus_1)
        self.assertEqual(system_4.analysisstatus, analysisstatus_1)
        self.assertEqual(system_5.analysisstatus, analysisstatus_1)
        self.assertEqual(system_6.analysisstatus, analysisstatus_1)
        self.assertEqual(system_7.analysisstatus, analysisstatus_1)
        self.assertEqual(system_8.analysisstatus, analysisstatus_1)
        self.assertEqual(system_9.analysisstatus, analysisstatus_1)
        self.assertEqual(system_1.systemstatus, systemstatus_1)
        self.assertEqual(system_2.systemstatus, systemstatus_1)
        self.assertEqual(system_3.systemstatus, systemstatus_1)
        self.assertEqual(system_4.systemstatus, systemstatus_1)
        self.assertEqual(system_5.systemstatus, systemstatus_1)
        self.assertEqual(system_6.systemstatus, systemstatus_1)
        self.assertEqual(system_7.systemstatus, systemstatus_1)
        self.assertEqual(system_8.systemstatus, systemstatus_1)
        self.assertEqual(system_9.systemstatus, systemstatus_1)

    def test_system_importer_file_csv_config_based_post_complete(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        domain_1 = Domain.objects.get(domain_name='domain_1')
        os_1 = Os.objects.get(os_name='os_1')
        location_1 = Location.objects.get(location_name='location_1')
        reason_1 = Reason.objects.get(reason_name='reason_1')
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        case_1 = Case.objects.get(case_name='case_1')
        case_2 = Case.objects.get(case_name='case_2')
        case_3 = Case.objects.get(case_name='case_3')
        company_1 = Company.objects.get(company_name='company_1')
        company_2 = Company.objects.get(company_name='company_2')
        company_3 = Company.objects.get(company_name='company_3')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = True
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_dnsname = dnsname_1
        system_importer_file_csv_configbased_config_model.csv_default_domain = domain_1
        system_importer_file_csv_configbased_config_model.csv_default_os = os_1
        system_importer_file_csv_configbased_config_model.csv_default_location = location_1
        system_importer_file_csv_configbased_config_model.csv_default_reason = reason_1
        system_importer_file_csv_configbased_config_model.csv_default_systemtype = systemtype_1
        system_importer_file_csv_configbased_config_model.save()
        # change config (many to many)
        system_importer_file_csv_configbased_config_model.csv_default_case.clear()
        system_importer_file_csv_configbased_config_model.csv_default_company.clear()
        system_importer_file_csv_configbased_config_model.csv_default_tag.clear()
        system_importer_file_csv_configbased_config_model.csv_default_case.add(case_1)
        system_importer_file_csv_configbased_config_model.csv_default_company.add(company_1)
        system_importer_file_csv_configbased_config_model.csv_default_tag.add(tag_1)
        system_importer_file_csv_configbased_config_model.csv_default_case.add(case_2)
        system_importer_file_csv_configbased_config_model.csv_default_company.add(company_2)
        system_importer_file_csv_configbased_config_model.csv_default_tag.add(tag_2)
        system_importer_file_csv_configbased_config_model.csv_default_case.add(case_3)
        system_importer_file_csv_configbased_config_model.csv_default_company.add(company_3)
        system_importer_file_csv_configbased_config_model.csv_default_tag.add(tag_3)
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_complete.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_1 = System.objects.get(system_name='systems_csv_complete_001')
        system_2 = System.objects.get(system_name='systems_csv_complete_002')
        system_3 = System.objects.get(system_name='systems_csv_complete_003')
        system_4 = System.objects.get(system_name='systems_csv_complete_004')
        system_5 = System.objects.get(system_name='systems_csv_complete_005')
        system_6 = System.objects.get(system_name='systems_csv_complete_006')
        system_7 = System.objects.get(system_name='systems_csv_complete_007')
        system_8 = System.objects.get(system_name='systems_csv_complete_008')
        system_9 = System.objects.get(system_name='systems_csv_complete_009')
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '9 systems were created.')
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_001').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_002').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_003').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_004').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_005').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_006').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_007').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_008').exists())
        self.assertTrue(System.objects.filter(system_name='systems_csv_complete_009').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.0.0.1').exists())
        self.assertTrue(system_2.ip.filter(ip_ip='127.0.0.2').exists())
        self.assertTrue(system_3.ip.filter(ip_ip='127.0.0.3').exists())
        self.assertTrue(system_4.ip.filter(ip_ip='192.168.122.1').exists())
        self.assertTrue(system_5.ip.filter(ip_ip='192.168.122.10').exists())
        self.assertTrue(system_6.ip.filter(ip_ip='192.168.122.100').exists())
        self.assertTrue(system_7.ip.filter(ip_ip='192.168.1.1').exists())
        self.assertTrue(system_8.ip.filter(ip_ip='192.168.1.2').exists())
        self.assertTrue(system_9.ip.filter(ip_ip='::1').exists())
        # compare (only three occurences)
        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
        self.assertEqual(system_2.analysisstatus, analysisstatus_1)
        self.assertEqual(system_3.analysisstatus, analysisstatus_1)
        self.assertTrue(system_1.case.filter(case_name='case_1').exists())
        self.assertTrue(system_1.case.filter(case_name='case_2').exists())
        self.assertTrue(system_1.case.filter(case_name='case_3').exists())
        self.assertTrue(system_2.case.filter(case_name='case_1').exists())
        self.assertTrue(system_2.case.filter(case_name='case_2').exists())
        self.assertTrue(system_2.case.filter(case_name='case_3').exists())
        self.assertTrue(system_3.case.filter(case_name='case_1').exists())
        self.assertTrue(system_3.case.filter(case_name='case_2').exists())
        self.assertTrue(system_3.case.filter(case_name='case_3').exists())
        self.assertTrue(system_1.company.filter(company_name='company_1').exists())
        self.assertTrue(system_1.company.filter(company_name='company_2').exists())
        self.assertTrue(system_1.company.filter(company_name='company_3').exists())
        self.assertTrue(system_2.company.filter(company_name='company_1').exists())
        self.assertTrue(system_2.company.filter(company_name='company_2').exists())
        self.assertTrue(system_2.company.filter(company_name='company_3').exists())
        self.assertTrue(system_3.company.filter(company_name='company_1').exists())
        self.assertTrue(system_3.company.filter(company_name='company_2').exists())
        self.assertTrue(system_3.company.filter(company_name='company_3').exists())
        self.assertEqual(system_1.dnsname, dnsname_1)
        self.assertEqual(system_2.dnsname, dnsname_1)
        self.assertEqual(system_3.dnsname, dnsname_1)
        self.assertEqual(system_1.domain, domain_1)
        self.assertEqual(system_2.domain, domain_1)
        self.assertEqual(system_3.domain, domain_1)
        self.assertEqual(system_1.os, os_1)
        self.assertEqual(system_2.os, os_1)
        self.assertEqual(system_3.os, os_1)
        self.assertEqual(system_1.location, location_1)
        self.assertEqual(system_2.location, location_1)
        self.assertEqual(system_3.location, location_1)
        self.assertEqual(system_1.reason, reason_1)
        self.assertEqual(system_2.reason, reason_1)
        self.assertEqual(system_3.reason, reason_1)
        self.assertEqual(system_1.systemstatus, systemstatus_1)
        self.assertEqual(system_2.systemstatus, systemstatus_1)
        self.assertEqual(system_3.systemstatus, systemstatus_1)
        self.assertEqual(system_1.systemtype, systemtype_1)
        self.assertEqual(system_2.systemtype, systemtype_1)
        self.assertEqual(system_3.systemtype, systemtype_1)
        self.assertTrue(system_1.tag.filter(tag_name='tag_1').exists())
        self.assertTrue(system_1.tag.filter(tag_name='tag_2').exists())
        self.assertTrue(system_1.tag.filter(tag_name='tag_3').exists())
        self.assertTrue(system_2.tag.filter(tag_name='tag_1').exists())
        self.assertTrue(system_2.tag.filter(tag_name='tag_2').exists())
        self.assertTrue(system_2.tag.filter(tag_name='tag_3').exists())
        self.assertTrue(system_3.tag.filter(tag_name='tag_1').exists())
        self.assertTrue(system_3.tag.filter(tag_name='tag_2').exists())
        self.assertTrue(system_3.tag.filter(tag_name='tag_3').exists())

    def test_system_importer_file_csv_config_based_post_invalid(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_importer_file_csv_config_based.html')

    def test_system_importer_file_csv_config_based_post_data_file(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_data.dat'), 'rb')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # close file
        systemcsv.close()
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'File seems not to be a CSV file. Check file.')

    def test_system_importer_file_csv_config_based_post_double(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_double.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # close file
        systemcsv.close()
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(len(System.objects.filter(system_name='system_double')), 2)
        self.assertEqual(str(messages[0]), 'System system_double already exists multiple times. Nothing was changed for this system.')

    def test_system_importer_file_csv_config_based_post_wrong(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_wrong.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # close file
        systemcsv.close()
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'Value for system in row 1 was an empty string. System not created.')
        self.assertEqual(str(messages[1]), 'Value for system in row 2 was too long. System not created.')

    def test_system_importer_file_csv_config_based_post_skip(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_skip.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # close file
        systemcsv.close()
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_skip_1 = System.objects.get(system_name='system_skip_1')
        system_skip_2 = System.objects.get(system_name='system_skip_2')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '2 systems were skipped.')
        self.assertEqual(system_skip_1.analysisstatus, None)
        self.assertEqual(system_skip_1.systemstatus, systemstatus_1)
        self.assertTrue(system_skip_1.ip.filter(ip_ip='127.1.1.1').exists())
        self.assertFalse(system_skip_1.ip.filter(ip_ip='127.2.2.2').exists())
        self.assertEqual(system_skip_2.analysisstatus, None)
        self.assertEqual(system_skip_2.systemstatus, systemstatus_1)
        self.assertTrue(system_skip_2.ip.filter(ip_ip='127.3.3.3').exists())
        self.assertFalse(system_skip_2.ip.filter(ip_ip='127.4.4.4').exists())

    def test_system_importer_file_csv_config_based_post_update_discard_manytomany(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_2')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        case_2 = Case.objects.get(case_name='case_2')
        company_2 = Company.objects.get(company_name='company_2')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = False
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_2
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_2
        system_importer_file_csv_configbased_config_model.save()
        # change config (many to many)
        system_importer_file_csv_configbased_config_model.csv_default_case.clear()
        system_importer_file_csv_configbased_config_model.csv_default_company.clear()
        system_importer_file_csv_configbased_config_model.csv_default_tag.clear()
        system_importer_file_csv_configbased_config_model.csv_default_case.add(case_2)
        system_importer_file_csv_configbased_config_model.csv_default_company.add(company_2)
        system_importer_file_csv_configbased_config_model.csv_default_tag.add(tag_2)
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_discard_manytomany.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # close file
        systemcsv.close()
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_update_discard_manytomany_1 = System.objects.get(system_name='system_update_discard_manytomany_1')
        system_update_discard_manytomany_2 = System.objects.get(system_name='system_update_discard_manytomany_2')
        # compare - general
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '2 systems were updated.')
        # compare - system_update_discard_manytomany_1
        self.assertFalse(system_update_discard_manytomany_1.case.filter(case_name='case_1').exists())
        self.assertTrue(system_update_discard_manytomany_1.case.filter(case_name='case_2').exists())
        self.assertFalse(system_update_discard_manytomany_1.company.filter(company_name='company_1').exists())
        self.assertTrue(system_update_discard_manytomany_1.company.filter(company_name='company_2').exists())
        self.assertFalse(system_update_discard_manytomany_1.ip.filter(ip_ip='10.1.1.1').exists())
        self.assertTrue(system_update_discard_manytomany_1.ip.filter(ip_ip='10.3.3.3').exists())
        self.assertEqual(system_update_discard_manytomany_1.analysisstatus, analysisstatus_2)
        self.assertEqual(system_update_discard_manytomany_1.systemstatus, systemstatus_2)
        self.assertFalse(system_update_discard_manytomany_1.tag.filter(tag_name='tag_1').exists())
        self.assertTrue(system_update_discard_manytomany_1.tag.filter(tag_name='tag_2').exists())
        # compare - system_update_discard_manytomany_2
        self.assertTrue(system_update_discard_manytomany_2.case.filter(case_name='case_2').exists())
        self.assertTrue(system_update_discard_manytomany_2.company.filter(company_name='company_2').exists())
        self.assertFalse(system_update_discard_manytomany_2.ip.filter(ip_ip='10.2.2.2').exists())
        self.assertTrue(system_update_discard_manytomany_2.ip.filter(ip_ip='10.4.4.4').exists())
        self.assertEqual(system_update_discard_manytomany_2.analysisstatus, analysisstatus_2)
        self.assertEqual(system_update_discard_manytomany_2.systemstatus, systemstatus_2)
        self.assertTrue(system_update_discard_manytomany_2.tag.filter(tag_name='tag_2').exists())

    def test_system_importer_file_csv_config_based_post_update_keep_manytomany(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_2')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        case_2 = Case.objects.get(case_name='case_2')
        company_2 = Company.objects.get(company_name='company_2')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = False
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = False
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = False
        system_importer_file_csv_configbased_config_model.csv_remove_company = False
        system_importer_file_csv_configbased_config_model.csv_remove_tag = False
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_2
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_2
        system_importer_file_csv_configbased_config_model.save()
        # change config (many to many)
        system_importer_file_csv_configbased_config_model.csv_default_case.clear()
        system_importer_file_csv_configbased_config_model.csv_default_company.clear()
        system_importer_file_csv_configbased_config_model.csv_default_tag.clear()
        system_importer_file_csv_configbased_config_model.csv_default_case.add(case_2)
        system_importer_file_csv_configbased_config_model.csv_default_company.add(company_2)
        system_importer_file_csv_configbased_config_model.csv_default_tag.add(tag_2)
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_keep_manytomany.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # close file
        systemcsv.close()
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_update_keep_manytomany_1 = System.objects.get(system_name='system_update_keep_manytomany_1')
        system_update_keep_manytomany_2 = System.objects.get(system_name='system_update_keep_manytomany_2')
        # compare - general
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '2 systems were updated.')
        # compare - system_update_keep_manytomany_1
        self.assertTrue(system_update_keep_manytomany_1.case.filter(case_name='case_1').exists())
        self.assertTrue(system_update_keep_manytomany_1.case.filter(case_name='case_2').exists())
        self.assertTrue(system_update_keep_manytomany_1.company.filter(company_name='company_1').exists())
        self.assertTrue(system_update_keep_manytomany_1.company.filter(company_name='company_2').exists())
        self.assertTrue(system_update_keep_manytomany_1.ip.filter(ip_ip='10.5.5.5').exists())
        self.assertTrue(system_update_keep_manytomany_1.ip.filter(ip_ip='10.7.7.7').exists())
        self.assertEqual(system_update_keep_manytomany_1.systemstatus, systemstatus_2)
        self.assertTrue(system_update_keep_manytomany_1.tag.filter(tag_name='tag_1').exists())
        self.assertTrue(system_update_keep_manytomany_1.tag.filter(tag_name='tag_2').exists())
        # compare - system_update_keep_manytomany_2
        self.assertTrue(system_update_keep_manytomany_2.case.filter(case_name='case_2').exists())
        self.assertTrue(system_update_keep_manytomany_2.company.filter(company_name='company_2').exists())
        self.assertTrue(system_update_keep_manytomany_2.ip.filter(ip_ip='10.6.6.6').exists())
        self.assertTrue(system_update_keep_manytomany_2.ip.filter(ip_ip='10.8.8.8').exists())
        self.assertEqual(system_update_keep_manytomany_2.systemstatus, systemstatus_2)
        self.assertTrue(system_update_keep_manytomany_2.tag.filter(tag_name='tag_2').exists())

    def test_system_importer_file_csv_config_based_post_create_single(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = False
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_create_single.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get object
        system_1 = System.objects.get(system_name='system_create_single_1')
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '1 system was created.')
        self.assertTrue(System.objects.filter(system_name='system_create_single_1').exists())
        self.assertFalse(system_1.ip.filter(ip_ip='127.1.2.31').exists())
        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
        self.assertEqual(system_1.systemstatus, systemstatus_1)

    def test_system_importer_file_csv_config_based_post_update_single(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = False
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = False
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_2
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_single.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_1 = System.objects.get(system_name='system_update_single_1')
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '1 system was updated.')
        self.assertTrue(System.objects.filter(system_name='system_update_single_1').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.2.3.41').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.2.3.42').exists())
        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
        self.assertEqual(system_1.systemstatus, systemstatus_2)

    def test_system_importer_file_csv_config_based_post_skip_single(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = False
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_2
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_skip_single.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_1 = System.objects.get(system_name='system_skip_single_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), '1 system was skipped.')
        self.assertTrue(System.objects.filter(system_name='system_skip_single_1').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.3.4.51').exists())
        self.assertFalse(system_1.ip.filter(ip_ip='127.3.4.52').exists())
        self.assertEqual(system_1.analysisstatus, None)
        self.assertEqual(system_1.systemstatus, systemstatus_1)

    def test_system_importer_file_csv_config_based_post_invalid_ip(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_config_based', password='URVYUzUig1BrzToryfkm')
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # change config
        system_importer_file_csv_configbased_config_model = SystemImporterFileCsvConfigbasedConfigModel(system_importer_file_csv_configbased_config_name='SystemImporterFileCsvConfigbasedConfig')
        system_importer_file_csv_configbased_config_model.csv_skip_existing_system = True
        system_importer_file_csv_configbased_config_model.csv_column_system = 1
        system_importer_file_csv_configbased_config_model.csv_headline = False
        system_importer_file_csv_configbased_config_model.csv_choice_ip = True
        system_importer_file_csv_configbased_config_model.csv_remove_ip = True
        system_importer_file_csv_configbased_config_model.csv_column_ip = 2
        system_importer_file_csv_configbased_config_model.csv_remove_case = True
        system_importer_file_csv_configbased_config_model.csv_remove_company = True
        system_importer_file_csv_configbased_config_model.csv_remove_tag = True
        system_importer_file_csv_configbased_config_model.csv_default_systemstatus = systemstatus_1
        system_importer_file_csv_configbased_config_model.csv_default_analysisstatus = analysisstatus_1
        system_importer_file_csv_configbased_config_model.save()
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_invalid_ip.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
            'systemstatus': systemstatus_1.systemstatus_id,
        }
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/configbased/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # get objects
        system_1 = System.objects.get(system_name='system_invalid_ip_1')
        # close file
        systemcsv.close()
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'Value for ip address in row 1 was not a valid IP address.')
        self.assertEqual(str(messages[1]), '1 system was created.')
        self.assertTrue(System.objects.filter(system_name='system_invalid_ip_1').exists())
        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
        self.assertEqual(system_1.systemstatus, systemstatus_1)
