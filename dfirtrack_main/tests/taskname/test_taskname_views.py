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

    def test_taskname_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskname/', safe='')
        # get response
        response = self.client.get('/taskname/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskname_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/taskname_list.html')

    def test_taskname_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_taskname_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # create url
        destination = urllib.parse.quote('/taskname/', safe='/')
        # get response
        response = self.client.get('/taskname', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_taskname_detail_not_logged_in(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskname/' + str(taskname_1.taskname_id) + '/', safe='')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskname_detail_logged_in(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_detail_template(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/taskname_detail.html')

    def test_taskname_detail_get_user_context(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_taskname_detail_redirect(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # create url
        destination = urllib.parse.quote('/taskname/' + str(taskname_1.taskname_id) + '/', safe='/')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_taskname_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskname/add/', safe='')
        # get response
        response = self.client.get('/taskname/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskname_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/taskname_add.html')

    def test_taskname_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_taskname_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # create url
        destination = urllib.parse.quote('/taskname/add/', safe='/')
        # get response
        response = self.client.get('/taskname/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_taskname_edit_not_logged_in(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskname/' + str(taskname_1.taskname_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskname_edit_logged_in(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_edit_template(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskname/taskname_edit.html')

    def test_taskname_edit_get_user_context(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskname')

    def test_taskname_edit_redirect(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # login testuser
        login = self.client.login(username='testuser_taskname', password='7xajmDLqQh1hs8i5PAx7')
        # create url
        destination = urllib.parse.quote('/taskname/' + str(taskname_1.taskname_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/taskname/' + str(taskname_1.taskname_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
