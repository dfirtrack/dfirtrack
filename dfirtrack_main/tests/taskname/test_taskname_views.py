from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Taskname
import urllib.parse

class TasknameViewTestCase(TestCase):
    """ taskname view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskname.objects.create(taskname_name='taskname_1')
        # create user
        test_user = User.objects.create_user(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')

    def test_tasknames_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasknames/', safe='')
        # get response
        response = self.client.get('/tasknames/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasknames_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasknames_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/tasknames_list.html')

    def test_tasknames_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_tasknames_detail_not_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasknames/' + str(taskname_1.taskname_id), safe='')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasknames_detail_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasknames_detail_template(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/tasknames_detail.html')

    def test_tasknames_detail_get_user_context(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_tasknames_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasknames/add/', safe='')
        # get response
        response = self.client.get('/tasknames/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasknames_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasknames_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/tasknames_add.html')

    def test_tasknames_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_tasknames_edit_not_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasknames/' + str(taskname_1.taskname_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasknames_edit_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasknames_edit_template(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/tasknames_edit.html')

    def test_tasknames_edit_get_user_context(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/tasknames/' + str(taskname_1.taskname_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')
