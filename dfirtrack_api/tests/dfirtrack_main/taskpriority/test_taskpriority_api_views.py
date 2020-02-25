from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Taskpriority
import urllib.parse

class TaskpriorityAPIViewTestCase(TestCase):
    """ taskpriority API view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskpriority.objects.create(taskpriority_name='tp_1')
        # create user
        test_user = User.objects.create_user(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')

    def test_taskpriority_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/taskprioritys/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_taskpriority_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # get response
        response = self.client.get('/api/taskprioritys/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskpriority_list_api_method_post(self):
        """ POST is forbidden """

        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # create POST string
        poststring = {"taskpriority_name": "tp_2"}
        # get response
        response = self.client.post('/api/taskprioritys/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_taskpriority_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # create url
        destination = urllib.parse.quote('/api/taskprioritys/', safe='/')
        # get response
        response = self.client.get('/api/taskprioritys', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_taskpriority_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
#        # get response
#        response = self.client.get('/api/taskprioritys/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_taskpriority_api')

    def test_taskpriority_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        taskpriority_api_1 = Taskpriority.objects.get(taskpriority_name='tp_1')
        # get response
        response = self.client.get('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_taskpriority_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        taskpriority_api_1 = Taskpriority.objects.get(taskpriority_name='tp_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # get response
        response = self.client.get('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskpriority_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        taskpriority_api_1 = Taskpriority.objects.get(taskpriority_name='tp_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # get response
        response = self.client.delete('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_taskpriority_detail_api_method_put(self):
        """ PUT is forbidden """

        # get object
        taskpriority_api_1 = Taskpriority.objects.get(taskpriority_name='tp_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # create url
        destination = urllib.parse.quote('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id) + '/', safe='/')
        # create PUT string
        putstring = {"taskpriority_name": "tp_3"}
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_taskpriority_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        taskpriority_api_1 = Taskpriority.objects.get(taskpriority_name='tp_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
        # create url
        destination = urllib.parse.quote('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_taskpriority_detail_api_get_user_context(self):
#        """ test user context """
#
#        # get object
#        taskpriority_api_1 = Taskpriority.objects.get(taskpriority_name='tp_1')
#        # login testuser
#        login = self.client.login(username='testuser_taskpriority_api', password='XyVSKtfXKwyyprt2b8Ej')
#        # get response
#        response = self.client.get('/api/taskprioritys/' + str(taskpriority_api_1.taskpriority_id) + '/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_taskpriority_api')
