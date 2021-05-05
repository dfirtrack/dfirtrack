from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from dfirtrack_config.models import MainConfigModel
import urllib.parse


def set_main_overview(main_overview):
    """ change config """

    model = MainConfigModel.objects.get(main_config_name='MainConfig')
    model.main_overview = f'main_overview_{main_overview}'
    model.save()

    # return to test function
    return

class MainOverviewViewTestCase(TestCase):
    """ main overview view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')

    def test_main_overview_not_logged_in(self):
        """ test main overview """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/main_overview/', safe='')
        # get response
        response = self.client.get('/main_overview/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_system_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('system')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/system/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_artifact_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('artifact')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_case_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('case')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/case/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_status_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('status')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/config/status/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_tag_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('tag')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/tag/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_task_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('task')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/task/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_main_overview_default_url(self):
        """ test main overview url and redirect """

        # change config
        set_main_overview('foobar')

        # login testuser
        self.client.login(username='testuser_main_overview', password='RYgxCfV2NRcfXlJvsSHP')
        # get reverse url
        url = reverse('main_overview')
        # compare url
        self.assertEqual(url, '/main_overview/')
        # create url
        destination = urllib.parse.quote('/system/')
        # get response
        response = self.client.get('/main_overview/')
        # compare redirect
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
