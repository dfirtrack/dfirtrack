from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterMarkdownConfigViewTestCase(TestCase):
    """ system exporter markdown config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_markdown_config', password='Rg6YK8f9LSlIY4yaBDxS')

    def test_system_exporter_markdown_config_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/config/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_config_logged_in(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_config', password='Rg6YK8f9LSlIY4yaBDxS')
        # get response
        response = self.client.get('/system/exporter/markdown/config/', follow=True)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_markdown_config_template(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_config', password='Rg6YK8f9LSlIY4yaBDxS')
        # get response
        response = self.client.get('/system/exporter/markdown/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_exporter_markdown_config_popup.html')

    def test_system_exporter_markdown_config_get_user_context(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_config', password='Rg6YK8f9LSlIY4yaBDxS')
        # get response
        response = self.client.get('/system/exporter/markdown/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_markdown_config')

    def test_system_exporter_markdown_config_redirect(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_config', password='Rg6YK8f9LSlIY4yaBDxS')
        # create url
        destination = urllib.parse.quote('/system/exporter/markdown/config/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/config', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
