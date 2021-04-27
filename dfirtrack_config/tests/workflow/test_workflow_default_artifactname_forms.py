from django.test import TestCase
from dfirtrack_config.models import Workflow
from dfirtrack_config.forms import WorkflowDefaultArtifactnameFormSet
from dfirtrack_artifacts.models import Artifacttype
from django.contrib.auth.models import User

class WorkflowFormTestCase(TestCase):
    """ workflowdefaultartifactname formset tests"""

    @classmethod
    def setUpTestData(cls):
        # create object
        artifacttype = Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        test_user = User.objects.create_user(username='testuser_workflowdefaultartifactname', password='QVe1EH1Z5MshOW2GHS4b')
        
        workflow = Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

    def test_workflow_default_artifact_name_form_empty(self):
        # get object
        form = WorkflowDefaultArtifactnameFormSet(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_workflow_default_artifact_name_form_filled_correct(self):
        # get object
        workflow_id = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id

        form = WorkflowDefaultArtifactnameFormSet(data = {
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-0-artifacttype': artifacttype_id,
            'form-0-artifact_default_name': 'default_name_1'
        })
        # compare        
        self.assertTrue(form.is_valid())

    def test_workflow_default_artifact_name_form_filled_incorrect(self):
        # get object
        workflow_id = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id

        form = WorkflowDefaultArtifactnameFormSet(data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-0-artifacttype': artifacttype_id,
            'form-0-artifact_default_name': 'default_name_1',
            'form-1-artifacttype': -1,
            'form-1-artifact_default_name': 'default_name_2'
        })
        self.assertFalse(form.is_valid())
