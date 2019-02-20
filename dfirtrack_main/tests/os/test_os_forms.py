from django.test import TestCase
from dfirtrack_main.forms import OsForm

class OsFormTestCase(TestCase):
    """ os form tests """

    def test_os_name_label(self):

        # get object
        form = OsForm()
        # compare
        self.assertEquals(form.fields['os_name'].label, 'Os name (*)')

    def test_os_name_empty(self):

        # get object
        form = OsForm(data = {'os_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_os_name_filled(self):

        # get object
        form = OsForm(data = {'os_name': 'os_1'})
        # compare
        self.assertTrue(form.is_valid())
