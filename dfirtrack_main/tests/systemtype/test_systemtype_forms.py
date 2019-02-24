from django.test import TestCase
from dfirtrack_main.forms import SystemtypeForm

class SystemtypeFormTestCase(TestCase):
    """ systemtype form tests """

    def test_systemtype_name_label(self):

        # get object
        form = SystemtypeForm()
        # compare
        self.assertEquals(form.fields['systemtype_name'].label, 'Systemtype name (*)')

    def test_systemtype_name_empty(self):

        # get object
        form = SystemtypeForm(data = {'systemtype_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_systemtype_name_filled(self):

        # get object
        form = SystemtypeForm(data = {'systemtype_name': 'systemtype_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_systemtype_name_proper_chars(self):

        # get object
        form = SystemtypeForm(data = {'systemtype_name': 'ssssssssssssssssssssssssssssssssssssssssssssssssss'})
        # compare
        self.assertTrue(form.is_valid())

    def test_systemtype_name_too_many_chars(self):

        # get object
        form = SystemtypeForm(data = {'systemtype_name': 'sssssssssssssssssssssssssssssssssssssssssssssssssss'})
        # compare
        self.assertFalse(form.is_valid())
