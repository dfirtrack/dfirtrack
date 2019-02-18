from django.test import TestCase
from dfirtrack_main.forms import DomainForm

class DomainFormTestCase(TestCase):
    """ domain form tests """

    def test_domain_name_label(self):

        # get object
        form = DomainForm()
        # compare
        self.assertEquals(form.fields['domain_name'].label, 'Domain name (*)')

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
