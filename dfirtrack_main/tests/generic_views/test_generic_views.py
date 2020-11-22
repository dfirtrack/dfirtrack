from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact, Artifactpriority, Artifactstatus, Artifacttype
from dfirtrack_main.models import Analysisstatus, System, Systemstatus, Task, Taskname, Taskpriority, Taskstatus
import urllib.parse

class GenericViewTestCase(TestCase):
    """ generic view tests """

    @classmethod
    def setUpTestData(cls):

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

    def test_status_view_not_logged_in(self):
        """ test generic view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/status/', safe='')
        # get response
        response = self.client.get('/status/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_status_view_logged_in(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/status/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_status_view_template(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/status/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/status.html')

    def test_status_view_get_user_context(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/status/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_generic_views')

    def test_status_view_redirect(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # create url
        destination = urllib.parse.quote('/status/', safe='/')
        # get response
        response = self.client.get('/status', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_status_view_get_object_context(self):
        """ test generic view """

        # login testuser
        self.client.login(username='testuser_generic_views', password='D9lPsoHFXeCNKEzM3IgE')
        # get response
        response = self.client.get('/status/')
        # get querysets
        analysisstatus_all = Analysisstatus.objects.all().order_by('analysisstatus_id')
        artifactpriority_all = Artifactpriority.objects.all().order_by('artifactpriority_id')
        artifactstatus_all = Artifactstatus.objects.all().order_by('artifactstatus_name')
        systemstatus_all = Systemstatus.objects.all().order_by('systemstatus_id')
        taskstatus_all = Taskstatus.objects.all().order_by('taskstatus_id')
        taskpriority_all = Taskpriority.objects.all().order_by('taskpriority_id')
        # compare
        self.assertEqual(response.context['artifacts_number'], 2)
        self.assertEqual(response.context['systems_number'], 3)
        self.assertEqual(response.context['tasks_number'], 1)
        self.assertEqual(type(response.context['analysisstatus_all']), type(analysisstatus_all))
        self.assertEqual(type(response.context['artifactpriority_all']), type(artifactpriority_all))
        self.assertEqual(type(response.context['artifactstatus_all']), type(artifactstatus_all))
        self.assertEqual(type(response.context['systemstatus_all']), type(systemstatus_all))
        self.assertEqual(type(response.context['taskpriority_all']), type(taskpriority_all))
        self.assertEqual(type(response.context['taskstatus_all']), type(taskstatus_all))
