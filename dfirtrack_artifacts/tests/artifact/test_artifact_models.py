from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_main.models import System, Systemstatus

class ArtifactModelTestCase(TestCase):
    """ artifact model tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact', password='dfIlDYMVqsRnLjpUR9EL')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create object
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        Artifact.objects.create(
            artifact_name = 'artifact_1',
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
            system = system_1,
        )

    def test_artifact_string(self):
        """ test string representation """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get object id
        artifact_id = artifact_1.artifact_id
        # get foreign key object id
        system_id = artifact_1.system.system_id
        # compare
        self.assertEqual(str(artifact_1), 'Artifact ' + str(artifact_id) + ' ([' + str(system_id) + '] system_1)')

    def test_artifact_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get label
        field_label = artifact_1._meta.get_field('artifact_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifact id')

    def test_artifact_name_attribute_label(self):
        """ test attribute label """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get label
        field_label = artifact_1._meta.get_field('artifact_name').verbose_name
        # compare
        self.assertEquals(field_label, 'artifact name')

    def test_artifact_create_time_attribute_label(self):
        """ test attribute label """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get label
        field_label = artifact_1._meta.get_field('artifact_create_time').verbose_name
        # compare
        self.assertEquals(field_label, 'artifact create time')

    def test_artifact_modify_time_attribute_label(self):
        """ test attribute label """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get label
        field_label = artifact_1._meta.get_field('artifact_modify_time').verbose_name
        # compare
        self.assertEquals(field_label, 'artifact modify time')

    def test_artifact_created_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get label
        field_label = artifact_1._meta.get_field('artifact_created_by_user_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifact created by user id')

    def test_artifact_modified_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get label
        field_label = artifact_1._meta.get_field('artifact_modified_by_user_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifact modified by user id')

    def test_artifact_name_length(self):
        """ test for max length """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # get max length
        max_length = artifact_1._meta.get_field('artifact_name').max_length
        # compare
        self.assertEquals(max_length, 4096)
