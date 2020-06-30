from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterMarkdownDomainsortedViewTestCase(TestCase):
    """ system view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_markdown_domainsorted', password='2bUTySfR8GpEsvFSi64a')

    def test_system_exporter_markdown_domainsorted_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/domainsorted/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/domainsorted/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_domainsorted_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_domainsorted', password='2bUTySfR8GpEsvFSi64a')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/domainsorted/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_domainsorted_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_markdown_domainsorted', password='2bUTySfR8GpEsvFSi64a')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/domainsorted', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
