import urllib.parse

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack.settings import INSTALLED_APPS as installed_apps
from dfirtrack_artifacts.models import (
    Artifact,
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)
from dfirtrack_config.models import MainConfigModel, Workflow
from dfirtrack_main.models import (
    Ip,
    System,
    Systemstatus,
    Task,
    Taskname,
    Taskpriority,
    Taskstatus,
)


class SystemViewTestCase(TestCase):
    """system view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_system', password='LqShcoecDud6JLRxhfKV'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create objects
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        system_2 = System.objects.create(
            system_name='system_2',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )

        # create object
        artifactpriority_1 = Artifactpriority.objects.create(
            artifactpriority_name='artifactpriority_1'
        )

        # create objects
        artifactstatus_open = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_open'
        )
        artifactstatus_closed = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_closed'
        )

        # create object
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create objects
        Artifact.objects.create(
            artifact_name='artifact_open_system_1',
            artifactpriority=artifactpriority_1,
            artifactstatus=artifactstatus_open,
            artifacttype=artifacttype_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        Artifact.objects.create(
            artifact_name='artifact_closed_system_1',
            artifactpriority=artifactpriority_1,
            artifactstatus=artifactstatus_closed,
            artifacttype=artifacttype_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        Artifact.objects.create(
            artifact_name='artifact_open_system_2',
            artifactpriority=artifactpriority_1,
            artifactstatus=artifactstatus_open,
            artifacttype=artifacttype_1,
            system=system_2,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        Artifact.objects.create(
            artifact_name='artifact_closed_system_2',
            artifactpriority=artifactpriority_1,
            artifactstatus=artifactstatus_closed,
            artifacttype=artifacttype_1,
            system=system_2,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )

        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.artifactstatus_open.add(artifactstatus_open)

        # create objects
        taskname_00_blocked_system_1 = Taskname.objects.create(
            taskname_name='task_00_blocked_system_1'
        )
        taskname_10_pending_system_1 = Taskname.objects.create(
            taskname_name='task_10_pending_system_1'
        )
        taskname_20_working_system_1 = Taskname.objects.create(
            taskname_name='task_20_working_system_1'
        )
        taskname_30_done_system_1 = Taskname.objects.create(
            taskname_name='task_30_done_system_1'
        )
        taskname_40_skipped_system_1 = Taskname.objects.create(
            taskname_name='task_40_skipped_system_1'
        )
        taskname_00_blocked_system_2 = Taskname.objects.create(
            taskname_name='task_00_blocked_system_2'
        )
        taskname_10_pending_system_2 = Taskname.objects.create(
            taskname_name='task_10_pending_system_2'
        )
        taskname_20_working_system_2 = Taskname.objects.create(
            taskname_name='task_20_working_system_2'
        )
        taskname_30_done_system_2 = Taskname.objects.create(
            taskname_name='task_30_done_system_2'
        )
        taskname_40_skipped_system_2 = Taskname.objects.create(
            taskname_name='task_40_skipped_system_2'
        )
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='taskpriority_1')

        # get objects
        taskstatus_00_blocked = Taskstatus.objects.get(taskstatus_name='00_blocked')
        taskstatus_10_pending = Taskstatus.objects.get(taskstatus_name='10_pending')
        taskstatus_20_working = Taskstatus.objects.get(taskstatus_name='20_working')
        taskstatus_30_done = Taskstatus.objects.get(taskstatus_name='30_done')
        taskstatus_40_skipped = Taskstatus.objects.get(taskstatus_name='40_skipped')

        # create objects
        Task.objects.create(
            taskname=taskname_00_blocked_system_1,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_00_blocked,
            system=system_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_10_pending_system_1,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_10_pending,
            system=system_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_20_working_system_1,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_20_working,
            system=system_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_30_done_system_1,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_30_done,
            system=system_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_40_skipped_system_1,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_40_skipped,
            system=system_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_00_blocked_system_2,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_00_blocked,
            system=system_2,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_10_pending_system_2,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_10_pending,
            system=system_2,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_20_working_system_2,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_20_working,
            system=system_2,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_30_done_system_2,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_30_done,
            system=system_2,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_40_skipped_system_2,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_40_skipped,
            system=system_2,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )

    def test_system_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/', safe='')
        # get response
        response = self.client.get('/system/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_list.html')

    def test_system_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_list_context_with_api(self):
        """test list view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_api' not in installed_apps:
            installed_apps.append('dfirtrack_api')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertTrue(response.context['dfirtrack_api'])

    def test_system_list_context_without_api(self):
        """test list view"""

        # remove app from dfirtrack.settings
        if 'dfirtrack_api' in installed_apps:
            installed_apps.remove('dfirtrack_api')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertFalse(response.context['dfirtrack_api'])

    def test_system_detail_not_logged_in(self):
        """test detail view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/', safe=''
        )
        # get response
        response = self.client.get(
            '/system/' + str(system_1.system_id) + '/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_detail_logged_in(self):
        """test detail view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_detail_template(self):
        """test detail view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_detail.html')

    def test_system_detail_get_user_context(self):
        """test detail view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_detail_redirect(self):
        """test detail view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/', safe='/'
        )
        # get response
        response = self.client.get('/system/' + str(system_1.system_id), follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_detail_context_workflows(self):
        """test detail view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_config' not in installed_apps:
            installed_apps.append('dfirtrack_config')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertEqual(str(response.context['workflows'][0]), 'workflow_1')

    def test_system_detail_context_tasks_all(self):
        """test detail view"""

        # get objects
        taskname_00_blocked_system_1 = Taskname.objects.get(
            taskname_name='task_00_blocked_system_1'
        )
        taskname_10_pending_system_1 = Taskname.objects.get(
            taskname_name='task_10_pending_system_1'
        )
        taskname_20_working_system_1 = Taskname.objects.get(
            taskname_name='task_20_working_system_1'
        )
        taskname_30_done_system_1 = Taskname.objects.get(
            taskname_name='task_30_done_system_1'
        )
        taskname_40_skipped_system_1 = Taskname.objects.get(
            taskname_name='task_40_skipped_system_1'
        )
        taskname_00_blocked_system_2 = Taskname.objects.get(
            taskname_name='task_00_blocked_system_2'
        )
        taskname_10_pending_system_2 = Taskname.objects.get(
            taskname_name='task_10_pending_system_2'
        )
        taskname_20_working_system_2 = Taskname.objects.get(
            taskname_name='task_20_working_system_2'
        )
        taskname_30_done_system_2 = Taskname.objects.get(
            taskname_name='task_30_done_system_2'
        )
        taskname_40_skipped_system_2 = Taskname.objects.get(
            taskname_name='task_40_skipped_system_2'
        )
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_00_blocked_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_10_pending_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_20_working_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_30_done_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_40_skipped_system_1)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_00_blocked_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_10_pending_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_20_working_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_30_done_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_40_skipped_system_2)
            .exists()
        )
        self.assertEqual(len(response.context['tasks_all']), 5)

    def test_system_detail_context_tasks_open(self):
        """test detail view"""

        # get objects
        taskname_00_blocked_system_1 = Taskname.objects.get(
            taskname_name='task_00_blocked_system_1'
        )
        taskname_10_pending_system_1 = Taskname.objects.get(
            taskname_name='task_10_pending_system_1'
        )
        taskname_20_working_system_1 = Taskname.objects.get(
            taskname_name='task_20_working_system_1'
        )
        taskname_30_done_system_1 = Taskname.objects.get(
            taskname_name='task_30_done_system_1'
        )
        taskname_40_skipped_system_1 = Taskname.objects.get(
            taskname_name='task_40_skipped_system_1'
        )
        taskname_00_blocked_system_2 = Taskname.objects.get(
            taskname_name='task_00_blocked_system_2'
        )
        taskname_10_pending_system_2 = Taskname.objects.get(
            taskname_name='task_10_pending_system_2'
        )
        taskname_20_working_system_2 = Taskname.objects.get(
            taskname_name='task_20_working_system_2'
        )
        taskname_30_done_system_2 = Taskname.objects.get(
            taskname_name='task_30_done_system_2'
        )
        taskname_40_skipped_system_2 = Taskname.objects.get(
            taskname_name='task_40_skipped_system_2'
        )
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_00_blocked_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_10_pending_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_20_working_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_30_done_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_40_skipped_system_1)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_00_blocked_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_10_pending_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_20_working_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_30_done_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_40_skipped_system_2)
            .exists()
        )
        self.assertEqual(len(response.context['tasks_open']), 3)

    def test_system_detail_context_tasks_closed(self):
        """test detail view"""

        # get object
        taskname_00_blocked_system_1 = Taskname.objects.get(
            taskname_name='task_00_blocked_system_1'
        )
        taskname_10_pending_system_1 = Taskname.objects.get(
            taskname_name='task_10_pending_system_1'
        )
        taskname_20_working_system_1 = Taskname.objects.get(
            taskname_name='task_20_working_system_1'
        )
        taskname_30_done_system_1 = Taskname.objects.get(
            taskname_name='task_30_done_system_1'
        )
        taskname_40_skipped_system_1 = Taskname.objects.get(
            taskname_name='task_40_skipped_system_1'
        )
        taskname_00_blocked_system_2 = Taskname.objects.get(
            taskname_name='task_00_blocked_system_2'
        )
        taskname_10_pending_system_2 = Taskname.objects.get(
            taskname_name='task_10_pending_system_2'
        )
        taskname_20_working_system_2 = Taskname.objects.get(
            taskname_name='task_20_working_system_2'
        )
        taskname_30_done_system_2 = Taskname.objects.get(
            taskname_name='task_30_done_system_2'
        )
        taskname_40_skipped_system_2 = Taskname.objects.get(
            taskname_name='task_40_skipped_system_2'
        )
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_00_blocked_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_10_pending_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_20_working_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_30_done_system_1)
            .exists()
        )
        self.assertTrue(
            response.context['tasks_all']
            .filter(taskname=taskname_40_skipped_system_1)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_00_blocked_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_10_pending_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_20_working_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_30_done_system_2)
            .exists()
        )
        self.assertFalse(
            response.context['tasks_all']
            .filter(taskname=taskname_40_skipped_system_2)
            .exists()
        )
        self.assertEqual(len(response.context['tasks_closed']), 2)

    def test_system_detail_context_with_api(self):
        """test detail view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_api' not in installed_apps:
            installed_apps.append('dfirtrack_api')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertTrue(response.context['dfirtrack_api'])

    def test_system_detail_context_without_api(self):
        """test detail view"""

        # remove app from dfirtrack.settings
        if 'dfirtrack_api' in installed_apps:
            installed_apps.remove('dfirtrack_api')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertFalse(response.context['dfirtrack_api'])

    def test_system_detail_context_artifacts_number(self):
        """test detail view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertEqual(response.context['artifacts_number'], 2)

    def test_system_add_not_logged_in(self):
        """test add view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/add/', safe='')
        # get response
        response = self.client.get('/system/add/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_add_logged_in(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_add_template(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_add.html')

    def test_system_add_get_user_context(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_add_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote('/system/add/', safe='/')
        # get response
        response = self.client.get('/system/add', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_add_post_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        # create post data
        data_dict = {
            'system_name': 'system_add_post_test',
            'systemstatus': systemstatus_id,
            'iplist': '',
        }
        # get response
        response = self.client.post('/system/add/', data_dict)
        # get object
        system_id = System.objects.get(system_name='system_add_post_test').system_id
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_add_post_invalid_reload(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_add_post_invalid_template(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_add.html')

    def test_system_add_post_ips_save_valid(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        # create post data
        data_dict = {
            'system_name': 'system_add_post_ips_save_valid_test',
            'systemstatus': systemstatus_id,
            'iplist': '127.0.0.3\n127.0.0.4',
        }
        # get response
        self.client.post('/system/add/', data_dict)
        # get object
        system_1 = System.objects.get(system_name='system_add_post_ips_save_valid_test')
        # get objects from system
        system_ip_3 = system_1.ip.filter(ip_ip='127.0.0.3')[0]
        system_ip_4 = system_1.ip.filter(ip_ip='127.0.0.4')[0]
        # get objects
        ip_3 = Ip.objects.get(ip_ip='127.0.0.3')
        ip_4 = Ip.objects.get(ip_ip='127.0.0.4')
        # compare
        self.assertEqual(system_ip_3, ip_3)
        self.assertEqual(system_ip_4, ip_4)

    def test_system_add_post_ips_save_empty_line_message(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        # create post data
        data_dict = {
            'system_name': 'system_add_post_ips_save_empty_line_test',
            'systemstatus': systemstatus_id,
            'iplist': '\n127.0.0.5',
        }
        # get response
        response = self.client.post('/system/add/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[0]), 'Empty line instead of IP was provided')

    def test_system_add_post_ips_save_no_ip_message(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        # create post data
        data_dict = {
            'system_name': 'system_add_post_ips_save_no_ip_test',
            'systemstatus': systemstatus_id,
            'iplist': 'foobar\n127.0.0.6',
        }
        # get response
        response = self.client.post('/system/add/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[0]), 'Provided string was no IP')

    def test_system_add_post_ips_save_ip_existing_message(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create object
        Ip.objects.create(ip_ip='127.0.0.7')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        # create post data
        data_dict = {
            'system_name': 'system_add_post_ips_save_ip_existing_test',
            'systemstatus': systemstatus_id,
            'iplist': '127.0.0.7',
        }
        # get response
        response = self.client.post('/system/add/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[0]), 'IP already exists in database')

    def test_system_add_context_workflows(self):
        """test add view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_config' not in installed_apps:
            installed_apps.append('dfirtrack_config')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertEqual(str(response.context['workflows'][0]), 'workflow_1')

    def test_system_add_post_workflows(self):
        """test add view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_config' not in installed_apps:
            installed_apps.append('dfirtrack_config')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        workflow_id = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create post data
        data_dict = {
            'system_name': 'system_add_with_valid_workflow',
            'systemstatus': systemstatus_id,
            'workflow': workflow_id,
            'iplist': '127.0.0.1',
        }
        # get response
        response = self.client.post('/system/add/', data_dict, follow=True)
        # compare
        self.assertContains(response, 'Workflow applied')

    def test_system_add_post_nonexistent_workflows(self):
        """test add view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_config' not in installed_apps:
            installed_apps.append('dfirtrack_config')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        systemstatus_id = Systemstatus.objects.get(
            systemstatus_name='systemstatus_1'
        ).systemstatus_id
        # create post data
        data_dict = {
            'system_name': 'system_add_with_invalid_workflow',
            'systemstatus': systemstatus_id,
            'workflow': 99,
            'iplist': '127.0.0.1',
        }
        # get response
        response = self.client.post('/system/add/', data_dict, follow=True)
        # compare
        self.assertContains(response, 'Could not apply workflow')

    def test_system_edit_not_logged_in(self):
        """test edit view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/edit/', safe=''
        )
        # get response
        response = self.client.get(
            '/system/' + str(system_1.system_id) + '/edit/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_edit_logged_in(self):
        """test edit view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_edit_template(self):
        """test edit view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_edit.html')

    def test_system_edit_get_user_context(self):
        """test edit view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_edit_redirect(self):
        """test edit view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/edit/', safe='/'
        )
        # get response
        response = self.client.get(
            '/system/' + str(system_1.system_id) + '/edit', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_edit_initial_ipstring(self):
        """test edit view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create objects
        ip_1 = Ip.objects.create(ip_ip='127.0.0.1')
        ip_2 = Ip.objects.create(ip_ip='127.0.0.2')
        # append objects
        system_1.ip.add(ip_1)
        system_1.ip.add(ip_2)
        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(
            response.context['form'].initial['iplist'], '127.0.0.1\n127.0.0.2'
        )

    def test_system_edit_post_redirect(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get user
        test_user = User.objects.get(username='testuser_system')
        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create object
        systemstatus_2 = Systemstatus.objects.create(systemstatus_name='systemstatus_2')
        # create object
        system_1 = System.objects.create(
            system_name='system_edit_post_test_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # create post data
        data_dict = {
            'system_name': 'system_edit_post_test_1',
            'systemstatus': systemstatus_2.systemstatus_id,
            'iplist': '',
        }
        # get response
        response = self.client.post(
            '/system/' + str(system_1.system_id) + '/edit/', data_dict
        )
        # get object
        system_2 = System.objects.get(system_name='system_edit_post_test_1')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_2.system_id) + '/', safe='/'
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_edit_post_invalid_reload(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/' + str(system_id) + '/edit/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_edit_post_invalid_template(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/system/' + str(system_id) + '/edit/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_edit.html')

    # TODO: does not work so far, model change in config does not affect the underlying view (it is not model related)
    def test_system_edit_post_system_name_editable_redirect(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get config model
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # set config model
        main_config_model.system_name_editable = True
        main_config_model.save()
        # get user
        test_user = User.objects.get(username='testuser_system')
        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create object
        system_1 = System.objects.create(
            system_name='system_edit_post_test_3',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # create post data
        data_dict = {
            'system_name': 'system_edit_post_test_4',
            'systemstatus': systemstatus_1.systemstatus_id,
            'iplist': '',
        }
        # get response
        response = self.client.post(
            '/system/' + str(system_1.system_id) + '/edit/', data_dict
        )
        # get object
        system_2 = System.objects.get(system_name='system_edit_post_test_4')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_2.system_id) + '/', safe='/'
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_edit_post_system_name_not_editable_redirect(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get user
        test_user = User.objects.get(username='testuser_system')
        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create object
        system_1 = System.objects.create(
            system_name='system_edit_post_test_5',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # create post data
        data_dict = {
            'system_name': 'system_edit_post_test_6',
            'systemstatus': systemstatus_1.systemstatus_id,
            'iplist': '',
        }
        # get response
        response = self.client.post(
            '/system/' + str(system_1.system_id) + '/edit/', data_dict
        )
        # get object
        system_2 = System.objects.get(system_name='system_edit_post_test_5')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_2.system_id) + '/', safe='/'
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_set_user_redirect(self):
        """test system set_user view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/', safe='/'
        )
        # get response
        response = self.client.get(
            '/system/' + str(system_1.system_id) + '/set_user/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_set_user_user(self):
        """test system set_user view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get user
        test_user = User.objects.get(username='testuser_system')
        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create object
        system_set_user = System.objects.create(
            system_name='system_unassigned',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # compare
        self.assertEqual(None, system_set_user.system_assigned_to_user_id)
        # get response
        self.client.get('/system/' + str(system_set_user.system_id) + '/set_user/')
        # refresh object
        system_set_user.refresh_from_db()
        # compare
        self.assertEqual(test_user, system_set_user.system_assigned_to_user_id)

    def test_system_unset_user_redirect(self):
        """test system unset_user view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/', safe='/'
        )
        # get response
        response = self.client.get(
            '/system/' + str(system_1.system_id) + '/unset_user/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_unset_user_user(self):
        """test system unset_user view"""

        # login testuser
        self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get user
        test_user = User.objects.get(username='testuser_system')
        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create object
        system_unset_user = System.objects.create(
            system_name='system_assigned',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
            system_assigned_to_user_id=test_user,
        )
        # compare
        self.assertEqual(test_user, system_unset_user.system_assigned_to_user_id)
        # get response
        self.client.get('/system/' + str(system_unset_user.system_id) + '/unset_user/')
        # refresh object
        system_unset_user.refresh_from_db()
        # compare
        self.assertEqual(None, system_unset_user.system_assigned_to_user_id)
