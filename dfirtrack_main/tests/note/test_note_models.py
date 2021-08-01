from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Case, Note, Notestatus


class NoteModelTestCase(TestCase):
    """ note model tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_note', password='hypEYjnw7Sr30jPmenUh')

        # create object
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')

        #create objects
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        # create object
        Note.objects.create(
            note_title='note_1',
            note_content = 'lorem ipsum',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )

    def test_note_string(self):
        """ test string representation """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # compare
        self.assertEqual(str(note_1), 'note_1')

    def test_note_id_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_id').verbose_name
        # compare
        self.assertEqual(field_label, 'note id')

    def test_note_title_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_title').verbose_name
        # compare
        self.assertEqual(field_label, 'note title')

    def test_note_content(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_content').verbose_name
        # compare
        self.assertEqual(field_label, 'note content')

    def test_note_version_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_version').verbose_name
        # compare
        self.assertEqual(field_label, 'note version')

    def test_note_is_abandoned_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_is_abandoned').verbose_name
        # compare
        self.assertEqual(field_label, 'note is abandoned')

    def test_note_case_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('case').verbose_name
        # compare
        self.assertEqual(field_label, 'case')

    def test_note_notestatus_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('notestatus').verbose_name
        # compare
        self.assertEqual(field_label, 'notestatus')

    def test_note_tag_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('tag').verbose_name
        # compare
        self.assertEqual(field_label, 'tag')

    def test_note_create_time_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_create_time').verbose_name
        # compare
        self.assertEqual(field_label, 'note create time')

    def test_note_modify_time_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_modify_time').verbose_name
        # compare
        self.assertEqual(field_label, 'note modify time')

    def test_note_created_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_created_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'note created by user id')

    def test_note_modified_by_user_id_attribute_label(self):
        """ test attribute label """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get label
        field_label = note_1._meta.get_field('note_modified_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'note modified by user id')

    def test_note_title_length(self):
        """ test for max length """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get max length
        max_length = note_1._meta.get_field('note_title').max_length
        # compare
        self.assertEqual(max_length, 250)

    def test_note_save_version(self):
        """ test version inc of save """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # get current version
        current_version = note_1.note_version
        # save note object
        note_1.save()
        self.assertEqual(current_version+1, note_1.note_version)

    def test_note_save_abandoned(self):
        """ test abandoned of save """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        case_1 = Case.objects.get(case_name='case_1')

        # check
        self.assertTrue(note_1.note_is_abandoned)

        # set case and save note
        note_1.case = case_1
        note_1.save()

        # check
        self.assertFalse(note_1.note_is_abandoned)
