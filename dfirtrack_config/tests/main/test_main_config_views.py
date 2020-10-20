from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class MainConfigViewTestCase(TestCase):
    """ main config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_main_config', password='4jl475KM3wof8w5mQ7SN')

    def test_main_config_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/main/', safe='')
        # get response
        response = self.client.get('/config/main/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_config_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_main_config', password='4jl475KM3wof8w5mQ7SN')
        # get response
        response = self.client.get('/config/main/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_main_config_template(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_main_config', password='4jl475KM3wof8w5mQ7SN')
        # get response
        response = self.client.get('/config/main/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/main_config_popup.html')

    def test_main_config_get_user_context(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_main_config', password='4jl475KM3wof8w5mQ7SN')
        # get response
        response = self.client.get('/config/main/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_main_config')

    def test_main_config_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_main_config', password='4jl475KM3wof8w5mQ7SN')
        # create url
        destination = urllib.parse.quote('/config/main/', safe='/')
        # get response
        response = self.client.get('/config/main', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
