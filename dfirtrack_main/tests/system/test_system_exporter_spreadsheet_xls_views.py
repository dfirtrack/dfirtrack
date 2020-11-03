from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_config.models import SystemExporterSpreadsheetXlsConfigModel
from dfirtrack_main.models import System, Systemstatus
from mock import patch
import urllib.parse
import xlrd

class SystemExporterSpreadsheetXlsViewTestCase(TestCase):
    """ system exporter spreadsheet XLS view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        """ create systems """

        # mock timezone.now()
        t_1 = datetime(2001, 2, 3, 4, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # create object with maximum attributes
            System.objects.create(
                system_name='system_1_all_attributes',
                systemstatus = systemstatus_1,
                system_modify_time = timezone.now(),
                system_created_by_user_id = test_user,
                system_modified_by_user_id = test_user,
            )

        # mock timezone.now()
        t_2 = datetime(2009, 8, 7, 6, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_2):

            # create object with minimum attributes
            System.objects.create(
                system_name='system_2_no_attributes',
                systemstatus = systemstatus_1,
                system_modify_time = timezone.now(),
                system_created_by_user_id = test_user,
                system_modified_by_user_id = test_user,
            )

        # create object that will not be exported
        System.objects.create(
            system_name='system_3_not_exported',
            systemstatus = systemstatus_1,
            system_export_spreadsheet = False,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def test_system_exporter_spreadsheet_xls_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/spreadsheet/xls/system/', safe='')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_logged_in(self):
        """ test exporter view """

        # login testuser
        self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_xls_redirect(self):
        """ test exporter view """

        # login testuser
        self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
        # create url
        destination = urllib.parse.quote('/system/exporter/spreadsheet/xls/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/spreadsheet/xls/system', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_exporter_spreadsheet_xls_minimal_spreadsheet(self):
        """ test exporter view """

        # mock timezone.now()
        t1_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t1_now):

            # get and modify config to show only mandatory columns
            system_exporter_spreadsheet_xls_config_model = SystemExporterSpreadsheetXlsConfigModel(system_exporter_spreadsheet_xls_config_name = 'SystemExporterSpreadsheetXlsConfig')
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
            system_exporter_spreadsheet_xls_config_model.spread_xls_system_create_time = False
            system_exporter_spreadsheet_xls_config_model.spread_xls_system_modify_time = False
            system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_systemstatus = False
            system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_analysisstatus = False
            system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_reason = False
            system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_recommendation = False
            system_exporter_spreadsheet_xls_config_model.spread_xls_worksheet_tag = False
            system_exporter_spreadsheet_xls_config_model.save()
            # login testuser
            self.client.login(username='testuser_system_exporter_spreadsheet_xls', password='AIsOtQ2zchYhNZBfWIHu')
            # get objects
            system_1 = System.objects.get(system_name='system_1_all_attributes')
            system_2 = System.objects.get(system_name='system_2_no_attributes')
            # get response
            response = self.client.get('/system/exporter/spreadsheet/xls/system/')
            # get systemlist from response content
            workbook = response.content
            # open systemlist directly from byte stream
            systemlist = xlrd.open_workbook(file_contents=workbook)
            # get sheets
            sheet_systems = systemlist.sheet_by_name('systems')
            # compare number of rows and columns
            self.assertEqual(sheet_systems.nrows, 6)
            self.assertEqual(sheet_systems.ncols, 2)
            # compare headlines
            self.assertEqual(sheet_systems.row_values(0), ['System', ''])
            # compare content - system 1
            self.assertEqual(sheet_systems.cell(1,0).value, system_1.system_name)
            # compare content - system 2
            self.assertEqual(sheet_systems.cell(2,0).value, system_2.system_name)
            # compare content - metadata
            self.assertEqual(sheet_systems.cell(4,0).value, 'SOD created:')
            self.assertEqual(sheet_systems.cell(4,1).value,  t1_now.strftime('%Y-%m-%d %H:%M'))
            self.assertEqual(sheet_systems.cell(5,0).value, 'Created by:')
            self.assertEqual(sheet_systems.cell(5,1).value, 'testuser_system_exporter_spreadsheet_xls')
