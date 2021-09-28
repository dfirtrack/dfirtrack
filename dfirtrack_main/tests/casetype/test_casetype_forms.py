from django.test import TestCase

from dfirtrack_main.forms import CasetypeForm


class CasetypeFormTestCase(TestCase):
    """ casetype form tests """

    def test_casetype_name_form_label(self):
        """ test form label """

        # get object
        form = CasetypeForm()
        # compare
        self.assertEqual(form.fields['casetype_name'].label, 'Casetype name (*)')

    def test_casetype_note_form_label(self):
        """ test form label """

        # get object
        form = CasetypeForm()
        # compare
        self.assertEqual(form.fields['casetype_note'].label, 'Casetype note')

    def test_casetype_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = CasetypeForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_casetype_name_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        form = CasetypeForm(data = {'casetype_name': 'casetype_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_casetype_note_form_filled(self):
        """ test additional form content """

        # get object
        form = CasetypeForm(data = {
            'casetype_name': 'casetype_1',
            'casetype_note': 'lorem ipsum',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_casetype_name_proper_chars(self):
        """ test for max length """

        # get object
        form = CasetypeForm(data = {'casetype_name': 'a' * 255})
        # compare
        self.assertTrue(form.is_valid())

    def test_casetype_name_too_many_chars(self):
        """ test for max length """

        # get object
        form = CasetypeForm(data = {'casetype_name': 'a' * 256})
        # compare
        self.assertFalse(form.is_valid())
