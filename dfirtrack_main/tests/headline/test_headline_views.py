from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Headline
import urllib.parse

class HeadlineViewTestCase(TestCase):
    """ headline view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Headline.objects.create(headline_name='headline_1')
        # create user
        test_user = User.objects.create_user(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')

    def test_headlines_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/headlines/', safe='')
        # get response
        response = self.client.get('/headlines/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_headlines_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headlines_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/headline/headlines_list.html')

    def test_headlines_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_headline')

    def test_headlines_detail_not_logged_in(self):
        """ test detail view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/headlines/' + str(headline_1.headline_id), safe='')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_headlines_detail_logged_in(self):
        """ test detail view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headlines_detail_template(self):
        """ test detail view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/headline/headlines_detail.html')

    def test_headlines_detail_get_user_context(self):
        """ test detail view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_headline')

    def test_headlines_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/headlines/add/', safe='')
        # get response
        response = self.client.get('/headlines/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_headlines_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headlines_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/headline/headlines_add.html')

    def test_headlines_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_headline')

    def test_headlines_edit_not_logged_in(self):
        """ test edit view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/headlines/' + str(headline_1.headline_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_headlines_edit_logged_in(self):
        """ test edit view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headlines_edit_template(self):
        """ test edit view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/headline/headlines_edit.html')

    def test_headlines_edit_get_user_context(self):
        """ test edit view """

        # get object
        headline_1 = Headline.objects.get(headline_name='headline_1')
        # login testuser
        login = self.client.login(username='testuser_headline', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/headlines/' + str(headline_1.headline_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_headline')
