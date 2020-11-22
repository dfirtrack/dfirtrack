from dfirtrack_config.models import Statushistory
from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class StatushistoryViewTestCase(TestCase):
    """ statushistory view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')

    def test_statushistory_save_view_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/statushistory/save/', safe='')
        # get response
        response = self.client.get('/config/statushistory/save/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_statushistory_save_view_logged_in(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')
        # get response
        response = self.client.get('/config/statushistory/save/')
        # create url
        destination = '/status/'
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_statushistory_save_view_redirect(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')
        # create url
        destination = '/status/'
        # get response
        response = self.client.get('/config/statushistory/save', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_statushistory_save_view_complate(self):
        """ test view """

        pass
        # TODO: test values submitted to database analogous to
        # 'test_status_view_get_object_context' in 'dfirtrack_main.tests.generic_views.test_generic_views'
