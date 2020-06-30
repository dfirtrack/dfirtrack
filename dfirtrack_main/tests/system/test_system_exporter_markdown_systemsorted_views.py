from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterMarkdownSystemsortedViewTestCase(TestCase):
    """ system exporter markdown systemsorted view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_markdown_systemsorted', password='2anJuuSjzjLmb2pOYuLf')

    def test_system_exporter_markdown_systemsorted_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/systemsorted/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/systemsorted/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_systemsorted_logged_in(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_systemsorted', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/systemsorted/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_systemsorted_redirect(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_systemsorted', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/systemsorted', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
