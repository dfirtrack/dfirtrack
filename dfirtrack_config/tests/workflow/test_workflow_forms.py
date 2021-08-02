from django.test import TestCase

from dfirtrack_config.forms import WorkflowForm
from dfirtrack_main.models import Taskname


class WorkflowFormTestCase(TestCase):
    """workflow form tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskname.objects.create(taskname_name="taskname_1")

    def test_workflow_name_form_label(self):
        """workflow form label test"""

        # get object
        form = WorkflowForm()
        # compare
        self.assertEqual(form.fields["workflow_name"].label, "Workflow name (*)")

    def test_workflow_form_empty(self):
        """INVALID"""

        # get object
        form = WorkflowForm(data={})
        # compare
        self.assertFalse(form.is_valid())

    def test_workflow__form_name_filled(self):
        """VALID"""

        # get object
        form = WorkflowForm(
            data={
                "workflow_name": "workflow_1",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_workflow_name_proper_chars(self):
        """test chars - VALID"""

        # get object
        form = WorkflowForm(
            data={
                "workflow_name": "workflow",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_workflow_name_too_many_chars(self):
        """test chars - INVALID"""

        # get object
        form = WorkflowForm(
            data={
                "a" * 51: "workflow",
            }
        )
        # compare
        self.assertFalse(form.is_valid())
