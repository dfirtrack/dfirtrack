from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_artifacts.models import Artifactstatus

class ArtifactstatusModelTestCase(TestCase):
    """ artifactstatus model tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifactstatus', password='PjwBHGpyg5FlsJQtpInN')

        # create object
        Artifactstatus.objects.create(
            artifactstatus_name = 'artifactstatus_1',
            artifactstatus_created_by_user_id = test_user,
            artifactstatus_modified_by_user_id = test_user,
        )

    def test_artifactstatus_string(self):
        """ test string representation """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # compare
        self.assertEqual(str(artifactstatus_1), 'Artifactstatus artifactstatus_1')

    def test_artifactstatus_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus id')

    def test_artifactstatus_name_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_name').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus name')

    def test_artifactstatus_description_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_description').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus description')

    def test_artifactstatus_slug_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_slug').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus slug')

    def test_artifactstatus_create_time_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_create_time').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus create time')

    def test_artifactstatus_modify_time_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_modify_time').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus modify time')

    def test_artifactstatus_created_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_created_by_user_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus created by user id')

    def test_artifactstatus_modified_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get label
        field_label = artifactstatus_1._meta.get_field('artifactstatus_modified_by_user_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifactstatus modified by user id')

    def test_artifactstatus_name_length(self):
        """ test for max length """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get max length
        max_length = artifactstatus_1._meta.get_field('artifactstatus_name').max_length
        # compare
        self.assertEquals(max_length, 255)

    def test_artifactstatus_description_length(self):
        """ test for max length """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get max length
        max_length = artifactstatus_1._meta.get_field('artifactstatus_description').max_length
        # compare
        self.assertEquals(max_length, 2048)

    def test_artifactstatus_slug_length(self):
        """ test for max length """

        # get object
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        # get max length
        max_length = artifactstatus_1._meta.get_field('artifactstatus_slug').max_length
        # compare
        self.assertEquals(max_length, 255)
