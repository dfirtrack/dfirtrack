from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.models import Analysisstatus, Case, Company, Dnsname, Domain, Location, Ip, Os, Reason, Recommendation, Serviceprovider, System, Systemstatus, Systemtype, Tag
from dfirtrack_main.tests.system_importer.config_functions import change_csv_import_filename
import os
import urllib.parse


class SystemImporterFileCsvInstantViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):
        """ one-time setup """

        # create user
        User.objects.create_user(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')

        # create objects
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_2')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_2')

    @classmethod
    def setUp(cls):
        """ setup in advance of every test """

        # get user
        test_user = User.objects.get(username='testuser_system_importer_file_csv_instant')

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        analysisstatus_2 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_2')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')

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

    def test_system_importer_file_csv_instant_minimal_double_quotation(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        change_csv_import_filename('system_importer_file_csv_testfile_01_minimal_double_quotation.csv')
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
        change_csv_import_filename('system_importer_file_csv_testfile_02_minimal_single_quotation.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
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
        change_csv_import_filename('system_importer_file_csv_testfile_03_minimal_headline.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
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
        change_csv_import_filename('system_importer_file_csv_testfile_07_complete.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_choice_tagfree_systemstatus = True
        system_importer_file_csv_config_model.csv_choice_tagfree_analysisstatus = True
        system_importer_file_csv_config_model.csv_choice_ip = True
        system_importer_file_csv_config_model.csv_column_ip = 2
        system_importer_file_csv_config_model.csv_choice_tag = True
        system_importer_file_csv_config_model.csv_column_tag = 3
        system_importer_file_csv_config_model.csv_tag_prefix = 'AUTO'
        system_importer_file_csv_config_model.csv_tag_prefix_delimiter = 'tag_prefix_underscore'
        system_importer_file_csv_config_model.csv_choice_dnsname = True
        system_importer_file_csv_config_model.csv_column_dnsname = 4
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 5
        system_importer_file_csv_config_model.csv_choice_location = True
        system_importer_file_csv_config_model.csv_column_location = 6
        system_importer_file_csv_config_model.csv_choice_os = True
        system_importer_file_csv_config_model.csv_column_os = 7
        system_importer_file_csv_config_model.csv_choice_reason = True
        system_importer_file_csv_config_model.csv_column_reason = 8
        system_importer_file_csv_config_model.csv_choice_recommendation = True
        system_importer_file_csv_config_model.csv_column_recommendation = 9
        system_importer_file_csv_config_model.csv_choice_serviceprovider = True
        system_importer_file_csv_config_model.csv_column_serviceprovider = 10
        system_importer_file_csv_config_model.csv_choice_systemtype = True
        system_importer_file_csv_config_model.csv_column_systemtype = 11
        system_importer_file_csv_config_model.csv_choice_case = True
        system_importer_file_csv_config_model.csv_column_case = 12
        system_importer_file_csv_config_model.csv_choice_company = True
        system_importer_file_csv_config_model.csv_column_company = 13
        system_importer_file_csv_config_model.save()
        # get objects (previously created)
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        analysisstatus_2 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_2')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
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
        self.assertTrue(Case.objects.filter(case_name='case_1').exists())
        self.assertTrue(Company.objects.filter(company_name='company_1').exists())
        self.assertTrue(Dnsname.objects.filter(dnsname_name='example.com').exists())
        self.assertTrue(Dnsname.objects.filter(dnsname_name='dfirtrack.org').exists())
        self.assertTrue(Domain.objects.filter(domain_name='DOM1').exists())
        self.assertTrue(Domain.objects.filter(domain_name='DOM3').exists())
        self.assertTrue(Location.objects.filter(location_name='Berlin').exists())
        self.assertTrue(Location.objects.filter(location_name='Hamburg').exists())
        self.assertTrue(Location.objects.filter(location_name='Munich').exists())
        self.assertTrue(Os.objects.filter(os_name='Linux').exists())
        self.assertTrue(Os.objects.filter(os_name='Windows Server 2008 R2').exists())
        self.assertTrue(Os.objects.filter(os_name='Windows 10').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='127.1.0.1').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='127.1.0.2').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='127.1.0.3').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='10.2.0.1').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='10.2.0.2').exists())
        self.assertTrue(Ip.objects.filter(ip_ip='10.2.0.3').exists())
        self.assertTrue(Reason.objects.filter(reason_name='reason_1').exists())
        self.assertTrue(Recommendation.objects.filter(recommendation_name='recommendation_1').exists())
        self.assertTrue(Serviceprovider.objects.filter(serviceprovider_name='serviceprovider_1').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_07_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_07_002').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_07_003').exists())
        self.assertTrue(Systemtype.objects.filter(systemtype_name='Client').exists())
        self.assertTrue(Systemtype.objects.filter(systemtype_name='Domaincontroller').exists())
        self.assertTrue(Systemtype.objects.filter(systemtype_name='Fileserver').exists())
        self.assertTrue(Tag.objects.filter(tag_name='AUTO_tag_1').exists())
        self.assertTrue(Tag.objects.filter(tag_name='AUTO_tag_2').exists())
        self.assertTrue(Tag.objects.filter(tag_name='AUTO_tag_3').exists())
        self.assertTrue(Tag.objects.filter(tag_name='AUTO_tag_4').exists())
        # get (fk) objects (to increase the performance for the following comparisons / for better readability)
        dnsname_1 = Dnsname.objects.get(dnsname_name='example.com')
        dnsname_3 = Dnsname.objects.get(dnsname_name='dfirtrack.org')
        domain_1 = Domain.objects.get(domain_name='DOM1')
        domain_3 = Domain.objects.get(domain_name='DOM3')
        location_1 = Location.objects.get(location_name='Berlin')
        location_2 = Location.objects.get(location_name='Munich')
        location_3 = Location.objects.get(location_name='Hamburg')
        system_1 = System.objects.get(system_name='system_csv_07_001')
        system_2 = System.objects.get(system_name='system_csv_07_002')
        system_3 = System.objects.get(system_name='system_csv_07_003')
        os_1 = Os.objects.get(os_name='Linux')
        os_2 = Os.objects.get(os_name='Windows Server 2008 R2')
        os_3 = Os.objects.get(os_name='Windows 10')
        reason_1= Reason.objects.get(reason_name='reason_1')
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        systemtype_1 = Systemtype.objects.get(systemtype_name='Fileserver')
        systemtype_2 = Systemtype.objects.get(systemtype_name='Domaincontroller')
        systemtype_3 = Systemtype.objects.get(systemtype_name='Client')
        # compare - relations
        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
        self.assertEqual(system_2.analysisstatus, analysisstatus_2)
        self.assertEqual(system_3.analysisstatus, analysisstatus_1)
        self.assertEqual(system_1.systemstatus, systemstatus_1)
        self.assertEqual(system_2.systemstatus, systemstatus_2)
        self.assertEqual(system_3.systemstatus, systemstatus_1)
        self.assertTrue(system_1.ip.filter(ip_ip='127.1.0.1').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.1.0.2').exists())
        self.assertTrue(system_1.ip.filter(ip_ip='127.1.0.3').exists())
        self.assertTrue(system_2.ip.filter(ip_ip='10.2.0.1').exists())
        self.assertTrue(system_2.ip.filter(ip_ip='10.2.0.2').exists())
        self.assertTrue(system_2.ip.filter(ip_ip='10.2.0.3').exists())
        self.assertTrue(system_1.tag.filter(tag_name='AUTO_tag_1').exists())
        self.assertTrue(system_1.tag.filter(tag_name='AUTO_tag_2').exists())
        self.assertTrue(system_3.tag.filter(tag_name='AUTO_tag_2').exists())
        self.assertTrue(system_3.tag.filter(tag_name='AUTO_tag_3').exists())
        self.assertTrue(system_3.tag.filter(tag_name='AUTO_tag_4').exists())
        self.assertTrue(system_1.tag.filter(tag_name='AUTO_tag_1').exists())
        self.assertTrue(system_1.dnsname, dnsname_1)
        self.assertTrue(system_3.dnsname, dnsname_3)
        self.assertTrue(system_1.domain, domain_1)
        self.assertTrue(system_3.domain, domain_3)
        self.assertTrue(system_1.location, location_1)
        self.assertTrue(system_2.location, location_2)
        self.assertTrue(system_3.location, location_3)
        self.assertTrue(system_1.os, os_1)
        self.assertTrue(system_2.os, os_2)
        self.assertTrue(system_3.os, os_3)
        self.assertTrue(system_1.reason, reason_1)
        self.assertTrue(system_1.recommendation, recommendation_1)
        self.assertTrue(system_1.serviceprovider, serviceprovider_1)
        self.assertTrue(system_1.systemtype, systemtype_1)
        self.assertTrue(system_2.systemtype, systemtype_2)
        self.assertTrue(system_3.systemtype, systemtype_3)
        self.assertTrue(system_1.case.filter(case_name='case_1').exists())
        self.assertTrue(system_1.company.filter(company_name='company_1').exists())

    def test_system_importer_file_csv_instant_minimal_comma(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        change_csv_import_filename('system_importer_file_csv_testfile_21_minimal_comma.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
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

    def test_system_importer_file_csv_instant_minimal_semicolon(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_instant', password='lw3V2i2uaTFlk4yTlIaV')
        # change config
        change_csv_import_filename('system_importer_file_csv_testfile_22_minimal_semicolon.csv')
        # change config
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_semicolon'
        system_importer_file_csv_config_model.csv_choice_domain = True
        system_importer_file_csv_config_model.csv_column_domain = 2
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
