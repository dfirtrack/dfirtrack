import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Casepriority


class CasepriorityViewTestCase(TestCase):
    """casepriority view tests"""

    @classmethod
    def setUpTestData(cls):
        # create object
        Casepriority.objects.create(casepriority_name='casepriority_1')
        # create user
        User.objects.create_user(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )

    def test_casepriority_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/casepriority/', safe='')
        # get response
        response = self.client.get('/casepriority/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casepriority_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # get response
        response = self.client.get('/casepriority/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casepriority_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # get response
        response = self.client.get('/casepriority/')
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/casepriority/casepriority_list.html'
        )

    def test_casepriority_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # get response
        response = self.client.get('/casepriority/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_casepriority')

    def test_casepriority_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # create url
        destination = urllib.parse.quote('/casepriority/', safe='/')
        # get response
        response = self.client.get('/casepriority', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casepriority_detail_not_logged_in(self):
        """test detail view"""

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id) + '/', safe=''
        )
        # get response
        response = self.client.get(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id) + '/',
            follow=True,
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casepriority_detail_logged_in(self):
        """test detail view"""

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # get response
        response = self.client.get(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casepriority_detail_template(self):
        """test detail view"""

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # get response
        response = self.client.get(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id) + '/'
        )
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/casepriority/casepriority_detail.html'
        )

    def test_casepriority_detail_get_user_context(self):
        """test detail view"""

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # get response
        response = self.client.get(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id) + '/'
        )
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_casepriority')

    def test_casepriority_detail_redirect(self):
        """test list view"""

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # login testuser
        self.client.login(
            username='testuser_casepriority', password='tRiCVI2mf531CLw7r6jQ'
        )
        # create url
        destination = urllib.parse.quote(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id) + '/',
            safe='/',
        )
        # get response
        response = self.client.get(
            '/casepriority/detail/' + str(casepriority_1.casepriority_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
