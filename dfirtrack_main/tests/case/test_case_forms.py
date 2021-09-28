from django.test import TestCase

from dfirtrack_main.forms import CaseForm
from dfirtrack_main.models import Casepriority, Casestatus


class CaseFormTestCase(TestCase):
    """ case form tests """

    def setUp(cls):

        # create objects
        Casepriority.objects.create(casepriority_name='casepriority_1')
        Casestatus.objects.create(casestatus_name='casestatus_1')

    def test_case_id_external_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['case_id_external'].label, 'Case external ID')

    def test_case_name_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['case_name'].label, 'Case name (*)')

    def test_case_is_incident_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['case_is_incident'].label, 'Is incident')

    def test_case_note_analysisresult_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['case_note_analysisresult'].label, 'Analysis result')

    def test_case_note_external_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['case_note_external'].label, 'External note')

    def test_case_note_internal_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['case_note_internal'].label, 'Internal note')

    def test_casepriority_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['casepriority'].label, 'Casepriority (*)')

    def test_casestatus_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['casestatus'].label, 'Casestatus (*)')

    def test_casetype_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['casetype'].empty_label, 'Select casetype (optional)')

    def test_tag_form_label(self):
        """ test form label """

        # get object
        form = CaseForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tags')

    def test_case_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = CaseForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_case_name_form_filled(self):
        """ test minimum form requirements / IVVALID """

        # get object
        form = CaseForm(data = {
            'case_name': 'case_1',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_casepriority_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get objects
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')

        # get object
        form = CaseForm(data = {
            'case_name': 'case_1',
            'casepriority': casepriority_1,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_casestatus_form_filled(self):
        """ test minimum form requirements / VALID """

        # get objects
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')

        # get object
        form = CaseForm(data = {
            'case_name': 'case_1',
            'casepriority': casepriority_1,
            'casestatus': casestatus_1,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_case_name_proper_chars(self):
        """ test for max length """

        # get objects
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')

        # get object
        form = CaseForm(data = {
            'case_name': 'd' * 50,
            'casepriority': casepriority_1,
            'casestatus': casestatus_1,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_case_name_too_many_chars(self):
        """ test for max length """

        # get objects
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')

        # get object
        form = CaseForm(data = {
            'case_name': 'd' * 51,
            'casepriority': casepriority_1,
            'casestatus': casestatus_1,
        })
        # compare
        self.assertFalse(form.is_valid())
