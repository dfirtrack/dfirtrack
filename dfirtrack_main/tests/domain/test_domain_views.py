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

    def test_domains_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domains/', safe='')
        # get response
        response = self.client.get('/domains/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domains_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domains_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domains_list.html')

    def test_domains_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domains_detail_not_logged_in(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domains/' + str(domain_1.domain_id), safe='')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domains_detail_logged_in(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domains_detail_template(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domains_detail.html')

    def test_domains_detail_get_user_context(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domains_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domains/add/', safe='')
        # get response
        response = self.client.get('/domains/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domains_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domains_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domains_add.html')

    def test_domains_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')

    def test_domains_edit_not_logged_in(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domains/' + str(domain_1.domain_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domains_edit_logged_in(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domains_edit_template(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domain/domains_edit.html')

    def test_domains_edit_get_user_context(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # login testuser
        login = self.client.login(username='testuser_domain', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/domains/' + str(domain_1.domain_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domain')
