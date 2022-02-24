import csv
import urllib.parse
from datetime import datetime
from unittest.mock import patch

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone

from dfirtrack_config.models import (
    MainConfigModel,
    SystemExporterSpreadsheetCsvConfigModel,
)
from dfirtrack_main.exporter.spreadsheet.csv import system_cron
from dfirtrack_main.models import (
    Analysisstatus,
    Case,
    Company,
    Dnsname,
    Domain,
    Ip,
    Location,
    Os,
    Reason,
    Recommendation,
    Serviceprovider,
    System,
    Systemstatus,
    Systemtype,
    Tag,
    Tagcolor,
)
from dfirtrack_main.tests.system.system_exporter_spreadsheet_csv_shared_checks import (
    system_exporter_spreadsheet_csv_complete_spreadsheet_check,
)


class SystemExporterSpreadsheetCsvViewTestCase(TestCase):
    """system exporter spreadsheet CSV view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_system_exporter_spreadsheet_csv',
            is_staff=True,
            is_superuser=True,
            password='XJzSzgX2q39OUWluwxoj',
        )
        User.objects.create_user(
            username='message_user', password='3qXjYKBj1CVCakjbCd7A'
        )

        # create objects
        dnsname_1 = Dnsname.objects.create(dnsname_name='dnsname_1')
        domain_1 = Domain.objects.create(domain_name='domain_1')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        analysisstatus_1 = Analysisstatus.objects.create(
            analysisstatus_name='analysisstatus_1'
        )
        reason_1 = Reason.objects.create(reason_name='reason_1')
        recommendation_1 = Recommendation.objects.create(
            recommendation_name='recommendation_1'
        )
        systemtype_1 = Systemtype.objects.create(systemtype_name='systemtype_1')
        ip_1 = Ip.objects.create(ip_ip='127.0.0.1')
        ip_2 = Ip.objects.create(ip_ip='127.0.0.2')
        ip_3 = Ip.objects.create(ip_ip='127.0.0.3')
        os_1 = Os.objects.create(os_name='os_1')
        company_1 = Company.objects.create(company_name='company_1')
        company_2 = Company.objects.create(company_name='company_2')
        company_3 = Company.objects.create(company_name='company_3')
        location_1 = Location.objects.create(location_name='location_1')
        serviceprovider_1 = Serviceprovider.objects.create(
            serviceprovider_name='serviceprovider_1'
        )
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        tag_1 = Tag.objects.create(
            tag_name='tag_1',
            tagcolor=tagcolor_1,
        )
        tag_2 = Tag.objects.create(
            tag_name='tag_2',
            tagcolor=tagcolor_1,
        )
        tag_3 = Tag.objects.create(
            tag_name='tag_3',
            tagcolor=tagcolor_1,
        )
        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )
        case_2 = Case.objects.create(
            case_name='case_2',
            case_is_incident=False,
            case_created_by_user_id=test_user,
        )
        case_3 = Case.objects.create(
            case_name='case_3',
            case_is_incident=False,
            case_created_by_user_id=test_user,
        )

        """ create systems """

        # mock timezone.now()
        t_1 = datetime(2011, 12, 13, 14, 15, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # create object with maximum attributes
            system_1 = System.objects.create(
                system_name='system_1_all_attributes',
                dnsname=dnsname_1,
                domain=domain_1,
                systemstatus=systemstatus_1,
                analysisstatus=analysisstatus_1,
                reason=reason_1,
                recommendation=recommendation_1,
                systemtype=systemtype_1,
                os=os_1,
                location=location_1,
                serviceprovider=serviceprovider_1,
                system_assigned_to_user_id=test_user,
                system_created_by_user_id=test_user,
                system_modified_by_user_id=test_user,
            )

            # add many to many attributes
            system_1.ip.add(ip_1)
            system_1.ip.add(ip_2)
            system_1.ip.add(ip_3)
            system_1.company.add(company_1)
            system_1.company.add(company_2)
            system_1.company.add(company_3)
            system_1.tag.add(tag_1)
            system_1.tag.add(tag_2)
            system_1.tag.add(tag_3)
            system_1.case.add(case_1)
            system_1.case.add(case_2)
            system_1.case.add(case_3)

        # mock timezone.now()
        t_2 = datetime(2009, 8, 17, 16, 15, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_2):

            # create object with minimum attributes
            System.objects.create(
                system_name='system_2_no_attributes',
                systemstatus=systemstatus_1,
                system_created_by_user_id=test_user,
                system_modified_by_user_id=test_user,
            )

        # create object that will not be exported
        System.objects.create(
            system_name='system_3_not_exported',
            systemstatus=systemstatus_1,
            system_export_spreadsheet=False,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_system_exporter_spreadsheet_csv_not_logged_in(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/exporter/spreadsheet/csv/system/', safe=''
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/csv/system/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_exporter_spreadsheet_csv_logged_in(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_csv_redirect(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )
        # create url
        destination = urllib.parse.quote(
            '/system/exporter/spreadsheet/csv/system/', safe='/'
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/csv/system', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_exporter_spreadsheet_csv_minimal_spreadsheet(self):
        """test instant spreadsheet export via button for direct download via browser"""

        """ modify config section """

        # get and modify config to show only mandatory columns
        system_exporter_spreadsheet_csv_config_model = SystemExporterSpreadsheetCsvConfigModel(
            system_exporter_spreadsheet_csv_config_name='SystemExporterSpreadsheetCsvConfig'
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_id = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_dnsname = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_domain = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_systemstatus = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_analysisstatus = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_reason = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_recommendation = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_systemtype = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_ip = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_os = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_company = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_location = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_serviceprovider = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_tag = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_case = False
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_create_time = (
            False
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_modify_time = (
            False
        )
        system_exporter_spreadsheet_csv_config_model.save()

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )

        # mock timezone.now()
        t1_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t1_now):

            # get response
            response = self.client.get('/system/exporter/spreadsheet/csv/system/')

        """ get file section """

        # get bytes object from response content
        csv_browser = response.content
        # decode and split at linebreaks
        csv_browser_decoded = csv_browser.decode('utf-8').split('\n')
        # open systemlist as csv object
        csv_reader = csv.reader(csv_browser_decoded, delimiter=',')

        """ compare values section """

        # compare number of rows
        self.assertEqual(
            len(csv_browser_decoded), 7
        )  # last linebreak leads to additional line because of split
        # TODO: there must be a more convenient way to random access csv cells directly than iterating over lines and switch for line numbers
        # TODO: like with 'xlrd' for xls files for example
        # set counter
        i = 1
        # compare lines
        for csv_line in csv_reader:
            if csv_line:
                if i == 1:
                    self.assertEqual(csv_line[0], 'System')
                elif i == 2:
                    self.assertEqual(csv_line[0], 'system_1_all_attributes')
                elif i == 3:
                    self.assertEqual(csv_line[0], 'system_2_no_attributes')
                elif i == 5:
                    self.assertEqual(csv_line[0], 'Created:')
                    self.assertEqual(csv_line[1], t1_now.strftime('%Y-%m-%d %H:%M'))
                elif i == 6:
                    self.assertEqual(csv_line[0], 'Created by:')
                    self.assertEqual(
                        csv_line[1], 'testuser_system_exporter_spreadsheet_csv'
                    )
            # increase counter
            i += 1

    def test_system_exporter_spreadsheet_csv_complete_spreadsheet(self):
        """test instant spreadsheet export via button for direct download via browser"""

        """ modify config section """

        # get and modify config to show all columns
        system_exporter_spreadsheet_csv_config_model = SystemExporterSpreadsheetCsvConfigModel(
            system_exporter_spreadsheet_csv_config_name='SystemExporterSpreadsheetCsvConfig'
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_id = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_dnsname = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_domain = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_systemstatus = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_analysisstatus = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_reason = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_recommendation = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_systemtype = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_ip = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_os = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_company = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_location = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_serviceprovider = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_tag = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_case = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_assigned_to_user_id = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_create_time = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_created_by_user_id = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_modify_time = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_modified_by_user_id = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.save()

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )

        # mock timezone.now()
        t2_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t2_now):

            # get response
            response = self.client.get('/system/exporter/spreadsheet/csv/system/')

        """ get file section """

        # get bytes object from response content
        csv_browser = response.content
        # decode and split at linebreaks
        csv_decoded = csv_browser.decode('utf-8').split('\n')

        """ test section """

        # test for complete spreadsheet content
        system_exporter_spreadsheet_csv_complete_spreadsheet_check(
            self, csv_decoded, t2_now, 'testuser_system_exporter_spreadsheet_csv', True
        )

    def test_system_exporter_spreadsheet_csv_cron_path_not_existent(self):
        """test spreadsheet export via scheduled task to server file system"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/this_path_does_not_exist'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # create spreadsheet without GET by directly calling the function
        system_cron()

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(response.context['user']), 'testuser_system_exporter_spreadsheet_csv'
        )
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_CSV: Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='3qXjYKBj1CVCakjbCd7A')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_CSV: Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_spreadsheet_csv_cron_path_no_write_permission(self):
        """test spreadsheet export via scheduled task to server file system"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/root'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # create spreadsheet without GET by directly calling the function
        system_cron()

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(response.context['user']), 'testuser_system_exporter_spreadsheet_csv'
        )
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_CSV: No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='3qXjYKBj1CVCakjbCd7A')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_CSV: No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_spreadsheet_csv_cron_complete_spreadsheet(self):
        """test spreadsheet export via scheduled task to server file system"""

        """ modify config section """

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/tmp'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # get and modify config to show all columns
        system_exporter_spreadsheet_csv_config_model = SystemExporterSpreadsheetCsvConfigModel(
            system_exporter_spreadsheet_csv_config_name='SystemExporterSpreadsheetCsvConfig'
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_id = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_dnsname = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_domain = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_systemstatus = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_analysisstatus = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_reason = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_recommendation = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_systemtype = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_ip = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_os = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_company = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_location = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_serviceprovider = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_tag = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_case = True
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_assigned_to_user_id = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_create_time = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_created_by_user_id = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_modify_time = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.spread_csv_system_modified_by_user_id = (
            True
        )
        system_exporter_spreadsheet_csv_config_model.save()

        """ call view section """

        # mock timezone.now()
        t3_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t3_now):

            # create spreadsheet without GET by directly calling the function
            system_cron()

        """ get file section """

        # refresh config
        main_config_model.refresh_from_db()
        # get time for output file
        filetime = t3_now.strftime('%Y%m%d_%H%M')
        # prepare output file path
        output_file_path = (
            main_config_model.cron_export_path + '/' + filetime + '_systems.csv'
        )
        # open file from temp folder
        csv_disk = open(output_file_path)

        """ test section """

        # test for complete spreadsheet content
        system_exporter_spreadsheet_csv_complete_spreadsheet_check(
            self, csv_disk, t3_now, 'cron'
        )

        # close file
        csv_disk.close()

    def test_system_exporter_spreadsheet_csv_create_cron_not_logged_in(self):
        """test helper function to check config before creating scheduled task"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/exporter/spreadsheet/csv/system/cron/', safe=''
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/csv/system/cron/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_exporter_spreadsheet_csv_create_cron_logged_in(self):
        """test helper function to check config before creating scheduled task"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )
        # create url
        destination = urllib.parse.quote(
            '/admin/django_q/schedule/add/?name=system_spreadsheet_exporter_csv&func=dfirtrack_main.exporter.spreadsheet.csv.system_cron',
            safe='/?=&',
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/csv/system/cron/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_exporter_spreadsheet_csv_create_cron_redirect(self):
        """test helper function to check config before creating scheduled task"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )
        # create url
        destination = urllib.parse.quote(
            '/admin/django_q/schedule/add/?name=system_spreadsheet_exporter_csv&func=dfirtrack_main.exporter.spreadsheet.csv.system_cron',
            safe='/?=&',
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/csv/system/cron', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_exporter_spreadsheet_csv_create_cron_path_not_existent(self):
        """test helper function to check config before creating scheduled task"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/this_path_does_not_exist'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )

        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/system/cron/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )
        self.assertEqual(
            messages[0].message,
            'Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_spreadsheet_csv_create_cron_path_no_write_permission(self):
        """test helper function to check config before creating scheduled task"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/root'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_csv',
            password='XJzSzgX2q39OUWluwxoj',
        )

        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/csv/system/cron/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )
        self.assertEqual(
            messages[0].message,
            'No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
