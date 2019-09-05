from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Domain, Domainuser
import urllib.parse

class DomainuserViewTestCase(TestCase):
    """ domainuser view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')

        # create object
        domain_1 = Domain.objects.create(
            domain_name='domain_1',
        )

        # create object
        Domainuser.objects.create(domainuser_name='domainuser_1', domain = domain_1)

    def test_domainusers_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domainusers/', safe='')
        # get response
        response = self.client.get('/domainusers/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domainusers_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domainusers_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domainuser/domainusers_list.html')

    def test_domainusers_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domainuser')

    def test_domainusers_detail_not_logged_in(self):
        """ test detail view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domainusers/' + str(domainuser_1.domainuser_id), safe='')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domainusers_detail_logged_in(self):
        """ test detail view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domainusers_detail_template(self):
        """ test detail view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domainuser/domainusers_detail.html')

    def test_domainusers_detail_get_user_context(self):
        """ test detail view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domainuser')

    def test_domainusers_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domainusers/add/', safe='')
        # get response
        response = self.client.get('/domainusers/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domainusers_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domainusers_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domainuser/domainusers_add.html')

    def test_domainusers_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domainuser')

    def test_domainusers_edit_not_logged_in(self):
        """ test edit view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/domainusers/' + str(domainuser_1.domainuser_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_domainusers_edit_logged_in(self):
        """ test edit view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domainusers_edit_template(self):
        """ test edit view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/domainuser/domainusers_edit.html')

    def test_domainusers_edit_get_user_context(self):
        """ test edit view """

        # get object
        domainuser_1 = Domainuser.objects.get(domainuser_name='domainuser_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser', password='8fcseQ9rXyG9vNaoECnq')
        # get response
        response = self.client.get('/domainusers/' + str(domainuser_1.domainuser_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_domainuser')
