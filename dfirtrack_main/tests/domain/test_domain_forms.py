from django.test import TestCase
from dfirtrack_main.forms import DomainForm

class DomainFormTestCase(TestCase):
    """ domain form tests """

    def test_domain_name_label(self):

        # get object
        form = DomainForm()
        # compare
        self.assertEquals(form.fields['domain_name'].label, 'Domain name (*)')

    def test_domain_note_label(self):

        # get object
        form = DomainForm()
        # compare
        self.assertEquals(form.fields['domain_note'].label, 'Domain note')

    def test_domain_name_empty(self):

        # get object
        form = DomainForm(data = {'domain_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_domain_name_filled(self):

        # get object
        form = DomainForm(data = {'domain_name': 'domain_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_domain_name_proper_chars(self):

        # get object
        form = DomainForm(data = {'domain_name': 'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'})
        # compare
        self.assertTrue(form.is_valid())

    def test_domain_name_too_many_chars(self):

        # get object
        form = DomainForm(data = {'domain_name': 'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'})
        # compare
        self.assertFalse(form.is_valid())
