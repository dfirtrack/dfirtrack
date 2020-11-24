from datetime import datetime
from dfirtrack_artifacts.models import Artifact, Artifactpriority, Artifactstatus, Artifacttype
from dfirtrack_config.models import Statushistory, StatushistoryEntry
from dfirtrack_main.models import Analysisstatus, System, Systemstatus, Task, Taskname, Taskpriority, Taskstatus
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from mock import patch
import urllib.parse

class StatushistoryViewTestCase(TestCase):
    """ statushistory view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')

        # create user
        test_user = User.objects.create_user(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')

        # create object
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create object
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')

        # create object
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')

        # create object
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        System.objects.create(
            system_name = 'system_2',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        System.objects.create(
            system_name = 'system_3',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_1,
            task_modify_time = timezone.now(),
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )

        # create object
        Artifact.objects.create(
            artifact_name = 'artifact_1',
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            system = system_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )
        Artifact.objects.create(
            artifact_name = 'artifact_2',
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            system = system_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )

    def test_statushistory_save_view_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/statushistory/save/', safe='')
        # get response
        response = self.client.get('/config/statushistory/save/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_statushistory_save_view_logged_in(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')
        # get response
        response = self.client.get('/config/statushistory/save/')
        # create url
        destination = '/config/status/'
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_statushistory_save_view_redirect(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')
        # create url
        destination = '/config/status/'
        # get response
        response = self.client.get('/config/statushistory/save', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_statushistory_save_view_complete(self):
        """ test view """

        # mock timezone.now()
        t_1 = datetime(2020, 5, 4, 3, 2, 1, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):

            # login testuser
            self.client.login(username='testuser_statushistory', password='SXHemnLqF6chIcem5ABs')
            # get response
            self.client.get('/config/statushistory/save/')

        # get objects
        statushistory = Statushistory.objects.get(statushistory_time=t_1)
        artifacts_number = StatushistoryEntry.objects.get(
            statushistory = statushistory,
            statushistoryentry_model_name = 'artifacts_number',
        )
        systems_number = StatushistoryEntry.objects.get(
            statushistory = statushistory,
            statushistoryentry_model_name = 'systems_number',
        )
        tasks_number = StatushistoryEntry.objects.get(
            statushistory = statushistory,
            statushistoryentry_model_name = 'tasks_number',
        )
        # compare
        self.assertEqual(artifacts_number.statushistoryentry_model_value, 2)
        self.assertEqual(systems_number.statushistoryentry_model_value, 3)
        self.assertEqual(tasks_number.statushistoryentry_model_value, 1)
