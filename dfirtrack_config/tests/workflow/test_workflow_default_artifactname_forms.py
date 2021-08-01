from dfirtrack_artifacts.models import Artifactpriority, Artifactstatus, Artifacttype
from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.forms import WorkflowDefaultArtifactAttributesFormSet
from dfirtrack_config.models import Workflow


class WWorkflowDefaultArtifactAttributesFormSetTestCase(TestCase):
    """ WorkflowDefaultArtifactAttributes formset tests """

    @classmethod
    def setUpTestData(cls):

        # create objects
        Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis')
        Artifactpriority.objects.get(artifactpriority_name='10_low')
        test_user = User.objects.create_user(username='testuser_WorkflowDefaultArtifactAttributes', password='QVe1EH1Z5MshOW2GHS4b')

        Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

    def test_workflow_default_artifact_name_form_empty(self):
        """ formset test - INVALID """

        # get object
        form = WorkflowDefaultArtifactAttributesFormSet(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_workflow_default_artifact_name_form_filled_correct(self):
        """ formset test - VALID """

        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        artfactstatus_id = Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis').artifactstatus_id
        artfactpriority_id = Artifactpriority.objects.get(artifactpriority_name='10_low').artifactpriority_id

        # create form
        form = WorkflowDefaultArtifactAttributesFormSet(data = {
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-0-artifacttype': artifacttype_id,
            'form-0-artifact_default_name': 'default_name_1',
            'form-0-artifact_default_status': artfactstatus_id,
            'form-0-artifact_default_priority': artfactpriority_id
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_workflow_default_artifact_name_form_filled_incorrect(self):
        """ formset test - INVALID """

        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        artfactstatus_id = Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis').artifactstatus_id
        artfactpriority_id = Artifactpriority.objects.get(artifactpriority_name='10_low').artifactpriority_id

        # create form
        form = WorkflowDefaultArtifactAttributesFormSet(data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-0-artifacttype': artifacttype_id,
            'form-0-artifact_default_name': 'default_name_1',
            'form-0-artifact_default_status': artfactstatus_id,
            'form-0-artifact_default_priority': artfactpriority_id,
            'form-1-artifacttype': -1,
            'form-1-artifact_default_name': 'default_name_2',
            'form-1-artifact_default_status': artfactstatus_id,
            'form-1-artifact_default_priority': artfactpriority_id
        })
        # compare
        self.assertFalse(form.is_valid())
