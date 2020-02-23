from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import System, Systemstatus
import urllib.parse

class SystemAPIViewTestCase(TestCase):
    """ system API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name = 'system_api_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def test_system_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/systems/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_system_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # get response
        response = self.client.get('/api/systems/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_list_api_method_post(self):
        """ POST is forbidden """

        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # create POST string
        poststring = {"system_name": "system_api_2"}
        # get response
        response = self.client.post('/api/systems/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_system_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # create url
        destination = urllib.parse.quote('/api/systems/', safe='/')
        # get response
        response = self.client.get('/api/systems', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_system_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
#        # get response
#        response = self.client.get('/api/systems/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_system_api')

    def test_system_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # get response
        response = self.client.get('/api/systems/' + str(system_api_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_system_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # get response
        response = self.client.get('/api/systems/' + str(system_api_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # get response
        response = self.client.delete('/api/systems/' + str(system_api_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_system_detail_api_method_put(self):
        """ PUT is forbidden """

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # create url
        destination = urllib.parse.quote('/api/systems/' + str(system_api_1.system_id) + '/', safe='/')
        # create PUT string
        putstring = {"system_name": "new_system_api_1"}
        # get response
        response = self.client.put(destination, data=putstring, content_='application/json')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_system_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
        # create url
        destination = urllib.parse.quote('/api/systems/' + str(system_api_1.system_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/systems/' + str(system_api_1.system_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_system_detail_api_get_user_context(self):
#        """ test user context """
#
#        # get object
#        system_api_1 = System.objects.get(system_name='system_api_1')
#        # login testuser
#        login = self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
#        # get response
#        response = self.client.get('/api/systems/' + str(system_api_1.system_id) + '/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_system_api')
