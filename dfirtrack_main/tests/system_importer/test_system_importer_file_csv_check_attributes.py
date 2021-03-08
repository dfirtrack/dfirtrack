from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemImporterFileCsvConfigModel
from dfirtrack_main.importer.file.csv import system_cron
from dfirtrack_main.models import Analysisstatus, Case, Company, Domain, Location, Os, System, Systemstatus, Tag, Tagcolor
from mock import patch
import os
import urllib.parse


#def set_config_choices_true(system_importer_file_csv_config_model):
#    """ set choices to true for all columns """
#
#    # set config values
#    system_importer_file_csv_config_model.csv_choice_system = True
#    system_importer_file_csv_config_model.csv_choice_ip = True
#    system_importer_file_csv_config_model.csv_choice_dnsname = True
#    system_importer_file_csv_config_model.csv_choice_domain = True
#    system_importer_file_csv_config_model.csv_choice_location = True
#    system_importer_file_csv_config_model.csv_choice_os = True
#    system_importer_file_csv_config_model.csv_choice_reason = True
#    system_importer_file_csv_config_model.csv_choice_recommendation = True
#    system_importer_file_csv_config_model.csv_choice_serviceprovider = True
#    system_importer_file_csv_config_model.csv_choice_systemtype = True
#    system_importer_file_csv_config_model.csv_choice_case = True
#    system_importer_file_csv_config_model.csv_choice_company = True
#    system_importer_file_csv_config_model.csv_choice_tag = True
#
#    # return config to config function
#    return system_importer_file_csv_config_model
#
#def set_config_column_fields_numeric_values():
#    """ set numeric values for columns out of range """
#
#    # get config
#    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#    # set choices to true for all columns
#    system_importer_file_csv_config_model = set_config_choices_true(system_importer_file_csv_config_model)
#
#    # set config values
#    system_importer_file_csv_config_model.csv_column_system = 100
#    system_importer_file_csv_config_model.csv_column_ip = 101
#    system_importer_file_csv_config_model.csv_column_dnsname = 102
#    system_importer_file_csv_config_model.csv_column_domain = 103
#    system_importer_file_csv_config_model.csv_column_location = 104
#    system_importer_file_csv_config_model.csv_column_os = 105
#    system_importer_file_csv_config_model.csv_column_reason = 106
#    system_importer_file_csv_config_model.csv_column_recommendation = 107
#    system_importer_file_csv_config_model.csv_column_serviceprovider = 108
#    system_importer_file_csv_config_model.csv_column_systemtype = 109
#    system_importer_file_csv_config_model.csv_column_case = 110
#    system_importer_file_csv_config_model.csv_column_company = 111
#    system_importer_file_csv_config_model.csv_column_tag = 112
#
#    # save config
#    system_importer_file_csv_config_model.save()
#
#    # return to column fields numeric values test function
#    return
#
#def set_config_column_choice_vs_default_single_error():
#    """ set column, choice and default single error """
#
#    # get config
#    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#    # set config values
#    system_importer_file_csv_config_model.csv_column_system = 1
#    system_importer_file_csv_config_model.csv_choice_ip = False
#    system_importer_file_csv_config_model.csv_column_ip = 2
#
#    # save config
#    system_importer_file_csv_config_model.save()
#
#    # return to column choice vs default test function
#    return
#
#def set_config_column_choice_vs_default_multiple_errors():
#    """ set column, choice and default randomly faulty """
#
#    # get objects
#    case_1 = Case.objects.get(case_name='case_1')
#    company_1 = Company.objects.get(company_name='company_1')
#    domain_1 = Domain.objects.get(domain_name='domain_1')
#    location_1 = Location.objects.get(location_name='location_1')
#    os_1 = Os.objects.get(os_name='os_1')
#    tag_1 = Tag.objects.get(tag_name='tag_1')
#
#    # get config
#    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#    # set config values
#    system_importer_file_csv_config_model.csv_column_system = 1
#    # CSV not chosen and CSV column filled out / +1
#    system_importer_file_csv_config_model.csv_choice_ip = False
#    system_importer_file_csv_config_model.csv_column_ip = 2
#    # CSV chosen and no CSV column filled out / +1
#    system_importer_file_csv_config_model.csv_choice_dnsname = True
#    system_importer_file_csv_config_model.csv_column_dnsname = None
#    system_importer_file_csv_config_model.csv_default_dnsname = None
#    # CSV chosen and DB chosen / CSV column filled out and DB chosen / +2
#    system_importer_file_csv_config_model.csv_choice_domain = True
#    system_importer_file_csv_config_model.csv_column_domain = 4
#    system_importer_file_csv_config_model.csv_default_domain = domain_1
#    # CSV column filled out and DB chosen / CSV not chosen and CSV column filled out / +2
#    system_importer_file_csv_config_model.csv_choice_location = False
#    system_importer_file_csv_config_model.csv_column_location = 5
#    system_importer_file_csv_config_model.csv_default_location = location_1
#    # CSV chosen and no CSV column filled out / CSV chosen and DB chosen / +2
#    system_importer_file_csv_config_model.csv_choice_os = True
#    system_importer_file_csv_config_model.csv_column_os = None
#    system_importer_file_csv_config_model.csv_default_os = os_1
#    # CSV not chosen and CSV column filled out / +1
#    system_importer_file_csv_config_model.csv_choice_reason = False
#    system_importer_file_csv_config_model.csv_column_reason = 7
#    system_importer_file_csv_config_model.csv_default_reason = None
#    # CSV not chosen and CSV column filled out / +1
#    system_importer_file_csv_config_model.csv_choice_recommendation = False
#    system_importer_file_csv_config_model.csv_column_recommendation = 8
#    system_importer_file_csv_config_model.csv_default_recommendation = None
#    # CSV not chosen and CSV column filled out / +1
#    system_importer_file_csv_config_model.csv_choice_serviceprovider = False
#    system_importer_file_csv_config_model.csv_column_serviceprovider = 9
#    system_importer_file_csv_config_model.csv_default_serviceprovider = None
#    # CSV not chosen and CSV column filled out / +1
#    system_importer_file_csv_config_model.csv_choice_systemtype = False
#    system_importer_file_csv_config_model.csv_column_systemtype = 10
#    system_importer_file_csv_config_model.csv_default_systemtype = None
#    # CSV chosen and DB chosen / CSV column filled out and DB chosen / +2
#    system_importer_file_csv_config_model.csv_choice_case = True
#    system_importer_file_csv_config_model.csv_column_case = 11
#    system_importer_file_csv_config_model.csv_default_case.add(case_1)
#    # CSV column filled out and DB chosen / CSV not chosen and CSV column filled out / +2
#    system_importer_file_csv_config_model.csv_choice_company = False
#    system_importer_file_csv_config_model.csv_column_company = 12
#    system_importer_file_csv_config_model.csv_default_company.add(company_1)
#    # CSV chosen and no CSV column filled out / CSV chosen and DB chosen / +2
#    system_importer_file_csv_config_model.csv_choice_tag = True
#    system_importer_file_csv_config_model.csv_column_tag = None
#    system_importer_file_csv_config_model.csv_default_tag.add(tag_1)
#
#    # save config
#    system_importer_file_csv_config_model.save()
#
#    # return to column choice vs default test function
#    return
#
#def set_config_tagfree_choices():
#    """ set tagfree statuses without tag choice """
#
#    # get config
#    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#    # set config values
#    system_importer_file_csv_config_model.csv_choice_tag = False
#    system_importer_file_csv_config_model.csv_choice_tagfree_systemstatus = True
#    system_importer_file_csv_config_model.csv_choice_tagfree_analysisstatus = True
#
#    # save config
#    system_importer_file_csv_config_model.save()
#
#    # return to tagfree choices test function
#    return
#
#def set_config_column_fields_equal_values():
#    """ set numeric values for column fields equal """
#
#    # get config
#    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#    # set choices to true for all columns
#    system_importer_file_csv_config_model = set_config_choices_true(system_importer_file_csv_config_model)
#
#    # set config values
#    system_importer_file_csv_config_model.csv_column_system = 1
#    system_importer_file_csv_config_model.csv_column_ip = 1
#    system_importer_file_csv_config_model.csv_column_dnsname = 1
#    system_importer_file_csv_config_model.csv_column_domain = 1
#    system_importer_file_csv_config_model.csv_column_location = 1
#    system_importer_file_csv_config_model.csv_column_os = 1
#    system_importer_file_csv_config_model.csv_column_reason = 1
#    system_importer_file_csv_config_model.csv_column_recommendation = 1
#    system_importer_file_csv_config_model.csv_column_serviceprovider = 1
#    system_importer_file_csv_config_model.csv_column_systemtype = 1
#    system_importer_file_csv_config_model.csv_column_case = 1
#    system_importer_file_csv_config_model.csv_column_company = 1
#    system_importer_file_csv_config_model.csv_column_tag = 1
#
#    # save config
#    system_importer_file_csv_config_model.save()
#
#    # return to column fields different values test function
#    return
#
#def set_config_remove_choices():
#    """ set remove choices in combination with skipping systems """
#
#    # get config
#    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#    # set config values
#    system_importer_file_csv_config_model.csv_skip_existing_system = True
#    system_importer_file_csv_config_model.csv_remove_systemstatus = True
#    system_importer_file_csv_config_model.csv_remove_analysisstatus = True
#    system_importer_file_csv_config_model.csv_remove_ip = True
#    system_importer_file_csv_config_model.csv_remove_dnsname = True
#    system_importer_file_csv_config_model.csv_remove_domain = True
#    system_importer_file_csv_config_model.csv_remove_location = True
#    system_importer_file_csv_config_model.csv_remove_os = True
#    system_importer_file_csv_config_model.csv_remove_reason = True
#    system_importer_file_csv_config_model.csv_remove_recommendation = True
#    system_importer_file_csv_config_model.csv_remove_serviceprovider = True
#    system_importer_file_csv_config_model.csv_remove_systemtype = True
#    system_importer_file_csv_config_model.csv_remove_case = True
#    system_importer_file_csv_config_model.csv_remove_company = True
#
#    # save config
#    system_importer_file_csv_config_model.save()
#
#    # return to remove choices test function
#    return

class SystemImporterFileCsvCheckAttributesViewTestCase(TestCase):
    """ system importer file CSV view tests """

    @classmethod
    def setUpTestData(cls):
        """ one-time setup """

        """ create objects """

        # create users
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_check_attributes', password='vlQnN2tg9HVGyyyIvezt')
        User.objects.create_user(username='message_user', password='POPKkir2A2biti52AYJG')

        # create objects
        analysisstatus_1 = Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
#        Case.objects.create(
#            case_name='case_1',
#            case_is_incident=True,
#            case_created_by_user_id=test_user,
#        )
#        Company.objects.create(company_name='company_1')
#        Domain.objects.create(domain_name='domain_1')
#        Location.objects.create(location_name='location_1')
#        Os.objects.create(os_name='os_1')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
#        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
#        Tag.objects.create(
#            tag_name='tag_1',
#            tagcolor=tagcolor_1,
#        )

        """ set config with fixed values """

        # build local path with test files
        csv_import_path = os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/')
        csv_import_filename = 'system_importer_file_csv_testfile_31_faulty_system.csv'

        # set fixed config values
        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
        system_importer_file_csv_config_model.csv_column_system = 2
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
        system_importer_file_csv_config_model.csv_field_delimiter = 'field_comma'
        system_importer_file_csv_config_model.csv_text_quote = 'text_double_quotation_marks'
        system_importer_file_csv_config_model.csv_ip_delimiter = 'ip_semicolon'
        system_importer_file_csv_config_model.csv_tag_delimiter = 'tag_space'

        # save config
        system_importer_file_csv_config_model.save()

#    @classmethod
#    def setUp(cls):
#        """ setup in advance of every test """
#
#        """ clean non-mandatory values which may set by other tests """
#
#        # get config
#        system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
#
#        # (re)set config values
#        system_importer_file_csv_config_model.csv_column_system = 1
#        system_importer_file_csv_config_model.csv_skip_existing_system = False
#        system_importer_file_csv_config_model.csv_remove_systemstatus = False
#        system_importer_file_csv_config_model.csv_remove_analysisstatus = False
#        system_importer_file_csv_config_model.csv_choice_tagfree_systemstatus = False
#        system_importer_file_csv_config_model.csv_choice_tagfree_analysisstatus = False
#        system_importer_file_csv_config_model.csv_choice_ip = False
#        system_importer_file_csv_config_model.csv_column_ip = None
#        system_importer_file_csv_config_model.csv_remove_ip = False
#        system_importer_file_csv_config_model.csv_choice_dnsname = False
#        system_importer_file_csv_config_model.csv_column_dnsname = None
#        system_importer_file_csv_config_model.csv_default_dnsname = None
#        system_importer_file_csv_config_model.csv_remove_dnsname = False
#        system_importer_file_csv_config_model.csv_choice_domain = False
#        system_importer_file_csv_config_model.csv_column_domain = None
#        system_importer_file_csv_config_model.csv_default_domain = None
#        system_importer_file_csv_config_model.csv_remove_domain = False
#        system_importer_file_csv_config_model.csv_choice_location = False
#        system_importer_file_csv_config_model.csv_column_location = None
#        system_importer_file_csv_config_model.csv_default_location = None
#        system_importer_file_csv_config_model.csv_remove_location = False
#        system_importer_file_csv_config_model.csv_choice_os = False
#        system_importer_file_csv_config_model.csv_column_os = None
#        system_importer_file_csv_config_model.csv_default_os = None
#        system_importer_file_csv_config_model.csv_remove_os = False
#        system_importer_file_csv_config_model.csv_choice_reason = False
#        system_importer_file_csv_config_model.csv_column_reason = None
#        system_importer_file_csv_config_model.csv_default_reason = None
#        system_importer_file_csv_config_model.csv_remove_reason = False
#        system_importer_file_csv_config_model.csv_choice_recommendation = False
#        system_importer_file_csv_config_model.csv_column_recommendation = None
#        system_importer_file_csv_config_model.csv_default_recommendation = None
#        system_importer_file_csv_config_model.csv_remove_recommendation = False
#        system_importer_file_csv_config_model.csv_choice_serviceprovider = False
#        system_importer_file_csv_config_model.csv_column_serviceprovider = None
#        system_importer_file_csv_config_model.csv_default_serviceprovider = None
#        system_importer_file_csv_config_model.csv_remove_serviceprovider = False
#        system_importer_file_csv_config_model.csv_choice_systemtype = False
#        system_importer_file_csv_config_model.csv_column_systemtype = None
#        system_importer_file_csv_config_model.csv_default_systemtype = None
#        system_importer_file_csv_config_model.csv_remove_systemtype = False
#        system_importer_file_csv_config_model.csv_choice_case = False
#        system_importer_file_csv_config_model.csv_column_case = None
#        system_importer_file_csv_config_model.csv_default_case.clear()
#        system_importer_file_csv_config_model.csv_remove_case = False
#        system_importer_file_csv_config_model.csv_choice_company = False
#        system_importer_file_csv_config_model.csv_column_company = None
#        system_importer_file_csv_config_model.csv_default_company.clear()
#        system_importer_file_csv_config_model.csv_remove_company = False
#        system_importer_file_csv_config_model.csv_choice_tag = False
#        system_importer_file_csv_config_model.csv_column_tag = None
#        system_importer_file_csv_config_model.csv_default_tag.clear()
#        system_importer_file_csv_config_model.csv_remove_tag = 'tag_remove_prefix'
#        system_importer_file_csv_config_model.csv_tag_prefix = 'AUTO'
#        system_importer_file_csv_config_model.csv_tag_prefix_delimiter = 'tag_prefix_underscore'
#
#        # save config
#        system_importer_file_csv_config_model.save()

    """ check numeric values of column fields for range """

    def test_system_importer_file_csv_check_attributes_cron_faulty_system(self):
        """ test importer view """

        # mock timezone.now()
        t_1 = datetime(2021, 3, 8, 18, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # execute cron job / scheduled task
            system_cron()

        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_attributes', password='vlQnN2tg9HVGyyyIvezt')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_importer_file_csv_check_attributes')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 3 | multiple: 0 [2021-03-08 18:05:00 - 2021-03-08 18:05:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='POPKkir2A2biti52AYJG')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, 'System CSV importer: created: 3 | updated: 0 | skipped: 3 | multiple: 0 [2021-03-08 18:05:00 - 2021-03-08 18:05:00]')
        self.assertEqual(messages[0].level_tag, 'success')
        self.assertTrue(System.objects.filter(system_name='system_csv_31_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_31_003').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_31_006').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_31_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_006').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_003').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_006').systemstatus, systemstatus_1)

    def test_system_importer_file_csv_check_attributes_instant_faulty_system(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_attributes', password='vlQnN2tg9HVGyyyIvezt')
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
        self.assertEqual(messages[0].message, 'Value for system in row 2 was too long. System not created.')
        self.assertEqual(messages[0].level_tag, 'warning')
        self.assertEqual(messages[1].message, 'Value for system in row 4 was an empty string. System not created.')
        self.assertEqual(messages[1].level_tag, 'warning')
        self.assertEqual(messages[2].message, 'Index for system in row 5 was out of range. System not created.')
        self.assertEqual(messages[2].level_tag, 'warning')
        self.assertEqual(messages[3].message, '3 systems were created.')
        self.assertEqual(messages[3].level_tag, 'success')
        self.assertEqual(messages[4].message, '3 systems were skipped.')
        self.assertEqual(messages[4].level_tag, 'success')
        self.assertTrue(System.objects.filter(system_name='system_csv_31_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_31_003').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_31_006').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_31_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_006').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_003').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_006').systemstatus, systemstatus_1)

    def test_system_importer_file_csv_check_attributes_upload_post_faulty_system(self):
        """ test importer view """

        # login testuser
        self.client.login(username='testuser_system_importer_file_csv_check_attributes', password='vlQnN2tg9HVGyyyIvezt')
        # open upload file
        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system_importer/system_importer_file_csv_files/system_importer_file_csv_testfile_31_faulty_system.csv'), 'r')
        # create post data
        data_dict = {
            'systemcsv': systemcsv,
        }
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1')
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.post('/system/importer/file/csv/upload/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(messages[0].message, 'Value for system in row 2 was too long. System not created.')
        self.assertEqual(messages[0].level_tag, 'warning')
        self.assertEqual(messages[1].message, 'Value for system in row 4 was an empty string. System not created.')
        self.assertEqual(messages[1].level_tag, 'warning')
        self.assertEqual(messages[2].message, 'Index for system in row 5 was out of range. System not created.')
        self.assertEqual(messages[2].level_tag, 'warning')
        self.assertEqual(messages[3].message, '3 systems were created.')
        self.assertEqual(messages[3].level_tag, 'success')
        self.assertEqual(messages[4].message, '3 systems were skipped.')
        self.assertEqual(messages[4].level_tag, 'success')
        self.assertTrue(System.objects.filter(system_name='system_csv_31_001').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_31_003').exists())
        self.assertTrue(System.objects.filter(system_name='system_csv_31_006').exists())
        self.assertEqual(System.objects.get(system_name='system_csv_31_001').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_003').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_006').analysisstatus, analysisstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_001').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_003').systemstatus, systemstatus_1)
        self.assertEqual(System.objects.get(system_name='system_csv_31_006').systemstatus, systemstatus_1)
        # close file
        systemcsv.close()
