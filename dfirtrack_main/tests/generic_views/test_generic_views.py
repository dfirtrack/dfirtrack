from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class GenericViewTestCase(TestCase):
    """ generic view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')

    def test_about_view_not_logged_in(self):
        """ test generic view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/about/', safe='')
        # get response
        response = self.client.get('/about/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_about_view_logged_in(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/about/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_about_view_template(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/about/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/about.html')

    def test_about_view_get_user_context(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/about/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_generic_views')

    def test_about_view_redirect(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # create url
        destination = urllib.parse.quote('/about/', safe='/')
        # get response
        response = self.client.get('/about', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_faq_view_not_logged_in(self):
        """ test generic view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/faq/', safe='')
        # get response
        response = self.client.get('/faq/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_faq_view_logged_in(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/faq/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_faq_view_template(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/faq/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/faq.html')

    def test_faq_view_get_user_context(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/faq/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_generic_views')

    def test_faq_view_redirect(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # create url
        destination = urllib.parse.quote('/faq/', safe='/')
        # get response
        response = self.client.get('/faq', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
