from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class TagAPIViewTestCase(TestCase):
    """ tag API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')

    def test_tag_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/tags/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_tag_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.get('/api/tags/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_list_api_method_post(self):
        """ POST is forbidden """

        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create POST string
        poststring = {"tag_name": "tag_api_1"}
        # get response
        response = self.client.post('/api/tags/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_tag_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/tags/', safe='/')
        # get response
        response = self.client.get('/api/tags', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_tag_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
#        # get response
#        response = self.client.get('/api/tags/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_tag_api')
