from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_artifacts.forms import ArtifactCreatorForm
from dfirtrack_artifacts.models import Artifactpriority, Artifactstatus, Artifacttype
from dfirtrack_main.models import System, Systemstatus, Tag, Tagcolor


class ArtifactCreatorFormTestCase(TestCase):
    """artifact creator form tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_artifact_creator', password='SCYWC2EqHES9IV4TjZ2B'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='system_2',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tag_name='tag_1',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_2',
            tagcolor=tagcolor_1,
        )

        # create object
        Artifactpriority.objects.create(artifactpriority_name='prio_1')

        # create object
        Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create object
        Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        Artifacttype.objects.create(artifacttype_name='artifacttype_2')

    def test_artifact_creator_artifactpriority_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['artifactpriority'].label, 'Artifactpriority (*)')

    def test_artifact_creator_artifactstatus_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['artifactstatus'].label, 'Artifactstatus (*)')

    def test_artifact_creator_artifacttype_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['artifacttype'].label, 'Artifacttypes (*)')

    def test_artifact_creator_system_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['system'].label, 'Systems (*)')

    def test_artifact_creator_tag_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tags')

    def test_artifact_creator_analysisresult_note_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(
            form.fields['artifact_note_analysisresult'].label, 'Analysis result'
        )

    def test_artifact_creator_external_note_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['artifact_note_external'].label, 'External note')

    def test_artifact_creator_internal_note_form_label(self):
        """test form label"""

        # get object
        form = ArtifactCreatorForm()
        # compare
        self.assertEqual(form.fields['artifact_note_internal'].label, 'Internal note')

    def test_artifact_creator_form_empty(self):
        """test minimum form requirements / INVALID"""

        # get object
        form = ArtifactCreatorForm(data={})
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_creator_artifacttype_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get object
        artifacttype_1_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_1'
        ).artifacttype_id
        artifacttype_2_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_2'
        ).artifacttype_id
        # get object
        form = ArtifactCreatorForm(
            data={
                'artifacttype': [artifacttype_1_id, artifacttype_2_id],
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_creator_artifactpriority_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get object
        artifactpriority_id = Artifactpriority.objects.get(
            artifactpriority_name='prio_1'
        ).artifactpriority_id
        # get object
        artifacttype_1_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_1'
        ).artifacttype_id
        artifacttype_2_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_2'
        ).artifacttype_id
        # get object
        form = ArtifactCreatorForm(
            data={
                'artifactpriority': artifactpriority_id,
                'artifacttype': [artifacttype_1_id, artifacttype_2_id],
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_creator_artifactstatus_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get object
        artifactpriority_id = Artifactpriority.objects.get(
            artifactpriority_name='prio_1'
        ).artifactpriority_id
        # get object
        artifactstatus_id = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        ).artifactstatus_id
        # get object
        artifacttype_1_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_1'
        ).artifacttype_id
        artifacttype_2_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_2'
        ).artifacttype_id
        # get object
        form = ArtifactCreatorForm(
            data={
                'artifactpriority': artifactpriority_id,
                'artifactstatus': artifactstatus_id,
                'artifacttype': [artifacttype_1_id, artifacttype_2_id],
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_creator_system_form_filled(self):
        """test minimum form requirements / VALID"""

        # get object
        artifactpriority_id = Artifactpriority.objects.get(
            artifactpriority_name='prio_1'
        ).artifactpriority_id
        # get object
        artifactstatus_id = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        ).artifactstatus_id
        # get object
        artifacttype_1_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_1'
        ).artifacttype_id
        artifacttype_2_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_2'
        ).artifacttype_id
        # get object
        system_1_id = System.objects.get(system_name='system_1').system_id
        system_2_id = System.objects.get(system_name='system_2').system_id
        # get object
        form = ArtifactCreatorForm(
            data={
                'artifactpriority': artifactpriority_id,
                'artifactstatus': artifactstatus_id,
                'artifacttype': [artifacttype_1_id, artifacttype_2_id],
                'system': [system_1_id, system_2_id],
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_artifact_creator_all_fields_form_filled(self):
        """test additional form content"""

        # get object
        artifactpriority_id = Artifactpriority.objects.get(
            artifactpriority_name='prio_1'
        ).artifactpriority_id
        # get object
        artifactstatus_id = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        ).artifactstatus_id
        # get object
        artifacttype_1_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_1'
        ).artifacttype_id
        artifacttype_2_id = Artifacttype.objects.get(
            artifacttype_name='artifacttype_2'
        ).artifacttype_id
        # get object
        system_1_id = System.objects.get(system_name='system_1').system_id
        system_2_id = System.objects.get(system_name='system_2').system_id
        # get object
        tag_1_id = Tag.objects.get(tag_name='tag_1').tag_id
        tag_2_id = Tag.objects.get(tag_name='tag_2').tag_id
        # get object
        form = ArtifactCreatorForm(
            data={
                'artifactpriority': artifactpriority_id,
                'artifactstatus': artifactstatus_id,
                'artifacttype': [artifacttype_1_id, artifacttype_2_id],
                'system': [system_1_id, system_2_id],
                'tag': [tag_1_id, tag_2_id],
                'artifact_note_analysisresult': 'lorem ipsum',
                'artifact_note_external': 'lorem ipsum',
                'artifact_note_internal': 'lorem ipsum',
            }
        )
        # compare
        self.assertTrue(form.is_valid())
