from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemModificatorViewTestCase(TestCase):
    """ system modificator view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G')

    def test_system_modificator_not_logged_in(self):
        """ test modificator view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/modificator/', safe='')
        # get response
        response = self.client.get('/system/modificator/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_modificator_logged_in(self):
        """ test modificator view """

        # login testuser
        login = self.client.login(username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G')
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_modificator_template(self):
        """ test modificator view """

        # login testuser
        login = self.client.login(username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G')
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_modificator.html')

    def test_system_modificator_get_user_context(self):
        """ test modificator view """

        # login testuser
        login = self.client.login(username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G')
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_modificator')

    def test_system_modificator_redirect(self):
        """ test modificator view """

        # login testuser
        login = self.client.login(username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G')
        # create url
        destination = urllib.parse.quote('/system/modificator/', safe='/')
        # get response
        response = self.client.get('/system/modificator', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
