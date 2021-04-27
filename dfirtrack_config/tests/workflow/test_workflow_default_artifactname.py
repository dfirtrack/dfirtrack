from django.test import TestCase
from dfirtrack_config.models import Workflow, WorkflowDefaultArtifactname
from dfirtrack_artifacts.models import Artifacttype
from django.contrib.auth.models import User

class WorkflowDefaultArtifactnameModelTestCase(TestCase):
    """ workflow model tests """

    @classmethod
    def setUpTestData(cls):
        # Create objects
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')        

        test_user = User.objects.create_user(username='testuser_workflow_artifact_default_name', password='QVe1EH1Z5MshOW2GHS4b')

        workflow = Workflow.objects.create(
            workflow_name='workflow_artifact_default_name',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        artifacttypedefaultnames = WorkflowDefaultArtifactname.objects.create(workflow=workflow, artifacttype=artifacttype_1, artifact_default_name='artifact_default_name_1')

    ''' test model methods '''

    def test_workflow_default_artifact_name_string(self):
        # get object
        wda = WorkflowDefaultArtifactname.objects.get(artifact_default_name='artifact_default_name_1')
        # compare
        self.assertEqual(str(wda), 'artifact_default_name_1')

    def test_workflow_default_artifact_name_length(self):
        # get object
        wda = WorkflowDefaultArtifactname.objects.get(artifact_default_name='artifact_default_name_1')
        # get max length
        max_length = wda._meta.get_field('artifact_default_name').max_length
        # compare
        self.assertEqual(max_length, 50)

    ''' test model labels '''

    def helper_workflow_default_artifact_name_attribute_label(self, field, expected_label):
        # get object
        wda = WorkflowDefaultArtifactname.objects.get(artifact_default_name='artifact_default_name_1')
        # get label
        field_label = wda._meta.get_field(field).verbose_name
        # compare
        self.assertEqual(field_label, expected_label)

    def test_workflow_default_artifact_name_id_attribute_label(self):
        self.helper_workflow_default_artifact_name_attribute_label('workflow_default_artifcatname_id', 'workflow default artifcatname id')

    def test_workflow_default_artifact_name_artifacttype_attribute_label(self):
        self.helper_workflow_default_artifact_name_attribute_label('artifacttype', 'artifacttype')

    def test_workflow_default_artifact_name_workflow_attribute_label(self):
        self.helper_workflow_default_artifact_name_attribute_label('workflow', 'workflow')

    def test_workflow_default_artifact_name_artifact_default_name_attribute_label(self):
        self.helper_workflow_default_artifact_name_attribute_label('artifact_default_name', 'artifact default name')