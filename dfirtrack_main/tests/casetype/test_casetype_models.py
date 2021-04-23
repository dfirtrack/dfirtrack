from django.test import TestCase
from dfirtrack_main.models import Casetype

class CasetypeModelTestCase(TestCase):
    """ casetype model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Casetype.objects.create(casetype_name = 'casetype_1')

    def test_casetype_string(self):
        """ test string representation """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # compare
        self.assertEqual(str(casetype_1), 'casetype_1')

    def test_casetype_id_attribute_label(self):
        """ test attribute label """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # get label
        field_label = casetype_1._meta.get_field('casetype_id').verbose_name
        # compare
        self.assertEqual(field_label, 'casetype id')

    def test_casetype_name_attribute_label(self):
        """ test attribute label """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # get label
        field_label = casetype_1._meta.get_field('casetype_name').verbose_name
        # compare
        self.assertEqual(field_label, 'casetype name')

    def test_casetype_note_attribute_label(self):
        """ test attribute label """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # get label
        field_label = casetype_1._meta.get_field('casetype_note').verbose_name
        # compare
        self.assertEqual(field_label, 'casetype note')

    def test_casetype_slug_attribute_label(self):
        """ test attribute label """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # get label
        field_label = casetype_1._meta.get_field('casetype_slug').verbose_name
        # compare
        self.assertEqual(field_label, 'casetype slug')

    def test_casetype_name_length(self):
        """ test for max length """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # get max length
        max_length = casetype_1._meta.get_field('casetype_name').max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_casetype_slug_length(self):
        """ test for max length """

        # get object
        casetype_1 = Casetype.objects.get(casetype_name='casetype_1')
        # get max length
        max_length = casetype_1._meta.get_field('casetype_slug').max_length
        # compare
        self.assertEqual(max_length, 255)
