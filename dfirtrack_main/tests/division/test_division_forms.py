from django.test import TestCase
from dfirtrack_main.forms import DivisionForm

class DivisionFormTestCase(TestCase):
    """ division form tests """

    def test_division_name_label(self):

        # get object
        form = DivisionForm()
        # compare
        self.assertEquals(form.fields['division_name'].label, 'Division name (*)')

    def test_division_note_label(self):

        # get object
        form = DivisionForm()
        # compare
        self.assertEquals(form.fields['division_note'].label, 'Division note')

    def test_division_name_empty(self):

        # get object
        form = DivisionForm(data = {'division_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_division_name_filled(self):

        # get object
        form = DivisionForm(data = {'division_name': 'division_1'})
        # compare
        self.assertTrue(form.is_valid())
