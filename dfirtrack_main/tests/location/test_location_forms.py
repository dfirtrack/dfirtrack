from django.test import TestCase
from dfirtrack_main.forms import LocationForm

class LocationFormTestCase(TestCase):
    """ location form tests """

    def test_location_name_label(self):

        # get object
        form = LocationForm()
        # compare
        self.assertEquals(form.fields['location_name'].label, 'Location name (*)')

    def test_location_note_label(self):

        # get object
        form = LocationForm()
        # compare
        self.assertEquals(form.fields['location_note'].label, 'Location note')

    def test_location_name_empty(self):

        # get object
        form = LocationForm(data = {'location_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_location_name_filled(self):

        # get object
        form = LocationForm(data = {'location_name': 'location_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_location_name_proper_chars(self):

        # get object
        form = LocationForm(data = {'location_name': 'llllllllllllllllllllllllllllllllllllllllllllllllll'})
        # compare
        self.assertTrue(form.is_valid())

    def test_location_name_too_many_chars(self):

        # get object
        form = LocationForm(data = {'location_name': 'lllllllllllllllllllllllllllllllllllllllllllllllllll'})
        # compare
        self.assertFalse(form.is_valid())
