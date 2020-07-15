from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterMarkdownViewTestCase(TestCase):
    """ system exporter markdown view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')

    def test_system_exporter_markdown_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/system/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_logged_in(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_redirect(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_exporter_markdown_config_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/config/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/config/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_config_template(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/exporter/markdown/config/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_exporter_markdown_config_popup.html')

    def test_system_exporter_markdown_config_get_user_context(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/exporter/markdown/config/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_markdown')
