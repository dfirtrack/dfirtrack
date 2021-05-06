from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact
from dfirtrack_artifacts.models import Artifacttype
from dfirtrack_artifacts.models import Artifactpriority
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_config.models import Workflow
from dfirtrack_config.models import WorkflowDefaultArtifactAttributes
from dfirtrack_config.models import WorkflowDefaultTasknameAttributes
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Task
from dfirtrack_main.models import Taskname
from dfirtrack_main.models import Taskpriority
from dfirtrack_main.models import Taskstatus


class WorkflowModelTestCase(TestCase):
    """ workflow model tests """

    @classmethod
    def setUpTestData(cls):
        """ default objects """
        
        # create objects
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        artfactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis')
        artfactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='10_low')

        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='10_pending')
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='10_low')

        systemstatus = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        test_user = User.objects.create_user(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')

        System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        """ workflow objects """

        # create empty workflow object
        workflow_task = Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        # create task workflow object
        workflow_task = Workflow.objects.create(
            workflow_name='workflow_task',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        # add taskname
        WorkflowDefaultTasknameAttributes.objects.create(
            workflow=workflow_task,
            taskname=taskname_1,
            task_default_priority=taskpriority_1,
            task_default_status=taskstatus_1
        )

        # create artifact workflow object
        workflow_artifact = Workflow.objects.create(
            workflow_name='workflow_artifact',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        # add default artifactname
        WorkflowDefaultArtifactAttributes.objects.create(
            workflow=workflow_artifact,
            artifacttype=artifacttype_1,
            artifact_default_name='artifact_default_name_1',
            artifact_default_priority=artfactpriority_1,
            artifact_default_status=artfactstatus_1
        )

    ''' test model methods '''

    def test_workflow_string(self):
        """ model test """

        # get object
        workflow = Workflow.objects.get(workflow_name='workflow_task')
        # compare
        self.assertEqual(str(workflow), 'workflow_task')

    def test_workflow_name_length(self):
        """ model test """

        # get object
        workflow = Workflow.objects.get(workflow_name='workflow_task')
        # get max length
        max_length = workflow._meta.get_field('workflow_name').max_length
        # compare
        self.assertEqual(max_length, 50)

    def test_workflow_get_absolute_url(self):
        """ model test """

        # get object
        workflow = Workflow.objects.get(workflow_name='workflow_task')
        # compare
        self.assertEqual(workflow.get_absolute_url(), f'/config/workflow/{workflow.workflow_id}/')

    def test_workflow_get_update_url(self):
        """ model test """

        # get object
        workflow = Workflow.objects.get(workflow_name='workflow_task')
        # compare
        self.assertEqual(workflow.get_update_url(), f'/config/workflow/{workflow.workflow_id}/update/')

    def test_workflow_get_delete_url(self):
        """ model test """

        # get object
        workflow = Workflow.objects.get(workflow_name='workflow_task')
        # compare
        self.assertEqual(workflow.get_delete_url(), f'/config/workflow/{workflow.workflow_id}/delete/')

    def helper_apply_workflow(self, system, workflow_name, workflow_amount):
        """ helper function """

        # get workflow
        workflow = Workflow.objects.get(workflow_name=workflow_name)
        # build workflow list
        workflows = [workflow.workflow_id for i in range(workflow_amount)]
        # get user
        user = User.objects.get(username='testuser_workflow')
        # apply workflow
        return Workflow.apply(workflows, system, user)

    def test_apply_workflow_task_creation(self):
        """ test task creation """

        # get object
        system = System.objects.get(system_name='system_1')
        # apply workflow
        error_code = self.helper_apply_workflow(system, 'workflow_task', 1)

        # get created task for system
        task = Task.objects.get(system=system)
        # compare
        self.assertEqual(error_code, 0)
        self.assertTupleEqual(
            (str(task.taskname), str(task.taskpriority), str(task.taskstatus)),
            ('taskname_1', '10_low', '10_pending')
        )

    def test_apply_workflow_differnt_taskattributes_creation(self):
        """ test task creation with different attributes """

        # get object
        system = System.objects.get(system_name='system_1')
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1')

        # create obects
        taskname_1 = Taskname.objects.create(taskname_name='taskname_2')
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='20_working')
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='20_medium')

        WorkflowDefaultTasknameAttributes.objects.create(
            workflow=workflow_1,
            taskname=taskname_1,
            task_default_priority=taskpriority_1,
            task_default_status=taskstatus_1
        )

         # apply workflow
        error_code = self.helper_apply_workflow(system, 'workflow_1', 1)

        # get created task for system
        task = Task.objects.get(system=system)
        # compare
        self.assertEqual(error_code, 0)
        self.assertTupleEqual(
            (str(task.taskname), str(task.taskpriority), str(task.taskstatus)),
            ('taskname_2', '20_medium', '20_working')
        )

    def test_apply_workflow_artifact_creation(self):
        """ test artifact creation """

        # get object
        system = System.objects.get(system_name='system_1')
        # apply workflow
        error_code = self.helper_apply_workflow(system, 'workflow_artifact', 1)

        # get created artifacts for system
        artifact = Artifact.objects.get(system=system)
        # compare
        self.assertEqual(error_code, 0)
        self.assertTupleEqual(
                (
                    str(artifact.artifact_name), 
                    str(artifact.artifacttype.artifacttype_name),
                    str(artifact.artifactstatus),
                    str(artifact.artifactpriority)
                ),
                (
                    'artifact_default_name_1', 
                    'artifacttype_1',
                    '10_needs_analysis',
                    '10_low'
                )
        )

    def test_apply_workflow_differnt_artifactattributes_creation(self):
        """ test artifact creation with different attributes """

        # get object
        system = System.objects.get(system_name='system_1')
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1')

        # create obects
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_2')
        artfactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='20_requested')
        artfactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='20_medium')

        WorkflowDefaultArtifactAttributes.objects.create(
            workflow=workflow_1,
            artifacttype=artifacttype_1,
            artifact_default_name='artifact_default_name_2',
            artifact_default_priority=artfactpriority_1,
            artifact_default_status=artfactstatus_1
        )

         # apply workflow
        error_code = self.helper_apply_workflow(system, 'workflow_1', 1)

        # get created artifacts for system
        artifact = Artifact.objects.get(system=system)
        # compare
        self.assertEqual(error_code, 0)
        self.assertTupleEqual(
                (
                    str(artifact.artifact_name), 
                    str(artifact.artifacttype.artifacttype_name),
                    str(artifact.artifactstatus),
                    str(artifact.artifactpriority)
                ),
                (
                    'artifact_default_name_2', 
                    'artifacttype_2',
                    '20_requested',
                    '20_medium'
                )
        )

    def test_apply_multiple_workflows_task_creation(self):
        """ test task creation """

        # get object
        system = System.objects.get(system_name='system_1')
        # apply workflow
        error_code = self.helper_apply_workflow(system, 'workflow_task', 2)

        # get created task for system
        tasks = Task.objects.filter(system=system)
        # compare
        self.assertEqual(error_code, 0)
        self.assertEqual(tasks.count(), 2)
        self.assertEqual(str(tasks[1].taskname), 'taskname_1')

    def test_apply_multiple_workflows_artifact_creation(self):
        """ test artifact creation """

        # get object
        system = System.objects.get(system_name='system_1')
        # apply workflow
        error_code = self.helper_apply_workflow(system, 'workflow_artifact', 2)

        artifacts = Artifact.objects.filter(system=system)
        # compare
        self.assertEqual(error_code, 0)
        self.assertEqual(artifacts.count(), 2)
        self.assertTupleEqual(
                (artifacts[1].artifact_name, artifacts[1].artifacttype.artifacttype_name),
                ('artifact_default_name_1', 'artifacttype_1')
        )

    def test_apply_nonexistent_workflow(self):
        """ plausibility test"""

        # get object
        workflows = (99,)
        system = System.objects.get(system_name='system_1')
        user = User.objects.get(username='testuser_workflow')
        error_code = Workflow.apply(workflows, system, user)
        # compare
        self.assertEqual(error_code, 1)

    def test_apply_wrong_value_workflow(self):
        """ plausibility test"""

        # get object
        workflows = ('should_be_integer',)
        system = System.objects.get(system_name='system_1')
        user = User.objects.get(username='testuser_workflow')
        error_code = Workflow.apply(workflows, system, user)
        # compare
        self.assertEqual(error_code, 1)

    ''' test model labels '''

    def helper_workflow_attribute_label(self, field, expected_label):
        """ helper function """

        # get object
        workflow = Workflow.objects.get(workflow_name='workflow_task')
        # get label
        field_label = workflow._meta.get_field(field).verbose_name
        # compare
        self.assertEqual(field_label, expected_label)

    def test_workflow_id_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('workflow_id', 'workflow id')

    def test_workflow_tasknames_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('tasknames', 'tasknames')

    def test_workflow_artifacttypes_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('artifacttypes', 'artifacttypes')

    def test_workflow_name_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('workflow_name', 'workflow name')

    def test_workflow_create_time_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('workflow_create_time', 'workflow create time')

    def test_workflow_modify_time_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('workflow_modify_time', 'workflow modify time')

    def test_workflow_created_by_user_id_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('workflow_created_by_user_id', 'workflow created by user id')

    def test_workflow_modified_by_user_id_attribute_label(self):
        """ label test """
        self.helper_workflow_attribute_label('workflow_modified_by_user_id', 'workflow modified by user id')
