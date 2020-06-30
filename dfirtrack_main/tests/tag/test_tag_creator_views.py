from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class TagCreatorViewTestCase(TestCase):
    """ tag creator view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_tag_creator', password='X4zm4Em28xrKgVMBpsWF')

    def test_tag_creator_not_logged_in(self):
        """ test creator view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tag/creator/', safe='')
        # get response
        response = self.client.get('/tag/creator/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tag_creator_logged_in(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_tag_creator', password='X4zm4Em28xrKgVMBpsWF')
        # get response
        response = self.client.get('/tag/creator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_creator_template(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_tag_creator', password='X4zm4Em28xrKgVMBpsWF')
        # get response
        response = self.client.get('/tag/creator/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/tag/tag_creator.html')

    def test_tag_creator_get_user_context(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_tag_creator', password='X4zm4Em28xrKgVMBpsWF')
        # get response
        response = self.client.get('/tag/creator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_tag_creator')

    def test_tag_creator_redirect(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_tag_creator', password='X4zm4Em28xrKgVMBpsWF')
        # create url
        destination = urllib.parse.quote('/tag/creator/', safe='/')
        # get response
        response = self.client.get('/tag/creator', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
