from django.test import TestCase
from dfirtrack_main.forms import ServiceproviderForm

class ServiceproviderFormTestCase(TestCase):
    """ serviceprovider form tests """

    def test_serviceprovider_name_label(self):

        # get object
        form = ServiceproviderForm()
        # compare
        self.assertEquals(form.fields['serviceprovider_name'].label, 'Serviceprovider name (*)')

    def test_serviceprovider_note_label(self):

        # get object
        form = ServiceproviderForm()
        # compare
        self.assertEquals(form.fields['serviceprovider_note'].label, 'Serviceprovider note')

    def test_serviceprovider_name_empty(self):

        # get object
        form = ServiceproviderForm(data = {'serviceprovider_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_serviceprovider_name_filled(self):

        # get object
        form = ServiceproviderForm(data = {'serviceprovider_name': 'serviceprovider_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_serviceprovider_name_proper_chars(self):

        # get object
        form = ServiceproviderForm(data = {'serviceprovider_name': 'ssssssssssssssssssssssssssssssssssssssssssssssssss'})
        # compare
        self.assertTrue(form.is_valid())

    def test_serviceprovider_name_too_many_chars(self):

        # get object
        form = ServiceproviderForm(data = {'serviceprovider_name': 'sssssssssssssssssssssssssssssssssssssssssssssssssss'})
        # compare
        self.assertFalse(form.is_valid())
