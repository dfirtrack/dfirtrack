from django.test import TestCase
from dfirtrack_main.models import Division

class DivisionModelTestCase(TestCase):
    """ division model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Division.objects.create(division_name='division_1')

    def test_division_string(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # compare
        self.assertEqual(str(division_1), 'division_1')

    def test_division_name_label(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # get label
        field_label = division_1._meta.get_field('division_name').verbose_name
        # compare
        self.assertEquals(field_label, 'division name')

    def test_division_note_label(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # get label
        field_label = division_1._meta.get_field('division_note').verbose_name
        # compare
        self.assertEquals(field_label, 'division note')

    def test_division_name_length(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # get max length
        max_length = division_1._meta.get_field('division_name').max_length
        # compare
        self.assertEquals(max_length, 50)
