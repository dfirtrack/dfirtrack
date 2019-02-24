from django.test import TestCase
from dfirtrack_main.models import Location

class LocationModelTestCase(TestCase):
    """ location model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Location.objects.create(location_name='location_1')

    def test_location_string(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # compare
        self.assertEqual(str(location_1), 'location_1')

    def test_location_name_label(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # get label
        field_label = location_1._meta.get_field('location_name').verbose_name
        # compare
        self.assertEquals(field_label, 'location name')

    def test_location_note_label(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # get label
        field_label = location_1._meta.get_field('location_note').verbose_name
        # compare
        self.assertEquals(field_label, 'location note')

    def test_location_name_length(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # get max length
        max_length = location_1._meta.get_field('location_name').max_length
        # compare
        self.assertEquals(max_length, 50)
