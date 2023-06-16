import urllib.parse
from datetime import datetime
from unittest.mock import patch

import xlrd
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone

from dfirtrack_config.models import (
    MainConfigModel,
    SystemExporterSpreadsheetXlsConfigModel,
)
from dfirtrack_main.exporter.spreadsheet.xls import system_cron
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
from dfirtrack_main.tests.system.system_exporter_spreadsheet_xls_shared_checks import (
    system_exporter_spreadsheet_xls_complete_spreadsheet_check,
)


class SystemExporterSpreadsheetXlsViewTestCase(TestCase):
    """system exporter spreadsheet XLS view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_system_exporter_spreadsheet_xls',
            is_staff=True,
            is_superuser=True,
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        User.objects.create_user(
            username='message_user', password='qbldDxAdkR5rbKQ1WHMW'
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
        t_1 = datetime(2001, 2, 3, 4, 5, tzinfo=timezone.utc)
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
        t_2 = datetime(2009, 8, 7, 6, 5, tzinfo=timezone.utc)
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

    def test_system_exporter_spreadsheet_xls_not_logged_in(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/exporter/spreadsheet/xls/system/', safe=''
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/xls/system/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_exporter_spreadsheet_xls_logged_in(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_xls_redirect(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        # create url
        destination = urllib.parse.quote(
            '/system/exporter/spreadsheet/xls/system/', safe='/'
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/xls/system', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_exporter_spreadsheet_xls_minimal_spreadsheet(self):
        """test instant spreadsheet export via button for direct download via browser"""

        """ modify config section """

        # get and modify config to show only mandatory columns
        system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel(
            system_exporter_spreadsheet_xls_config_name='SystemExporterSpreadsheetXlsConfig'
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_id = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_dnsname = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_domain = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_systemstatus = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_analysisstatus = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_reason = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_recommendation = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_systemtype = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_ip = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_os = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_company = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_location = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_serviceprovider = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_tag = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_case = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_create_time = (
            False
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_modify_time = (
            False
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_systemstatus = (
            False
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_analysisstatus = (
            False
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_reason = False
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_recommendation = (
            False
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_tag = False
        system_exporter_spreadsheet_xls_config_model.save()

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )

        # mock timezone.now()
        t1_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t1_now):
            # get response
            response = self.client.get('/system/exporter/spreadsheet/xls/system/')

        """ get file section """

        # get file from response content
        xls_browser = response.content
        # open systemlist directly from byte stream
        systemlist = xlrd.open_workbook(file_contents=xls_browser)

        """ prepare objects section """

        # get objects
        system_1 = System.objects.get(system_name='system_1_all_attributes')
        system_2 = System.objects.get(system_name='system_2_no_attributes')

        # get sheets
        sheet_systems = systemlist.sheet_by_name('systems')

        """ compare values section """

        # compare non-available sheets
        self.assertRaises(
            xlrd.biffh.XLRDError, systemlist.sheet_by_name, sheet_name='systemstatus'
        )
        self.assertRaises(
            xlrd.biffh.XLRDError, systemlist.sheet_by_name, sheet_name='analysisstatus'
        )
        self.assertRaises(
            xlrd.biffh.XLRDError, systemlist.sheet_by_name, sheet_name='reasons'
        )
        self.assertRaises(
            xlrd.biffh.XLRDError, systemlist.sheet_by_name, sheet_name='recommendations'
        )
        self.assertRaises(
            xlrd.biffh.XLRDError, systemlist.sheet_by_name, sheet_name='tags'
        )
        # compare number of rows and columns
        self.assertEqual(sheet_systems.nrows, 6)
        self.assertEqual(sheet_systems.ncols, 2)
        # compare headlines
        self.assertEqual(sheet_systems.row_values(0), ['System', ''])
        # compare content - system 1
        self.assertEqual(sheet_systems.cell(1, 0).value, system_1.system_name)
        # compare content - system 2
        self.assertEqual(sheet_systems.cell(2, 0).value, system_2.system_name)
        # compare content - metadata
        self.assertEqual(sheet_systems.cell(4, 0).value, 'Created:')
        self.assertEqual(
            sheet_systems.cell(4, 1).value, t1_now.strftime('%Y-%m-%d %H:%M')
        )
        self.assertEqual(sheet_systems.cell(5, 0).value, 'Created by:')
        self.assertEqual(
            sheet_systems.cell(5, 1).value, 'testuser_system_exporter_spreadsheet_xls'
        )

    def test_system_exporter_spreadsheet_xls_complete_spreadsheet(self):
        """test instant spreadsheet export via button for direct download via browser"""

        """ modify config section """

        # get and modify config to show all columns and sheets
        system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel(
            system_exporter_spreadsheet_xls_config_name='SystemExporterSpreadsheetXlsConfig'
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_id = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_dnsname = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_domain = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_systemstatus = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_analysisstatus = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_reason = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_recommendation = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_systemtype = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_ip = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_os = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_company = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_location = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_serviceprovider = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_tag = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_case = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_assigned_to_user_id = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_create_time = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_created_by_user_id = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_modify_time = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_modified_by_user_id = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_systemstatus = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_analysisstatus = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_reason = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_recommendation = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_tag = True
        system_exporter_spreadsheet_xls_config_model.save()

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )

        # mock timezone.now()
        t2_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t2_now):
            # get response
            response = self.client.get('/system/exporter/spreadsheet/xls/system/')

        """ get file section """

        # get file from response content
        xls_browser = response.content
        # open systemlist directly from byte stream
        systemlist = xlrd.open_workbook(file_contents=xls_browser)

        """ test section """

        # test for complete spreadsheet content
        system_exporter_spreadsheet_xls_complete_spreadsheet_check(
            self, systemlist, t2_now, 'testuser_system_exporter_spreadsheet_xls'
        )

    def test_system_exporter_spreadsheet_xls_cron_path_not_existent(self):
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
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(response.context['user']), 'testuser_system_exporter_spreadsheet_xls'
        )
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_XLS: Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='qbldDxAdkR5rbKQ1WHMW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_XLS: Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_spreadsheet_xls_cron_path_no_write_permission(self):
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
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(response.context['user']), 'testuser_system_exporter_spreadsheet_xls'
        )
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_XLS: No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='qbldDxAdkR5rbKQ1WHMW')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] SYSTEM_XLS: No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_spreadsheet_xls_cron_complete_spreadsheet(self):
        """test spreadsheet export via scheduled task to server file system"""

        """ modify config section """

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/tmp'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # get and modify config to show all columns and sheets
        system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel(
            system_exporter_spreadsheet_xls_config_name='SystemExporterSpreadsheetXlsConfig'
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_id = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_dnsname = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_domain = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_systemstatus = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_analysisstatus = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_reason = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_recommendation = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_systemtype = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_ip = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_os = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_company = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_location = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_serviceprovider = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_tag = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_case = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_assigned_to_user_id = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_create_time = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_created_by_user_id = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_modify_time = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_system_modified_by_user_id = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_systemstatus = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_analysisstatus = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_reason = True
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_recommendation = (
            True
        )
        system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_tag = True
        system_exporter_spreadsheet_xls_config_model.save()

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
            main_config_model.cron_export_path + '/' + filetime + '_systems.xls'
        )
        # open file from temp folder
        xls_disk = xlrd.open_workbook(output_file_path)

        """ test section """

        # test for complete spreadsheet content
        system_exporter_spreadsheet_xls_complete_spreadsheet_check(
            self, xls_disk, t3_now, 'cron'
        )

    def test_system_exporter_spreadsheet_xls_create_cron_not_logged_in(self):
        """test helper function to check config before creating scheduled task"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/exporter/spreadsheet/xls/system/cron/', safe=''
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/xls/system/cron/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_exporter_spreadsheet_xls_create_cron_logged_in(self):
        """test helper function to check config before creating scheduled task"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        # create url
        destination = urllib.parse.quote(
            '/admin/django_q/schedule/add/?name=system_spreadsheet_exporter_xls&func=dfirtrack_main.exporter.spreadsheet.xls.system_cron',
            safe='/?=&',
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/xls/system/cron/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_exporter_spreadsheet_xls_create_cron_redirect(self):
        """test helper function to check config before creating scheduled task"""

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )
        # create url
        destination = urllib.parse.quote(
            '/admin/django_q/schedule/add/?name=system_spreadsheet_exporter_xls&func=dfirtrack_main.exporter.spreadsheet.xls.system_cron',
            safe='/?=&',
        )
        # get response
        response = self.client.get(
            '/system/exporter/spreadsheet/xls/system/cron', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_exporter_spreadsheet_xls_create_cron_path_not_existent(self):
        """test helper function to check config before creating scheduled task"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/this_path_does_not_exist'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )

        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/cron/')
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

    def test_system_exporter_spreadsheet_xls_create_cron_path_no_write_permission(self):
        """test helper function to check config before creating scheduled task"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/root'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # login testuser
        self.client.login(
            username='testuser_system_exporter_spreadsheet_xls',
            password='AIsOtQ2zchYhNZBfWIHu',
        )

        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/cron/')
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
