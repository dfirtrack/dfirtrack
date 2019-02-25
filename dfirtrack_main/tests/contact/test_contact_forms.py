from django.test import TestCase
from dfirtrack_main.forms import ContactForm

class ContactFormTestCase(TestCase):
    """ contact form tests """

    def test_contact_name_label(self):

        # get object
        form = ContactForm()
        # compare
        self.assertEquals(form.fields['contact_name'].label, 'Contact name (*)')

    def test_contact_phone_label(self):

        # get object
        form = ContactForm()
        # compare
        self.assertEquals(form.fields['contact_phone'].label, 'Contact phone')

    def test_contact_email_label(self):

        # get object
        form = ContactForm()
        # compare
        self.assertEquals(form.fields['contact_email'].label, 'Contact email (*)')

    def test_contact_note_label(self):

        # get object
        form = ContactForm()
        # compare
        self.assertEquals(form.fields['contact_note'].label, 'Contact note')

    def test_contact_name_empty(self):

        # get object
        form = ContactForm(data = {'contact_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_contact_name_filled_without_email(self):

        # get object
        form = ContactForm(data = {'contact_name': 'contact_1'})
        # compare
        self.assertFalse(form.is_valid())

    def test_contact_name_filled_with_email(self):

        # get object
        form = ContactForm(data = {'contact_name': 'contact_1', 'contact_email': 'contact_1@example.org'})
        # compare
        self.assertTrue(form.is_valid())

    def test_contact_name_proper_chars(self):

        # get object
        form = ContactForm(data = {
            'contact_name': 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc',
            'contact_email': 'contact_1@example.org'
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_contact_name_too_many_chars(self):

        # get object
        form = ContactForm(data = {
            'contact_name': 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc',
            'contact_email': 'contact_1@example.org'
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_contact_phone_proper_chars(self):

        # get object
        form = ContactForm(data = {
            'contact_name': 'contact_1',
            'contact_phone': 'cccccccccccccccccccccccccccccccccccccccccccccccccc',
            'contact_email': 'contact_1@example.org'
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_contact_phone_too_many_chars(self):

        # get object
        form = ContactForm(data = {
            'contact_name': 'contact_1',
            'contact_phone': 'ccccccccccccccccccccccccccccccccccccccccccccccccccc',
            'contact_email': 'contact_1@example.org'
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_contact_email_proper_chars(self):

        # get object
        form = ContactForm(data = {
            'contact_name': 'contact_1',
            'contact_email': 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_contact_email_too_many_chars(self):

        # get object
        form = ContactForm(data = {
            'contact_name': 'contact_1',
            'contact_email': 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
        })
        # compare
        self.assertFalse(form.is_valid())
