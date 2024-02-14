import urllib.parse
from datetime import datetime
from datetime import timezone as dttimezone

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.models import (
    Case,
    Casepriority,
    Casestatus,
    Casetype,
    Tag,
    Tagcolor,
)


class CaseAPIViewTestCase(TestCase):
    """case API view tests"""

    @classmethod
    def setUpTestData(cls):
        """one time setup"""

        # create user
        test_user = User.objects.create_user(
            username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5'
        )

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')
        casetype_1 = Casetype.objects.create(casetype_name='casetype_1')

        # create object
        Case.objects.create(
            case_name='case_api_1',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            casetype=casetype_1,
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # create object
        Tag.objects.create(
            tagcolor=tagcolor_1,
            tag_name='tag_1',
        )

    def test_case_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/case/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_case_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get response
        response = self.client.get('/api/case/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get user
        test_user_id = str(User.objects.get(username='testuser_case_api').id)
        # get objects
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # create POST string
        poststring = {
            "case_name": "case_api_2",
            "casepriority": casepriority_1.casepriority_id,
            "casestatus": casestatus_1.casestatus_id,
            "casetype": casetype_1.casetype_id,
            "case_is_incident": False,
            "case_created_by_user_id": test_user_id,
        }
        # check for existence of object
        case_api_2_none = Case.objects.filter(case_name='case_api_2')
        # compare
        self.assertEqual(len(case_api_2_none), 0)
        # get response
        response = self.client.post('/api/case/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)
        # get new object
        case_api_2 = Case.objects.get(case_name='case_api_2')
        # compare
        self.assertEqual(case_api_2.casepriority, casepriority_1)
        self.assertEqual(case_api_2.casestatus, casestatus_1)
        self.assertEqual(case_api_2.casetype, casetype_1)
        self.assertEqual(case_api_2.case_is_incident, False)

    def test_case_list_api_method_post_all_id(self):
        """POST is allowed"""

        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get user
        test_user_id = str(User.objects.get(username='testuser_case_api').id)
        # get objects
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create POST string
        poststring = {
            "case_name": "case_api_3",
            "case_id_external": "case_api_3_external",
            "casepriority": casepriority_1.casepriority_id,
            "casestatus": casestatus_1.casestatus_id,
            "casetype": casetype_1.casetype_id,
            "tag": [
                tag_1.tag_id,
            ],
            "case_is_incident": True,
            "case_start_time": '2021-05-09T11:15',
            "case_end_time": '2021-05-09T11:25',
            "case_created_by_user_id": test_user_id,
            "case_modified_by_user_id": test_user_id,
            "case_assigned_to_user_id": test_user_id,
        }
        # check for existence of object
        case_api_3_none = Case.objects.filter(case_name='case_api_3')
        # compare
        self.assertEqual(len(case_api_3_none), 0)
        # get response
        response = self.client.post('/api/case/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)
        # get new object
        case_api_3 = Case.objects.get(case_name='case_api_3')
        # compare
        self.assertEqual(case_api_3.case_id_external, 'case_api_3_external')
        self.assertEqual(case_api_3.casepriority, casepriority_1)
        self.assertEqual(case_api_3.casestatus, casestatus_1)
        self.assertEqual(case_api_3.casetype, casetype_1)
        self.assertTrue(case_api_3.tag.filter(tag_name='tag_1').exists())
        self.assertEqual(
            case_api_3.case_start_time,
            datetime(2021, 5, 9, 11, 15, tzinfo=dttimezone.utc),
        )
        self.assertEqual(
            case_api_3.case_end_time,
            datetime(2021, 5, 9, 11, 25, tzinfo=dttimezone.utc),
        )

    def test_case_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # create url
        destination = urllib.parse.quote('/api/case/', safe='/')
        # get response
        response = self.client.get('/api/case', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        case_api_1 = Case.objects.get(case_name='case_api_1')
        # get response
        response = self.client.get('/api/case/' + str(case_api_1.case_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_case_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        case_api_1 = Case.objects.get(case_name='case_api_1')
        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get response
        response = self.client.get('/api/case/' + str(case_api_1.case_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        case_api_1 = Case.objects.get(case_name='case_api_1')
        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get response
        response = self.client.delete('/api/case/' + str(case_api_1.case_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_case_detail_api_method_put(self):
        """PUT is allowed"""

        # get object
        case_api_1 = Case.objects.get(case_name='case_api_1')
        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get user
        test_user_id = str(User.objects.get(username='testuser_case_api').id)
        # create objects
        casepriority_2 = Casepriority.objects.create(casepriority_name='casepriority_2')
        casestatus_2 = Casestatus.objects.create(casestatus_name='casestatus_2')
        casetype_2 = Casetype.objects.create(casetype_name='casetype_2')
        # create url
        destination = urllib.parse.quote(
            '/api/case/' + str(case_api_1.case_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "case_name": "new_case_api_1",
            "casepriority": casepriority_2.casepriority_id,
            "casestatus": casestatus_2.casestatus_id,
            "casetype": casetype_2.casetype_id,
            "case_is_incident": False,
            "case_created_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get new object
        new_case_api_1 = Case.objects.get(case_name='new_case_api_1')
        # compare
        self.assertEqual(new_case_api_1.casepriority, casepriority_2)
        self.assertEqual(new_case_api_1.casestatus, casestatus_2)
        self.assertEqual(new_case_api_1.casetype, casetype_2)
        self.assertEqual(new_case_api_1.case_is_incident, False)

    def test_case_detail_api_method_put_all_id(self):
        """PUT is allowed"""

        # get object
        case_api_1 = Case.objects.get(case_name='case_api_1')
        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # get user
        test_user_id = str(User.objects.get(username='testuser_case_api').id)
        # create objects
        casepriority_3 = Casepriority.objects.create(casepriority_name='casepriority_3')
        casestatus_3 = Casestatus.objects.create(casestatus_name='casestatus_3')
        casetype_3 = Casetype.objects.create(casetype_name='casetype_3')
        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create url
        destination = urllib.parse.quote(
            '/api/case/' + str(case_api_1.case_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "case_name": "new_case_api_2",
            "case_id_external": "new_case_api_2_external",
            "casepriority": casepriority_3.casepriority_id,
            "casestatus": casestatus_3.casestatus_id,
            "casetype": casetype_3.casetype_id,
            "tag": [
                tag_1.tag_id,
            ],
            "case_is_incident": False,
            "case_start_time": '2021-05-09T11:35',
            "case_end_time": '2021-05-09T11:45',
            "case_created_by_user_id": test_user_id,
            "case_modified_by_user_id": test_user_id,
            "case_assigned_to_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get new object
        new_case_api_2 = Case.objects.get(case_name='new_case_api_2')
        # compare
        self.assertEqual(new_case_api_2.case_id_external, 'new_case_api_2_external')
        self.assertEqual(new_case_api_2.casepriority, casepriority_3)
        self.assertEqual(new_case_api_2.casestatus, casestatus_3)
        self.assertEqual(new_case_api_2.casetype, casetype_3)
        self.assertTrue(new_case_api_2.tag.filter(tag_name='tag_1').exists())
        self.assertEqual(
            new_case_api_2.case_start_time,
            datetime(2021, 5, 9, 11, 35, tzinfo=dttimezone.utc),
        )
        self.assertEqual(
            new_case_api_2.case_end_time,
            datetime(2021, 5, 9, 11, 45, tzinfo=dttimezone.utc),
        )

    def test_case_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        case_api_1 = Case.objects.get(case_name='case_api_1')
        # login testuser
        self.client.login(username='testuser_case_api', password='nkeZDU2qGKXWR49sAVf5')
        # create url
        destination = urllib.parse.quote(
            '/api/case/' + str(case_api_1.case_id) + '/', safe='/'
        )
        # get response
        response = self.client.get('/api/case/' + str(case_api_1.case_id), follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
