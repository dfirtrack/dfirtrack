from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_artifacts.models import Artifactpriority, Artifactstatus, Artifacttype
from dfirtrack_config.models import Workflow, WorkflowDefaultArtifactAttributes


class WorkflowDefaultArtifactAttributesModelTestCase(TestCase):
    """ workflow model tests """

    @classmethod
    def setUpTestData(cls):

        # create objects
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        artfactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis')
        artfactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='10_low')

        test_user = User.objects.create_user(username='testuser_workflow_artifact_default_name', password='QVe1EH1Z5MshOW2GHS4b')

        workflow = Workflow.objects.create(
            workflow_name='workflow_artifact_default_name',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        WorkflowDefaultArtifactAttributes.objects.create(
            workflow=workflow,
            artifacttype=artifacttype_1,
            artifact_default_name='artifact_default_name_1',
            artifact_default_priority=artfactpriority_1,
            artifact_default_status=artfactstatus_1
        )

    ''' test model methods '''

    def test_workflow_default_artifactname_string(self):
        """ model test """

        # get object
        wda = WorkflowDefaultArtifactAttributes.objects.get(artifact_default_name='artifact_default_name_1')
        # compare
        self.assertEqual(str(wda), 'artifact_default_name_1')

    def test_workflow_default_artifactname_length(self):
        """ model test """

        # get object
        wda = WorkflowDefaultArtifactAttributes.objects.get(artifact_default_name='artifact_default_name_1')
        # get max length
        max_length = wda._meta.get_field('artifact_default_name').max_length
        # compare
        self.assertEqual(max_length, 50)

    ''' test model labels '''

    def helper_workflow_default_artifactname_attribute_label(self, field, expected_label):
        """ helper function """

        # get object
        wda = WorkflowDefaultArtifactAttributes.objects.get(artifact_default_name='artifact_default_name_1')
        # get label
        field_label = wda._meta.get_field(field).verbose_name
        # compare
        self.assertEqual(field_label, expected_label)

    def test_workflow_default_artifactname_id_attribute_label(self):
        """ label test """
        self.helper_workflow_default_artifactname_attribute_label('workflow_default_artifactname_id', 'workflow default artifactname id')

    def test_workflow_default_artifactname_artifacttype_attribute_label(self):
        """ label test """
        self.helper_workflow_default_artifactname_attribute_label('artifacttype', 'artifacttype')

    def test_workflow_default_artifactname_workflow_attribute_label(self):
        """ label test """
        self.helper_workflow_default_artifactname_attribute_label('workflow', 'workflow')

    def test_workflow_default_artifactname_artifact_default_name_attribute_label(self):
        """ label test """
        self.helper_workflow_default_artifactname_attribute_label('artifact_default_name', 'artifact default name')

    def test_workflow_default_artifactname_artifact_default_priority_attribute_label(self):
        """ label test """
        self.helper_workflow_default_artifactname_attribute_label('artifact_default_priority', 'artifact default priority')

    def test_workflow_default_artifactname_artifact_default_status_attribute_label(self):
        """ label test """
        self.helper_workflow_default_artifactname_attribute_label('artifact_default_status', 'artifact default status')
