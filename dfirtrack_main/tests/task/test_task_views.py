from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Task, Taskname, Taskpriority, Taskstatus
import urllib.parse

class TaskViewTestCase(TestCase):
    """ task view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')

        # create object
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')

        # create object
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')

        # create object
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

        # create object
        Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_1,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )

    def test_task_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/task/', safe='')
        # get response
        response = self.client.get('/task/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_list.html')

    def test_task_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/', safe='/')
        # get response
        response = self.client.get('/task', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_closed_not_logged_in(self):
        """ test closed view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/task/closed/', safe='')
        # get response
        response = self.client.get('/task/closed/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_closed_logged_in(self):
        """ test closed view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/closed/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_closed_template(self):
        """ test closed view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/closed/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_closed_list.html')

    def test_task_closed_get_user_context(self):
        """ test closed view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/closed/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_closed_redirect(self):
        """ test closed view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/closed/', safe='/')
        # get response
        response = self.client.get('/task/closed', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_detail_not_logged_in(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_detail_logged_in(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_detail_template(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_detail.html')

    def test_task_detail_get_user_context(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_detail_redirect(self):
        """ test detail view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/task/add/', safe='')
        # get response
        response = self.client.get('/task/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_add.html')

    def test_task_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/add/', safe='/')
        # get response
        response = self.client.get('/task/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_add_post_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user_id = User.objects.get(username = 'testuser_task').id
        # get object
        taskname_id = Taskname.objects.create(taskname_name = 'task_add_post_test').taskname_id
        # get object
        taskpriority_id = Taskpriority.objects.get(taskpriority_name = 'prio_1').taskpriority_id
        # get object
        taskstatus_id = Taskstatus.objects.get(taskstatus_name = 'taskstatus_1').taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        response = self.client.post('/task/add/', data_dict)
        # get object
        taskname = Taskname.objects.get(taskname_name = 'task_add_post_test')
        # get object
        task_id = Task.objects.get(taskname = taskname).task_id
        # create url
        destination = urllib.parse.quote('/task/' + str(task_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_add_post_invalid_reload(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/task/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_add_post_invalid_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/task/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_add.html')

    def test_task_edit_not_logged_in(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/task/' + str(task_1.task_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_edit_logged_in(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_edit_template(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_edit.html')

    def test_task_edit_get_user_context(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_edit_redirect(self):
        """ test edit view """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_edit_post_redirect(self):
        """ test edit view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_post_test_1')
        # get object
        taskname_2 = Taskname.objects.create(taskname_name = 'task_edit_post_test_2')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus = Taskstatus.objects.get(taskstatus_name = 'taskstatus_1')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'taskname': taskname_2.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        response = self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_2)
        # create url
        destination = urllib.parse.quote('/task/' + str(task_2.task_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_edit_post_invalid_reload(self):
        """ test edit view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name = 'taskname_1')
        # get object
        task_id = Task.objects.get(taskname = taskname_1).task_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/task/' + str(task_id) + '/edit/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_edit_post_invalid_template(self):
        """ test edit view """

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name = 'taskname_1')
        # get object
        task_id = Task.objects.get(taskname = taskname_1).task_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/task/' + str(task_id) + '/edit/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_edit.html')
