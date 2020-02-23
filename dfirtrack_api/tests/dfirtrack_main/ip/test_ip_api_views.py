from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class IpAPIViewTestCase(TestCase):
    """ ip API view tests """

    @classmethod
    def setUpTestData(cls):

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
        poststring = {"ip_ip": "127.0.0.1"}
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

#    def test_ip_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_ip_api', password='2SxcYh8yo3rGs4PBqhg9')
#        # get response
#        response = self.client.get('/api/ips/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_ip_api')
