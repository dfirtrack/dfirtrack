from django.test import TestCase
from dfirtrack_config.models import Workflow
from dfirtrack_config.forms import WorkflowDefaultTasknameAttributesFormSet
from dfirtrack_main.models import Taskname
from dfirtrack_main.models import Taskpriority
from dfirtrack_main.models import Taskstatus
from django.contrib.auth.models import User


class WorkflowDefaultTasknameAttributesFormSetTestCase(TestCase):
    """ WorkflowDefaultTasknameAttributes formset tests """

    @classmethod
    def setUpTestData(cls):

        # create or get objects
        Taskname.objects.create(taskname_name='taskname_1')
        Taskpriority.objects.get(taskpriority_name='10_low')
        Taskstatus.objects.get(taskstatus_name="10_pending")

        test_user = User.objects.create_user(username='testuser_WorkflowDefaultTasknameAttributes', password='QVe1EH1Z5MshOW2GHS4b')

        Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

    def test_workflow_taskname_attribute_form_empty(self):
        """ formset test - INVALID """

        # get object
        form = WorkflowDefaultTasknameAttributesFormSet(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_workflow_taskname_attribute_form_filled_correct(self):
        """ formset test - VALID """

        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        taskpriority_id  = Taskpriority.objects.get(taskpriority_name='10_low').taskpriority_id
        taskstastus_id = Taskstatus.objects.get(taskstatus_name="10_pending").taskstatus_id

        # create form
        form = WorkflowDefaultTasknameAttributesFormSet(data = {
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-0-taskname': taskname_id,
            'form-0-task_default_priority': taskpriority_id,
            'form-0-task_default_status': taskstastus_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_workflow_taskname_attribute_form_filled_incorrect(self):
        """ formset test - INVALID """

        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        taskpriority_id  = Taskpriority.objects.get(taskpriority_name='10_low').taskpriority_id
        taskstastus_id = Taskstatus.objects.get(taskstatus_name="10_pending").taskstatus_id

        # create form
        form = WorkflowDefaultTasknameAttributesFormSet(data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-0-taskname': taskname_id,
            'form-0-task_default_priority': taskpriority_id,
            'form-0-task_default_status': taskstastus_id,
            'form-1-taskname': -1,
            'form-1-task_default_priority': taskpriority_id,
            'form-1-task_default_status': taskstastus_id,
        })
        # compare
        self.assertFalse(form.is_valid())
