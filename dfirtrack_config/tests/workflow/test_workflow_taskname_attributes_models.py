from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import Workflow, WorkflowDefaultTasknameAttributes
from dfirtrack_main.models import Taskname, Taskpriority, Taskstatus


class WorkflowDefaultTasknameAttributesModelTestCase(TestCase):
    """ workflow model tests """

    @classmethod
    def setUpTestData(cls):

        # create objects
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')
        taskpriority_1  = Taskpriority.objects.get(taskpriority_name='10_low')
        taskstastus_1 = Taskstatus.objects.get(taskstatus_name="10_pending")

        test_user = User.objects.create_user(username='testuser_workflow_taskname', password='QVe1EH1Z5MshOW2GHS4b')

        workflow = Workflow.objects.create(
            workflow_name='workflow_taskname_default_attributes',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        WorkflowDefaultTasknameAttributes.objects.create(
            workflow=workflow,
            taskname=taskname_1,
            task_default_priority=taskpriority_1,
            task_default_status=taskstastus_1
        )

    ''' test model methods '''

    def test_workflow_default_taskname_string(self):
        """ model test """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        wdt = WorkflowDefaultTasknameAttributes.objects.get(taskname=taskname_1)
        # compare
        self.assertEqual(str(wdt), taskname_1.taskname_name)

    ''' test model labels '''

    def helper_workflow_taskname_attribute_label(self, field, expected_label):
        """ helper function """

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        wdt = WorkflowDefaultTasknameAttributes.objects.get(taskname=taskname_1)
        # get label
        field_label = wdt._meta.get_field(field).verbose_name
        # compare
        self.assertEqual(field_label, expected_label)

    def test_workflow_taskname_id_attribute_label(self):
        """ label test """
        self.helper_workflow_taskname_attribute_label('workflow_default_taskname_id', 'workflow default taskname id')

    def test_workflow_taskname_attribute_label(self):
        """ label test """
        self.helper_workflow_taskname_attribute_label('taskname', 'taskname')

    def test_workflow_taskname_workflow_attribute_label(self):
        """ label test """
        self.helper_workflow_taskname_attribute_label('workflow', 'workflow')

    def test_workflow_taskname_priority_attribute_label(self):
        """ label test """
        self.helper_workflow_taskname_attribute_label('task_default_priority', 'task default priority')

    def test_workflow_taskname_status_attribute_label(self):
        """ label test """
        self.helper_workflow_taskname_attribute_label('task_default_status', 'task default status')