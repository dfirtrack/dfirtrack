from django.test import TestCase
from dfirtrack_main.models import Casepriority

class CasepriorityModelTestCase(TestCase):
    """ casepriority model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Casepriority.objects.create(casepriority_name = 'casepriority_1')

    def test_casepriority_string(self):
        """ test string representation """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # compare
        self.assertEqual(str(casepriority_1), 'casepriority_1')

    def test_casepriority_verbose_name_plural(self):
        """ test string representation """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # compare
        self.assertEqual(casepriority_1._meta.verbose_name_plural, 'casepriorities')

    def test_casepriority_id_attribute_label(self):
        """ test attribute label """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get label
        field_label = casepriority_1._meta.get_field('casepriority_id').verbose_name
        # compare
        self.assertEqual(field_label, 'casepriority id')

    def test_casepriority_name_attribute_label(self):
        """ test attribute label """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get label
        field_label = casepriority_1._meta.get_field('casepriority_name').verbose_name
        # compare
        self.assertEqual(field_label, 'casepriority name')

    def test_casepriority_note_attribute_label(self):
        """ test attribute label """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get label
        field_label = casepriority_1._meta.get_field('casepriority_note').verbose_name
        # compare
        self.assertEqual(field_label, 'casepriority note')

    def test_casepriority_slug_attribute_label(self):
        """ test attribute label """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get label
        field_label = casepriority_1._meta.get_field('casepriority_slug').verbose_name
        # compare
        self.assertEqual(field_label, 'casepriority slug')

    def test_casepriority_name_length(self):
        """ test for max length """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get max length
        max_length = casepriority_1._meta.get_field('casepriority_name').max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_casepriority_slug_length(self):
        """ test for max length """

        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get max length
        max_length = casepriority_1._meta.get_field('casepriority_slug').max_length
        # compare
        self.assertEqual(max_length, 255)
