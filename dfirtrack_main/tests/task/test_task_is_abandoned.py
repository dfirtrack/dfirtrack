from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_artifacts.models import (
    Artifact,
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)
from dfirtrack_main.models import (
    Case,
    System,
    Systemstatus,
    Task,
    Taskname,
    Taskpriority,
    Taskstatus,
)


class TaskIsAbandonedTestCase(TestCase):
    """task view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )

        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        system_artifact = System.objects.create(
            system_name='system_artifact',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        artifactpriority_1 = Artifactpriority.objects.create(
            artifactpriority_name='artifactpriority_1'
        )

        # create object
        artifactstatus_1 = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_1'
        )

        # create object
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        artifact_1 = Artifact.objects.create(
            artifact_name='artifact_1',
            artifactpriority=artifactpriority_1,
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
            system=system_artifact,
        )

        # create objects
        taskname_none = Taskname.objects.create(taskname_name='taskname_none')
        taskname_artifact = Taskname.objects.create(taskname_name='taskname_artifact')
        taskname_case = Taskname.objects.create(taskname_name='taskname_case')
        taskname_system = Taskname.objects.create(taskname_name='taskname_system')

        # create object
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')

        # create object
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

        # create object
        Task.objects.create(
            taskname=taskname_none,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_artifact,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
            artifact=artifact_1,
        )
        Task.objects.create(
            taskname=taskname_case,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
            case=case_1,
        )
        Task.objects.create(
            taskname=taskname_system,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
            system=system_1,
        )

    def test_task_add_post_fk_none(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # create object
        taskname = Taskname.objects.create(taskname_name='task_add_post_fk_none')
        # get objects
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # compare
        self.assertTrue(Task.objects.get(taskname=taskname).task_is_abandoned)

    def test_task_add_post_fk_artifact(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # create object
        taskname = Taskname.objects.create(taskname_name='task_add_post_fk_artifact')
        # get objects
        artifact_id = Artifact.objects.get(artifact_name='artifact_1').artifact_id
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'artifact': artifact_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # compare
        self.assertFalse(Task.objects.get(taskname=taskname).task_is_abandoned)

    def test_task_add_post_fk_case(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # create object
        taskname = Taskname.objects.create(taskname_name='task_add_post_fk_case')
        # get objects
        case_id = Case.objects.get(case_name='case_1').case_id
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'case': case_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # compare
        self.assertFalse(Task.objects.get(taskname=taskname).task_is_abandoned)

    def test_task_add_post_fk_system(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # create object
        taskname = Taskname.objects.create(taskname_name='task_add_post_fk_system')
        # get objects
        system_id = System.objects.get(system_name='system_1').system_id
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'system': system_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post('/task/add/', data_dict)
        # compare
        self.assertFalse(Task.objects.get(taskname=taskname).task_is_abandoned)

    def test_task_edit_post_fk_none(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_none')
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        task_none = Task.objects.get(taskname=taskname)
        artifact_id = Artifact.objects.get(artifact_name='artifact_1').artifact_id
        case_id = Case.objects.get(case_name='case_1').case_id
        system_id = System.objects.get(system_name='system_1').system_id
        # compare
        self.assertTrue(task_none.task_is_abandoned)
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'artifact': artifact_id,
            'case': case_id,
            'system': system_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post(f'/task/{task_none.task_id}/edit/', data_dict)
        # refresh object
        task_none.refresh_from_db()
        # compare
        self.assertFalse(task_none.task_is_abandoned)

    def test_task_edit_post_fk_artifact(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_artifact')
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        task_artifact = Task.objects.get(taskname=taskname)
        # compare
        self.assertFalse(task_artifact.task_is_abandoned)
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post(f'/task/{task_artifact.task_id}/edit/', data_dict)
        # refresh object
        task_artifact.refresh_from_db()
        # compare
        self.assertTrue(task_artifact.task_is_abandoned)

    def test_task_edit_post_fk_case(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_case')
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        task_case = Task.objects.get(taskname=taskname)
        # compare
        self.assertFalse(task_case.task_is_abandoned)
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post(f'/task/{task_case.task_id}/edit/', data_dict)
        # refresh object
        task_case.refresh_from_db()
        # compare
        self.assertTrue(task_case.task_is_abandoned)

    def test_task_edit_post_fk_system(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_task_is_abandoned').id
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_system')
        taskpriority_id = Taskpriority.objects.get(
            taskpriority_name='prio_1'
        ).taskpriority_id
        taskstatus_id = Taskstatus.objects.get(
            taskstatus_name='taskstatus_1'
        ).taskstatus_id
        task_system = Task.objects.get(taskname=taskname)
        # compare
        self.assertFalse(task_system.task_is_abandoned)
        # get post data
        data_dict = {
            'taskname': taskname.taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
            'task_created_by_user_id': test_user_id,
            'task_modified_by_user_id': test_user_id,
        }
        # get response
        self.client.post(f'/task/{task_system.task_id}/edit/', data_dict)
        # refresh object
        task_system.refresh_from_db()
        # compare
        self.assertTrue(task_system.task_is_abandoned)

    def test_task_edit_post_delete_artifact(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_artifact')
        task_artifact = Task.objects.get(taskname=taskname)
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # compare
        self.assertFalse(task_artifact.task_is_abandoned)
        # delete object
        artifact_1.delete()
        # refresh object
        task_artifact.refresh_from_db()
        # compare
        self.assertTrue(task_artifact.task_is_abandoned)

    def test_task_edit_post_delete_case(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_case')
        task_case = Task.objects.get(taskname=taskname)
        case_1 = Case.objects.get(case_name='case_1')
        # compare
        self.assertFalse(task_case.task_is_abandoned)
        # delete object
        case_1.delete()
        # refresh object
        task_case.refresh_from_db()
        # compare
        self.assertTrue(task_case.task_is_abandoned)

    def test_task_edit_post_delete_system(self):
        """test abandoned setting"""

        # login testuser
        self.client.login(
            username='testuser_task_is_abandoned', password='kOlEaeHosQ2H3svhYkzv'
        )
        # get objects
        taskname = Taskname.objects.get(taskname_name='taskname_system')
        task_system = Task.objects.get(taskname=taskname)
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertFalse(task_system.task_is_abandoned)
        # delete object
        system_1.delete()
        # refresh object
        task_system.refresh_from_db()
        # compare
        self.assertTrue(task_system.task_is_abandoned)
