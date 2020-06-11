from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Domain
import urllib.parse

class DomainViewTestCase(TestCase):
    """ domain view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Domain.objects.create(domain_name='domain_1')
        # create user
        test_user = User.objects.create_user(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')

    def test_domain_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domain/', safe='')
        # get response
        response = self.client.get('/domain/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domain_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domain_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domain_list.html')

    def test_domain_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domain_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/domain/', safe='/')
        # get response
        response = self.client.get('/domain', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_domain_detail_not_logged_in(self):
        """ test detail view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domain/' + str(domain_1.domain_id) + '/', safe='')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domain_detail_logged_in(self):
        """ test detail view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domain_detail_template(self):
        """ test detail view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domain_detail.html')

    def test_domain_detail_get_user_context(self):
        """ test detail view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domain_detail_redirect(self):
        """ test detail view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/domain/' + str(domain_1.domain_id) + '/', safe='/')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_domain_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domain/add/', safe='')
        # get response
        response = self.client.get('/domain/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domain_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domain_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domain_add.html')

    def test_domain_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domain_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/domain/add/', safe='/')
        # get response
        response = self.client.get('/domain/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_domain_edit_not_logged_in(self):
        """ test edit view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domain/' + str(domain_1.domain_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domain_edit_logged_in(self):
        """ test edit view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domain_edit_template(self):
        """ test edit view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domain_edit.html')

    def test_domain_edit_get_user_context(self):
        """ test edit view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domain_edit_redirect(self):
        """ test edit view """

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # create url
        destination = urllib.parse.quote('/domain/' + str(domain_1.domain_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/domain/' + str(domain_1.domain_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
