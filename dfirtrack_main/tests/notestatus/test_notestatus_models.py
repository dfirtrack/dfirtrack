from django.test import TestCase

from dfirtrack_main.models import Notestatus


class NotestatusModelTestCase(TestCase):
    """notestatus model tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Notestatus.objects.create(notestatus_name='notestatus_1')

    def test_notestatus_string(self):
        """test string representation"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # compare
        self.assertEqual(str(notestatus_1), 'notestatus_1')

    def test_notestatus_verbose_name_plural(self):
        """test string representation"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # compare
        self.assertEqual(notestatus_1._meta.verbose_name_plural, 'notestatus')

    def test_notestatus_id_attribute_label(self):
        """test attribute label"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get label
        field_label = notestatus_1._meta.get_field('notestatus_id').verbose_name
        # compare
        self.assertEqual(field_label, 'notestatus id')

    def test_notestatus_name_attribute_label(self):
        """test attribute label"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get label
        field_label = notestatus_1._meta.get_field('notestatus_name').verbose_name
        # compare
        self.assertEqual(field_label, 'notestatus name')

    def test_notestatus_note_attribute_label(self):
        """test attribute label"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get label
        field_label = notestatus_1._meta.get_field('notestatus_note').verbose_name
        # compare
        self.assertEqual(field_label, 'notestatus note')

    def test_notestatus_name_length(self):
        """test attribute label"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get max length
        max_length = notestatus_1._meta.get_field('notestatus_name').max_length
        # compare
        self.assertEqual(max_length, 30)
