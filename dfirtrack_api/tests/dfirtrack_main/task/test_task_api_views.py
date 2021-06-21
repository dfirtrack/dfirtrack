from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact
from dfirtrack_artifacts.models import Artifactpriority
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_artifacts.models import Artifacttype
from dfirtrack_main.models import Case
from dfirtrack_main.models import Casepriority
from dfirtrack_main.models import Casestatus
from dfirtrack_main.models import Casetype
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor
from dfirtrack_main.models import Task
from dfirtrack_main.models import Taskname
from dfirtrack_main.models import Taskpriority
from dfirtrack_main.models import Taskstatus
import urllib.parse


class TaskAPIViewTestCase(TestCase):
    """ task API view tests """

    @classmethod
    def setUpTestData(cls):
        """ one time setup """

        # create user
        test_user = User.objects.create_user(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')

        """ case """

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')
        casetype_1 = Casetype.objects.create(casetype_name='casetype_1')

        # create object
        Case.objects.create(
            case_name = 'case_1',
            casepriority = casepriority_1,
            casestatus = casestatus_1,
            casetype = casetype_1,
            case_is_incident = True,
            case_created_by_user_id = test_user,
            case_modified_by_user_id = test_user,
        )

        """ tag """

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tagcolor = tagcolor_1,
            tag_name = 'tag_1',
        )

        """ system """

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        """ artifact """

        # create objects
        artifactpriority_1 = Artifactpriority.objects.create(artifactpriority_name='artifactpriority_1')
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        Artifact.objects.create(
            artifact_name='artifact_1',
            artifactpriority = artifactpriority_1,
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            system = system_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )

        """ task """

        # create objects
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')
        Taskname.objects.create(taskname_name='taskname_2')
        Taskname.objects.create(taskname_name='taskname_3')
        taskname_parent = Taskname.objects.create(taskname_name='taskname_parent')

        # create objects
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')

        # create object
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

        # create object - main testing task
        Task.objects.create(
            taskname = taskname_1,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_1,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )

        # create object - parent task
        Task.objects.create(
            taskname = taskname_parent,
            taskpriority = taskpriority_1,
            taskstatus = taskstatus_1,
            task_created_by_user_id = test_user,
            task_modified_by_user_id = test_user,
        )

    def test_task_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/task/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_task_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get response
        response = self.client.get('/api/task/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_list_api_method_post(self):
        """ POST is allowed """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get user
        test_user_id = User.objects.get(username='testuser_task_api').id
        # get objects
        taskname_2 = Taskname.objects.get(taskname_name='taskname_2')
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='prio_1')
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # create POST string
        poststring = {
            "taskname": taskname_2.taskname_id,
            "taskpriority": taskpriority_1.taskpriority_id,
            "taskstatus": taskstatus_1.taskstatus_id,
            "task_created_by_user_id": test_user_id,
            "task_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        task_2_none = Task.objects.filter(taskname=taskname_2)
        # compare
        self.assertEqual(len(task_2_none), 0)
        # get response
        response = self.client.post('/api/task/', data=poststring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        task_2 = Task.objects.get(taskname=taskname_2)
        # compare
        self.assertEqual(task_2.taskpriority, taskpriority_1)
        self.assertEqual(task_2.taskstatus, taskstatus_1)
        self.assertTrue(task_2.task_is_abandoned)

    def test_task_list_api_method_post_all_id(self):
        """ POST is allowed """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get user
        test_user_id = User.objects.get(username='testuser_task_api').id
        # get objects
        taskname_3 = Taskname.objects.get(taskname_name='taskname_3')
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='prio_1')
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # get objects
        taskname_parent_id = Taskname.objects.get(taskname_name='taskname_parent').taskname_id
        parent_task_1 = Task.objects.get(taskname=taskname_parent_id)
        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        case_1 = Case.objects.get(case_name='case_1')
        system_1 = System.objects.get(system_name='system_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create POST string
        poststring = {
            "parent_task": parent_task_1.task_id,
            "artifact": artifact_1.artifact_id,
            "case": case_1.case_id,
            "system": system_1.system_id,
            "tag": [
                tag_1.tag_id,
            ],
            "taskname": taskname_3.taskname_id,
            "taskpriority": taskpriority_1.taskpriority_id,
            "taskstatus": taskstatus_1.taskstatus_id,
            "task_scheduled_time": '2021-05-09T12:15',
            "task_started_time": '2021-05-09T12:25',
            "task_finished_time": '2021-05-09T12:35',
            "task_due_time": '2021-05-09T12:45',
            "task_assigned_to_user_id": test_user_id,
            "task_created_by_user_id": test_user_id,
            "task_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        task_3_none = Task.objects.filter(taskname=taskname_3)
        # compare
        self.assertEqual(len(task_3_none), 0)
        # get response
        response = self.client.post('/api/task/', data=poststring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        task_3 = Task.objects.get(taskname=taskname_3)
        # compare
        self.assertEqual(task_3.parent_task, parent_task_1)
        self.assertEqual(task_3.taskpriority, taskpriority_1)
        self.assertEqual(task_3.taskstatus, taskstatus_1)
        self.assertEqual(task_3.task_scheduled_time, datetime(2021, 5, 9, 12, 15, tzinfo=timezone.utc))
        self.assertEqual(task_3.task_started_time, datetime(2021, 5, 9, 12, 25, tzinfo=timezone.utc))
        self.assertEqual(task_3.task_finished_time, datetime(2021, 5, 9, 12, 35, tzinfo=timezone.utc))
        self.assertEqual(task_3.task_due_time, datetime(2021, 5, 9, 12, 45, tzinfo=timezone.utc))
        self.assertEqual(task_3.artifact, artifact_1)
        self.assertEqual(task_3.case, case_1)
        self.assertEqual(task_3.system, system_1)
        self.assertTrue(task_3.tag.filter(tag_name='tag_1').exists())
        self.assertFalse(task_3.task_is_abandoned)

    def test_task_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # create url
        destination = urllib.parse.quote('/api/task/', safe='/')
        # get response
        response = self.client.get('/api/task', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_task_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        task_api_1 = Task.objects.get(
            taskname = taskname_id,
        )
        # get response
        response = self.client.get('/api/task/' + str(task_api_1.task_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_task_detail_api_method_get(self):
        """ GET is allowed """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        task_api_1 = Task.objects.get(
            taskname = taskname_id,
        )
        # get response
        response = self.client.get('/api/task/' + str(task_api_1.task_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        task_api_1 = Task.objects.get(
            taskname = taskname_id,
        )
        # get response
        response = self.client.delete('/api/task/' + str(task_api_1.task_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_task_detail_api_method_put(self):
        """ PUT is allowed """

        # get objects
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        task_api_1 = Task.objects.get(taskname=taskname_id)
        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get user
        test_user_id = User.objects.get(username='testuser_task_api').id
        # create objects
        taskpriority_2 = Taskpriority.objects.create(taskpriority_name='prio_2')
        taskstatus_2 = Taskstatus.objects.create(taskstatus_name='taskstatus_2')
        # create url
        destination = urllib.parse.quote('/api/task/' + str(task_api_1.task_id) + '/', safe='/')
        # create PUT string
        putstring = {
            "taskname": taskname_id,
            "taskpriority": taskpriority_2.taskpriority_id,
            "taskstatus": taskstatus_2.taskstatus_id,
            "task_created_by_user_id": test_user_id,
            "task_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        task_api_1.refresh_from_db()
        # compare
        self.assertEqual(task_api_1.taskpriority, taskpriority_2)
        self.assertEqual(task_api_1.taskstatus, taskstatus_2)
        self.assertTrue(task_api_1.task_is_abandoned)

    def test_task_detail_api_method_put_all_id(self):
        """ PUT is allowed """

        # get objects
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        task_api_1 = Task.objects.get(taskname = taskname_id)
        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get user
        test_user_id = User.objects.get(username='testuser_task_api').id
        # create objects
        taskpriority_3 = Taskpriority.objects.create(taskpriority_name='prio_3')
        taskstatus_3 = Taskstatus.objects.create(taskstatus_name='taskstatus_3')
        # get objects
        taskname_parent_id = Taskname.objects.get(taskname_name='taskname_parent').taskname_id
        parent_task_1 = Task.objects.get(taskname=taskname_parent_id)
        # get objects
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        case_1 = Case.objects.get(case_name='case_1')
        system_1 = System.objects.get(system_name='system_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create url
        destination = urllib.parse.quote('/api/task/' + str(task_api_1.task_id) + '/', safe='/')
        # create PUT string
        putstring = {
            "parent_task": parent_task_1.task_id,
            "artifact": artifact_1.artifact_id,
            "case": case_1.case_id,
            "system": system_1.system_id,
            "tag": [
                tag_1.tag_id,
            ],
            "taskname": taskname_id,
            "taskpriority": taskpriority_3.taskpriority_id,
            "taskstatus": taskstatus_3.taskstatus_id,
            "task_scheduled_time": '2021-05-09T13:15',
            "task_started_time": '2021-05-09T13:25',
            "task_finished_time": '2021-05-09T13:35',
            "task_due_time": '2021-05-09T13:45',
            "task_assigned_to_user_id": test_user_id,
            "task_created_by_user_id": test_user_id,
            "task_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        task_api_1.refresh_from_db()
        # compare
        self.assertEqual(task_api_1.parent_task, parent_task_1)
        self.assertEqual(task_api_1.taskpriority, taskpriority_3)
        self.assertEqual(task_api_1.taskstatus, taskstatus_3)
        self.assertEqual(task_api_1.task_scheduled_time, datetime(2021, 5, 9, 13, 15, tzinfo=timezone.utc))
        self.assertEqual(task_api_1.task_started_time, datetime(2021, 5, 9, 13, 25, tzinfo=timezone.utc))
        self.assertEqual(task_api_1.task_finished_time, datetime(2021, 5, 9, 13, 35, tzinfo=timezone.utc))
        self.assertEqual(task_api_1.task_due_time, datetime(2021, 5, 9, 13, 45, tzinfo=timezone.utc))
        self.assertEqual(task_api_1.artifact, artifact_1)
        self.assertEqual(task_api_1.case, case_1)
        self.assertEqual(task_api_1.system, system_1)
        self.assertTrue(task_api_1.tag.filter(tag_name='tag_1').exists())
        self.assertFalse(task_api_1.task_is_abandoned)

    def test_task_detail_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        self.client.login(username='testuser_task_api', password='jmvsz1Z551zZ4E3Cnp8D')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        task_api_1 = Task.objects.get(
            taskname = taskname_id,
        )
        # create url
        destination = urllib.parse.quote('/api/task/' + str(task_api_1.task_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/task/' + str(task_api_1.task_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
