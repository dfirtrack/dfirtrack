from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Ip
import urllib.parse

class IpAPIViewTestCase(TestCase):
    """ ip API view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Ip.objects.create(ip_ip='127.0.0.1')
        # create user
        test_user = User.objects.create_user(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')

    def test_ip_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/ips/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_ip_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.get('/api/ips/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ip_list_api_method_post(self):
        """ POST is allowed """

        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create POST string
        poststring = {"ip_ip": "127.0.0.2"}
        # get response
        response = self.client.post('/api/ips/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_ip_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/ips/', safe='/')
        # get response
        response = self.client.get('/api/ips', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_ip_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        ip_api_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # get response
        response = self.client.get('/api/ips/' + str(ip_api_1.ip_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_ip_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        ip_api_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.get('/api/ips/' + str(ip_api_1.ip_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ip_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        ip_api_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.delete('/api/ips/' + str(ip_api_1.ip_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_ip_detail_api_method_put(self):
        """ PUT is allowed """

        # get object
        ip_api_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/ips/' + str(ip_api_1.ip_id) + '/', safe='/')
        # create PUT string
        putstring = {"ip_ip": "127.0.0.3"}
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ip_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        ip_api_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/ips/' + str(ip_api_1.ip_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/ips/' + str(ip_api_1.ip_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
