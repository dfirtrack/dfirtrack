from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Domain, Domainuser
import urllib.parse

class DomainuserAPIViewTestCase(TestCase):
    """ domainuser API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')

        # create object
        domain_1 = Domain.objects.create(
            domain_name = 'domain_1',
        )

        # create object
        Domainuser.objects.create(
            domainuser_name='domainuser_api_1',
            domainuser_is_domainadmin = True,
            domain = domain_1,
        )

    def test_domainuser_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/domainusers/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_domainuser_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
        # get response
        response = self.client.get('/api/domainusers/')
        # compare
        self.assertEqual(response.status_code, 200)

#    def test_domainuser_list_api_method_post(self):
#        """ POST is allowed """
#
#        # login testuser
#        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
#        # get object
#        domain_id = str(Domain.objects.get(domain_name='domain_1').domain_id)
#        # create POST string
#        poststring = {
#            "domainuser_name": "domainuser_api_2",
#            "domainuser_is_domainadmin": False,
#            "domain": domain_id,
#        }
#        # get response
#        response = self.client.post('/api/domainusers/', data=poststring)
#        # compare
#        self.assertEqual(response.status_code, 201)

    def test_domainuser_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
        # create url
        destination = urllib.parse.quote('/api/domainusers/', safe='/')
        # get response
        response = self.client.get('/api/domainusers', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_domainuser_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
#        # get response
#        response = self.client.get('/api/domainusers/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_domainuser_api')

    def test_domainuser_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        domainuser_api_1 = Domainuser.objects.get(domainuser_name='domainuser_api_1')
        # get response
        response = self.client.get('/api/domainusers/' + str(domainuser_api_1.domainuser_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_domainuser_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        domainuser_api_1 = Domainuser.objects.get(domainuser_name='domainuser_api_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
        # get response
        response = self.client.get('/api/domainusers/' + str(domainuser_api_1.domainuser_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_domainuser_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        domainuser_api_1 = Domainuser.objects.get(domainuser_name='domainuser_api_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
        # get response
        response = self.client.delete('/api/domainusers/' + str(domainuser_api_1.domainuser_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

#    def test_domainuser_detail_api_method_put(self):
#        """ PUT is allowed """
#
#        # get object
#        domainuser_api_1 = Domainuser.objects.get(domainuser_name='domainuser_api_1')
#        # login testuser
#        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
#        # create url
#        destination = urllib.parse.quote('/api/domainusers/' + str(domainuser_api_1.domainuser_id) + '/', safe='/')
#        # create PUT string
#        putstring = {
#            "domainuser_name": "domainuser_api_3",
#            "domainuser_is_domainadmin": False,
#            "domain": domain_id,
#        }
#        # get response
#        response = self.client.put(destination, data=putstring, content_type='application/json')
#        # compare
#        self.assertEqual(response.status_code, 200)

    def test_domainuser_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        domainuser_api_1 = Domainuser.objects.get(domainuser_name='domainuser_api_1')
        # login testuser
        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
        # create url
        destination = urllib.parse.quote('/api/domainusers/' + str(domainuser_api_1.domainuser_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/domainusers/' + str(domainuser_api_1.domainuser_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_domainuser_detail_api_get_user_context(self):
#        """ test user context """
#
#        # get object
#        domainuser_api_1 = Domainuser.objects.get(domainuser_name='domainuser_api_1')
#        # login testuser
#        login = self.client.login(username='testuser_domainuser_api', password='pzJk89y9aQYUkAfwJ5KN')
#        # get response
#        response = self.client.get('/api/domainusers/' + str(domainuser_api_1.domainuser_id) + '/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_domainuser_api')
