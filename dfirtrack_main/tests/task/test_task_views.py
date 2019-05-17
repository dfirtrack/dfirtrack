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

    def test_tasks_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasks/', safe='')
        # get response
        response = self.client.get('/tasks/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasks_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasks_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/tasks_list.html')

    def test_tasks_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_tasks_detail_not_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasks/' + str(task_1.task_id), safe='')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasks_detail_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasks_detail_template(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/tasks_detail.html')

    def test_tasks_detail_get_user_context(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_tasks_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasks/add/', safe='')
        # get response
        response = self.client.get('/tasks/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasks_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasks_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/tasks_add.html')

    def test_tasks_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_tasks_edit_not_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/tasks/' + str(task_1.task_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_tasks_edit_logged_in(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tasks_edit_template(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/tasks_edit.html')

    def test_tasks_edit_get_user_context(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # login testuser
        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/tasks/' + str(task_1.task_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

#    def test_tasks_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
#        # get response
#        response = self.client.get('/tasks/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
