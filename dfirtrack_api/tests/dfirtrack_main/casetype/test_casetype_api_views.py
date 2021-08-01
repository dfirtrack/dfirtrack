import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Casetype


class CasetypeAPIViewTestCase(TestCase):
    """casetype API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Casetype.objects.create(casetype_name='casetype_api_1')
        # create user
        User.objects.create_user(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )

    def test_casetype_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/casetype/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_casetype_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # get response
        response = self.client.get('/api/casetype/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # create POST string
        poststring = {"casetype_name": "casetype_api_2"}
        # get response
        response = self.client.post('/api/casetype/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_casetype_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # create url
        destination = urllib.parse.quote('/api/casetype/', safe='/')
        # get response
        response = self.client.get('/api/casetype', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casetype_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        casetype_api_1 = Casetype.objects.get(casetype_name='casetype_api_1')
        # get response
        response = self.client.get(
            '/api/casetype/' + str(casetype_api_1.casetype_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_casetype_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        casetype_api_1 = Casetype.objects.get(casetype_name='casetype_api_1')
        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # get response
        response = self.client.get(
            '/api/casetype/' + str(casetype_api_1.casetype_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        casetype_api_1 = Casetype.objects.get(casetype_name='casetype_api_1')
        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # get response
        response = self.client.delete(
            '/api/casetype/' + str(casetype_api_1.casetype_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casetype_detail_api_method_put(self):
        """PUT is allowed"""

        # get object
        casetype_api_1 = Casetype.objects.get(casetype_name='casetype_api_1')
        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/casetype/' + str(casetype_api_1.casetype_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {"casetype_name": "new_casetype_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        casetype_api_1 = Casetype.objects.get(casetype_name='casetype_api_1')
        # login testuser
        self.client.login(
            username='testuser_casetype_api', password='xERoxqcrqTqtCK3IrSUx'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/casetype/' + str(casetype_api_1.casetype_id) + '/', safe='/'
        )
        # get response
        response = self.client.get(
            '/api/casetype/' + str(casetype_api_1.casetype_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
