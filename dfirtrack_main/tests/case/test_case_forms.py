from django.test import TestCase
from dfirtrack_main.forms import CaseForm

class CaseFormTestCase(TestCase):
    """ case form tests """

    def test_case_name_label(self):

        # get object
        form = CaseForm()
        # compare
        self.assertEquals(form.fields['case_name'].label, 'Case name (*)')

    def test_case_is_incident_label(self):

        # get object
        form = CaseForm()
        # compare
        self.assertEquals(form.fields['case_is_incident'].label, 'Case is incident')

    def test_case_name_empty(self):

        # get object
        form = CaseForm(data = {'case_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_case_name_filled(self):

        # get object
        form = CaseForm(data = {'case_name': 'case_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_case_name_proper_chars(self):

        # get object
        form = CaseForm(data = {'case_name': 'dddddddddddddddddddddddddddddddddddddddddddddddddd'})
        # compare
        self.assertTrue(form.is_valid())

    def test_case_name_too_many_chars(self):

        # get object
        form = CaseForm(data = {'case_name': 'ddddddddddddddddddddddddddddddddddddddddddddddddddd'})
        # compare
        self.assertFalse(form.is_valid())
