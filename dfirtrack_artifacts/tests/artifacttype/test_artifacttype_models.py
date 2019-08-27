from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_artifacts.models import Artifacttype

class ArtifacttypeModelTestCase(TestCase):
    """ artifacttype model tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifacttype', password='PjwBHGpyg5FlsJQtpInN')

        # create object
        Artifacttype.objects.create(
            artifacttype_name = 'artifacttype_1',
            artifacttype_created_by_user_id = test_user,
            artifacttype_modified_by_user_id = test_user,
        )

    def test_artifacttype_string(self):
        """ test string representation """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # compare
        self.assertEqual(str(artifacttype_1), 'Artifacttype artifacttype_1')

    def test_artifacttype_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype id')

    def test_artifacttype_name_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_name').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype name')

    def test_artifacttype_description_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_description').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype description')

    def test_artifacttype_slug_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_slug').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype slug')

    def test_artifacttype_create_time_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_create_time').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype create time')

    def test_artifacttype_modify_time_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_modify_time').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype modify time')

    def test_artifacttype_created_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_created_by_user_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype created by user id')

    def test_artifacttype_modified_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get label
        field_label = artifacttype_1._meta.get_field('artifacttype_modified_by_user_id').verbose_name
        # compare
        self.assertEquals(field_label, 'artifacttype modified by user id')

    def test_artifacttype_name_length(self):
        """ test for max length """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get max length
        max_length = artifacttype_1._meta.get_field('artifacttype_name').max_length
        # compare
        self.assertEquals(max_length, 255)

    def test_artifacttype_description_length(self):
        """ test for max length """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get max length
        max_length = artifacttype_1._meta.get_field('artifacttype_description').max_length
        # compare
        self.assertEquals(max_length, 2048)

    def test_artifacttype_slug_length(self):
        """ test for max length """

        # get object
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get max length
        max_length = artifacttype_1._meta.get_field('artifacttype_slug').max_length
        # compare
        self.assertEquals(max_length, 255)
