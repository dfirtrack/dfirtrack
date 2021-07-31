from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Analysisstatus
from dfirtrack_main.models import Case
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor
import datetime
import json
import pytz
import urllib.parse


class SystemDatatablesProcessingTestCase(TestCase):
    """ system datatables (server-side) processing tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system', password='LqShcoecDud6JLRxhfKV')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.create(systemstatus_name='systemstatus_2')

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        tag_1 = Tag.objects.create(
            tag_name = 'tag_1',
            tagcolor = tagcolor_1,
        )

        # create object
        case_1 = Case.objects.create(
            case_name = 'case_1',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )

        # create object
        analysisstatus_1 = Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            analysisstatus = analysisstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_1.case.add(case_1)
        system_1.tag.add(tag_1)

        # create object
        System.objects.create(
            system_name = 'system_2',
            systemstatus = systemstatus_2,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        system_3 = System.objects.create(
            system_name = 'system_3',
            systemstatus = systemstatus_1,
            analysisstatus = analysisstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_3.case.add(case_1)
        system_3.tag.add(tag_1)

        # create object
        mod_time_naive = datetime.datetime(2021, 1, 17, 13, 39, 29, 35025)
        mod_time_tz = mod_time_naive.replace(tzinfo=pytz.timezone("GMT"))
        System.objects.create(
            system_name = 'system_4',
            systemstatus = systemstatus_2,
            system_modify_time = mod_time_tz,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # create object
        System.objects.create(
            system_name = 'system_5',
            systemstatus = systemstatus_2,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # create object
        System.objects.create(
            system_name = 'system_6',
            systemstatus = systemstatus_2,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def test_dt_processing_not_logged_in(self):
        """ test system datatables processing """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/json/', safe='')
        # get response
        response = self.client.get('/system/json/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_dt_processing_logged_in(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_dt_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_1', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 1)
        self.assertTrue('system_1' in data['data'][0]['system_name'])

    def test_dt_no_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 6)
        self.assertTrue(len(data['data']) == 6)

    def test_dt_search_irregular_string(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_1!', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 6)

    def test_dt_referer_systemstatus_wo_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER=f'/systemstatus/{systemstatus_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 2)
        self.assertTrue('system_1' in data['data'][0]['system_name'] or 'system_1' in data['data'][1]['system_name'])

    def test_dt_referer_systemstatus_w_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_1', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER=f'/systemstatus/{systemstatus_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 1)
        self.assertTrue('system_1' in data['data'][0]['system_name'])

    def test_dt_referer_case_wo_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        case_id = Case.objects.get(case_name='case_1').case_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER=f'/case/{case_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 2)
        self.assertTrue('system_1' in data['data'][0]['system_name'] or 'system_1' in data['data'][1]['system_name'])

    def test_dt_referer_case_w_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        case_id = Case.objects.get(case_name='case_1').case_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_1', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER=f'/case/{case_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 1)
        self.assertTrue('system_1' in data['data'][0]['system_name'])

    def test_dt_referer_analysisstatus_wo_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1').analysisstatus_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER=f'/analysisstatus/{analysisstatus_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 2)
        self.assertTrue('system_1' in data['data'][0]['system_name'] or 'system_1' in data['data'][1]['system_name'])

    def test_dt_referer_analysisstatus_w_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1').analysisstatus_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_1', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER=f'/analysisstatus/{analysisstatus_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 1)
        self.assertTrue('system_1' in data['data'][0]['system_name'])

    def test_dt_referer_tag_wo_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        tag_id = Tag.objects.get(tag_name='tag_1').tag_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus', 'draw': '1'}, HTTP_REFERER=f'/tag/{tag_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 2)
        self.assertTrue('system_1' in data['data'][0]['system_name'] or 'system_1' in data['data'][1]['system_name'])

    def test_dt_referer_tag_w_search(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get data
        tag_id = Tag.objects.get(tag_name='tag_1').tag_id
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_1', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus', 'draw': '1'}, HTTP_REFERER=f'/tag/{tag_id}/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 1)
        self.assertTrue('system_1' in data['data'][0]['system_name'])

    def test_dt_search_cleanup(self):
        """ test system datatables processing """
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '35025', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus', 'draw': '1'}, HTTP_REFERER='/system/')
        data = json.loads(response.content)
        # compare
        self.assertEqual(int(data['recordsFiltered']), 0)
