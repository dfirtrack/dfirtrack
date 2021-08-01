import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Casestatus


class CasestatusViewTestCase(TestCase):
    """ casestatus view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Casestatus.objects.create(casestatus_name='casestatus_1')
        # create user
        User.objects.create_user(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')

    def test_casestatus_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/casestatus/', safe='')
        # get response
        response = self.client.get('/casestatus/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_casestatus_list_logged_in(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # get response
        response = self.client.get('/casestatus/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casestatus_list_template(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # get response
        response = self.client.get('/casestatus/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/casestatus/casestatus_list.html')

    def test_casestatus_list_get_user_context(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # get response
        response = self.client.get('/casestatus/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_casestatus')

    def test_casestatus_list_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # create url
        destination = urllib.parse.quote('/casestatus/', safe='/')
        # get response
        response = self.client.get('/casestatus', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_casestatus_detail_not_logged_in(self):
        """ test detail view """

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/casestatus/detail/' + str(casestatus_1.casestatus_id) + '/', safe='')
        # get response
        response = self.client.get('/casestatus/detail/' + str(casestatus_1.casestatus_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_casestatus_detail_logged_in(self):
        """ test detail view """

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # get response
        response = self.client.get('/casestatus/detail/' + str(casestatus_1.casestatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casestatus_detail_template(self):
        """ test detail view """

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # get response
        response = self.client.get('/casestatus/detail/' + str(casestatus_1.casestatus_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/casestatus/casestatus_detail.html')

    def test_casestatus_detail_get_user_context(self):
        """ test detail view """

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # get response
        response = self.client.get('/casestatus/detail/' + str(casestatus_1.casestatus_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_casestatus')

    def test_casestatus_detail_redirect(self):
        """ test list view """

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # login testuser
        self.client.login(username='testuser_casestatus', password='6imkOwOYEjWv5TnOzjQ1')
        # create url
        destination = urllib.parse.quote('/casestatus/detail/' + str(casestatus_1.casestatus_id) + '/', safe='/')
        # get response
        response = self.client.get('/casestatus/detail/' + str(casestatus_1.casestatus_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
