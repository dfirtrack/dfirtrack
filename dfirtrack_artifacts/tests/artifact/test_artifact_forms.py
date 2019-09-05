from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.forms import ArtifactForm
from dfirtrack_artifacts.models import Artifactstatus, Artifacttype
from dfirtrack_main.models import Case, System, Systemstatus

class ArtifactFormTestCase(TestCase):
    """ artifact form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact', password='zpdfNMmo3vYrkHrrL6EU')

        # create object
        Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create object
        Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        Case.objects.create(
            case_name = 'case_1',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def test_artifact_name_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_name'].label, 'Artifact name (*)')

    def test_artifact_artifactstatus_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifactstatus'].label, 'Artifactstatus (*)')

    def test_artifact_artifacttype_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifacttype'].label, 'Artifacttype (*)')

    def test_artifact_source_path_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_source_path'].label, 'Artifact source path')

    def test_artifact_system_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['system'].label, 'System (*)')

    def test_artifact_case_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['case'].label, 'Case')

    def test_artifact_requested_time_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_requested_time'].label, 'Artifact requested time (YYYY-MM-DD HH:MM:SS)')

    def test_artifact_acquisition_time_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_acquisition_time'].label, 'Artifact acquisition time (YYYY-MM-DD HH:MM:SS)')

    def test_artifact_md5_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_md5'].label, 'MD5')

    def test_artifact_sha1_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_sha1'].label, 'SHA1')

    def test_artifact_sha256_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_sha256'].label, 'SHA256')

    def test_artifact_note_form_label(self):
        """ test form label """

        # get object
        form = ArtifactForm()
        # compare
        self.assertEquals(form.fields['artifact_note'].label, 'Artifact note')

    def test_artifact_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = ArtifactForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_name_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_artifactstatus_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_artifacttype_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_system_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_source_path_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_source_path': 'C:\Windows\foo\bar',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_case_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        case_id = Case.objects.get(case_name='case_1').case_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'case': case_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_requested_time_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_requested_time': timezone.now(),
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_acquisiton_time_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_acquisiton_time': timezone.now(),
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_md5_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_md5': 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_sha1_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha1': 'ssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_sha256_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha256': 'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_note_form_filled(self):
        """ test additional form content """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_note': 'lorem ipsum',
        })
        # compare
        self.assertTrue(form.is_valid())

    """
    the length of the following attributes is not tested at the moment due to their enormous numbers
    * artifact_name
    * artifact_source_path
    * artifact_storage_path
    """

    def test_artifact_md5_proper_chars(self):
        """ test for max length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_md5': 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_md5_too_many_chars(self):
        """ test for max length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_md5': 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_md5_too_less_chars(self):
        """ test for min length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_md5': 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_sha1_proper_chars(self):
        """ test for max length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha1': 'ssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_sha1_too_many_chars(self):
        """ test for max length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha1': 'sssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_sha1_too_less_chars(self):
        """ test for min length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha1': 'sssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_sha256_proper_chars(self):
        """ test for max length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha256': 'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_sha256_too_many_chars(self):
        """ test for max length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha256': 'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_sha256_too_less_chars(self):
        """ test for min length """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha256': 'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_requested_time_formatcheck(self):
        """ test input format """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_requested_time': 'wrong format',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_acquisiton_time_formatcheck(self):
        """ test input format """

        # get object
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1').artifactstatus_id
        # get object
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ArtifactForm(data = {
            'artifact_name': 'artifact_1',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_acquisition_time': 'wrong format',
        })
        # compare
        self.assertFalse(form.is_valid())
