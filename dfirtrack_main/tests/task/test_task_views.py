from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import System, Systemstatus, Task, Taskname, Taskpriority, Taskstatus
import urllib.parse

class TaskViewTestCase(TestCase):
    """ task view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_list_template(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_list.html')

    def test_task_list_get_user_context(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_list_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/closed/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_closed_template(self):
        """ test closed view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/closed/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_closed_list.html')

    def test_task_closed_get_user_context(self):
        """ test closed view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/closed/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_closed_redirect(self):
        """ test closed view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_add_system_selected(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get response
        response = self.client.get('/task/add/?system=' + str(system_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_add_template(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_add.html')

    def test_task_add_get_user_context(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get response
        response = self.client.get('/task/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task')

    def test_task_add_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/add/', safe='/')
        # get response
        response = self.client.get('/task/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_add_post_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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

    def test_task_add_post_system_selected_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
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
        response = self.client.post('/task/add/?system=' + str(system_id), data_dict)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_add_post_invalid_reload(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/task/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_add_post_invalid_template(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/task/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_add.html')

    def test_task_add_started_time_working(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user_id = User.objects.get(username = 'testuser_task').id
        # get object
        taskname_id = Taskname.objects.create(taskname_name = 'task_add_started_time_working').taskname_id
        # get object
        taskpriority_id = Taskpriority.objects.get(taskpriority_name = 'prio_1').taskpriority_id
        # get object
        taskstatus_id = Taskstatus.objects.get(taskstatus_name = 'Working').taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # get object
        taskname = Taskname.objects.get(taskname_name = 'task_add_started_time_working')
        # get object
        task_add_started_time_working = Task.objects.get(taskname = taskname)
        # compare
        self.assertTrue(task_add_started_time_working.task_started_time)

    def test_task_add_started_time_done(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user_id = User.objects.get(username = 'testuser_task').id
        # get object
        taskname_id = Taskname.objects.create(taskname_name = 'task_add_started_time_done').taskname_id
        # get object
        taskpriority_id = Taskpriority.objects.get(taskpriority_name = 'prio_1').taskpriority_id
        # get object
        taskstatus_id = Taskstatus.objects.get(taskstatus_name = 'Done').taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # get object
        taskname = Taskname.objects.get(taskname_name = 'task_add_started_time_done')
        # get object
        task_add_started_time_done = Task.objects.get(taskname = taskname)
        # compare
        self.assertTrue(task_add_started_time_done.task_started_time)

    def test_task_add_finished_time_done(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user_id = User.objects.get(username = 'testuser_task').id
        # get object
        taskname_id = Taskname.objects.create(taskname_name = 'task_add_finished_time_done').taskname_id
        # get object
        taskpriority_id = Taskpriority.objects.get(taskpriority_name = 'prio_1').taskpriority_id
        # get object
        taskstatus_id = Taskstatus.objects.get(taskstatus_name = 'Done').taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # get object
        taskname = Taskname.objects.get(taskname_name = 'task_add_finished_time_done')
        # get object
        task_add_finished_time_done = Task.objects.get(taskname = taskname)
        # compare
        self.assertTrue(task_add_finished_time_done.task_finished_time)

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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_edit_post_redirect(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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

    def test_task_edit_post_system_selected_redirect(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
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
        response = self.client.post('/task/' + str(task_1.task_id) + '/edit/?system=' + str(system_id), data_dict)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_edit_post_invalid_reload(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
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

    def test_task_edit_started_time_pending(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_started_time_pending')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_started_time = timezone.now(),
            task_finished_time = timezone.now(),
        )
        # create post data
        data_dict = {
            'taskname': taskname_1.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus_pending.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_1)
        # compare
        self.assertEqual(None, task_2.task_started_time)

    def test_task_edit_finished_time_pending(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_finished_time_pending')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_started_time = timezone.now(),
            task_finished_time = timezone.now(),
        )
        # create post data
        data_dict = {
            'taskname': taskname_1.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus_pending.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_1)
        # compare
        self.assertEqual(None, task_2.task_finished_time)

    def test_task_edit_started_time_working(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_started_time_working')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_working = Taskstatus.objects.get(taskstatus_name = 'Working')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'taskname': taskname_1.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus_working.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_1)
        # compare
        self.assertTrue(task_2.task_started_time)

    def test_task_edit_finished_time_working(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_finished_time_working')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_working = Taskstatus.objects.get(taskstatus_name = 'Working')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_started_time = timezone.now(),
            task_finished_time = timezone.now(),
        )
        # create post data
        data_dict = {
            'taskname': taskname_1.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus_working.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_1)
        # compare
        self.assertEqual(None, task_2.task_finished_time)

    def test_task_edit_started_time_done(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_started_time_done')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'taskname': taskname_1.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus_done.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_1)
        # compare
        self.assertTrue(task_2.task_started_time)

    def test_task_edit_finished_time_done(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # get object
        taskname_1 = Taskname.objects.create(taskname_name = 'task_edit_finished_time_done')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_1 = Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'taskname': taskname_1.taskname_id,
            'taskpriority': taskpriority.taskpriority_id,
            'taskstatus': taskstatus_done.taskstatus_id,
            'task_modified_by_user_id': test_user.id,
        }
        # get response
        self.client.post('/task/' + str(task_1.task_id) + '/edit/', data_dict)
        # get object
        task_2 = Task.objects.get(taskname = taskname_1)
        # compare
        self.assertTrue(task_2.task_finished_time)

    def test_task_start_redirect(self):
        """ test task start view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/start/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_start_system_selected(self):
        """ test task start view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/start/?system=' + str(system_id))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_start_status(self):
        """ test task start view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_start = Taskname.objects.create(taskname_name = 'task_start')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_start = Task.objects.create(
            taskname = taskname_task_start,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_start.task_id) + '/start/')
        # get object
        task_started = Task.objects.get(task_id = task_task_start.task_id)
        # get object
        taskstatus_working = Taskstatus.objects.get(taskstatus_name = 'Working')
        # compare
        self.assertEqual(taskstatus_working, task_started.taskstatus)

    def test_task_start_started_time(self):
        """ test task start view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_start = Taskname.objects.create(taskname_name = 'task_start')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_start = Task.objects.create(
            taskname = taskname_task_start,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_start.task_id) + '/start/')
        # get object
        task_started = Task.objects.get(task_id = task_task_start.task_id)
        # compare
        self.assertTrue(task_started.task_started_time)

    def test_task_finish_redirect(self):
        """ test task finish view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/finish/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_finish_system_selected(self):
        """ test task finish view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/finish/?system=' + str(system_id))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_finish_status(self):
        """ test task finish view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_finish = Taskname.objects.create(taskname_name = 'task_finish')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_finish = Task.objects.create(
            taskname = taskname_task_finish,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_finish.task_id) + '/finish/')
        # get object
        task_finished = Task.objects.get(task_id = task_task_finish.task_id)
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # compare
        self.assertEqual(taskstatus_done, task_finished.taskstatus)

    def test_task_finish_started_time(self):
        """ test task finish view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_finish = Taskname.objects.create(taskname_name = 'task_finish')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_finish = Task.objects.create(
            taskname = taskname_task_finish,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_finish.task_id) + '/finish/')
        # get object
        task_finished = Task.objects.get(task_id = task_task_finish.task_id)
        # compare
        self.assertTrue(task_finished.task_started_time)

    def test_task_finish_finished_time(self):
        """ test task finish view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_finish = Taskname.objects.create(taskname_name = 'task_finish')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_finish = Task.objects.create(
            taskname = taskname_task_finish,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_finish.task_id) + '/finish/')
        # get object
        task_finished = Task.objects.get(task_id = task_task_finish.task_id)
        # compare
        self.assertTrue(task_finished.task_finished_time)

    def test_task_renew_redirect(self):
        """ test task renew view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/renew/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_renew_system_selected(self):
        """ test task renew view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/renew/?system=' + str(system_id))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_renew_status(self):
        """ test task renew view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_renew = Taskname.objects.create(taskname_name = 'task_renew')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_task_renew = Task.objects.create(
            taskname = taskname_task_renew,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_renew.task_id) + '/renew/')
        # get object
        task_renewed = Task.objects.get(task_id = task_task_renew.task_id)
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # compare
        self.assertEqual(taskstatus_pending, task_renewed.taskstatus)

    def test_task_renew_user(self):
        """ test task renew view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_renew = Taskname.objects.create(taskname_name = 'task_renew')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_task_renew = Task.objects.create(
            taskname = taskname_task_renew,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_assigned_to_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_renew.task_id) + '/renew/')
        # get object
        task_renewed = Task.objects.get(task_id = task_task_renew.task_id)
        # compare
        self.assertEqual(None, task_renewed.task_assigned_to_user_id)

    def test_task_renew_started_time(self):
        """ test task renew view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_renew = Taskname.objects.create(taskname_name = 'task_renew')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_task_renew = Task.objects.create(
            taskname = taskname_task_renew,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_started_time = timezone.now(),
        )
        # get response
        self.client.get('/task/' + str(task_task_renew.task_id) + '/renew/')
        # get object
        task_renewed = Task.objects.get(task_id = task_task_renew.task_id)
        # compare
        self.assertEqual(None, task_renewed.task_started_time)

    def test_task_renew_finished_time(self):
        """ test task renew view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_renew = Taskname.objects.create(taskname_name = 'task_renew')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_done = Taskstatus.objects.get(taskstatus_name = 'Done')
        # create object
        task_task_renew = Task.objects.create(
            taskname = taskname_task_renew,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_done,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_finished_time = timezone.now(),
        )
        # get response
        self.client.get('/task/' + str(task_task_renew.task_id) + '/renew/')
        # get object
        task_renewed = Task.objects.get(task_id = task_task_renew.task_id)
        # compare
        self.assertEqual(None, task_renewed.task_finished_time)

    def test_task_set_user_redirect(self):
        """ test task set_user view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/set_user/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_set_user_system_selected(self):
        """ test task set_user view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/set_user/?system=' + str(system_id))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_set_user_user(self):
        """ test task set_user view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_set_user = Taskname.objects.create(taskname_name = 'task_set_user')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_set_user = Task.objects.create(
            taskname = taskname_task_set_user,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_set_user.task_id) + '/set_user/')
        # get object
        task_set_user = Task.objects.get(task_id = task_task_set_user.task_id)
        # compare
        self.assertEqual(test_user, task_set_user.task_assigned_to_user_id)

    def test_task_unset_user_redirect(self):
        """ test task unset_user view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/task/' + str(task_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/unset_user/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_unset_user_system_selected(self):
        """ test task unset_user view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # get response
        response = self.client.get('/task/' + str(task_1.task_id) + '/unset_user/?system=' + str(system_id))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_unset_user_user(self):
        """ test task unset_user view """

        # login testuser
        self.client.login(username='testuser_task', password='8dR7ilC8cnCr8U2aq14V')
        # get user
        test_user = User.objects.get(username = 'testuser_task')
        # create object
        taskname_task_unset_user = Taskname.objects.create(taskname_name = 'task_unset_user')
        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name = 'prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name = 'Pending')
        # create object
        task_task_unset_user = Task.objects.create(
            taskname = taskname_task_unset_user,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_pending,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
            task_assigned_to_user_id = test_user,
        )
        # get response
        self.client.get('/task/' + str(task_task_unset_user.task_id) + '/unset_user/')
        # get object
        task_unset_user = Task.objects.get(task_id = task_task_unset_user.task_id)
        # compare
        self.assertEqual(None, task_unset_user.task_assigned_to_user_id)
