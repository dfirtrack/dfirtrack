from django.test import TestCase
from dfirtrack_main.forms import HeadlineForm

class HeadlineFormTestCase(TestCase):
    """ headline form tests """

    def test_headline_name_label(self):

        # get object
        form = HeadlineForm()
        # compare
        self.assertEquals(form.fields['headline_name'].label, 'Headline (*)')

    def test_headline_name_empty(self):

        # get object
        form = HeadlineForm(data = {'headline_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_headline_name_filled(self):

        # get object
        form = HeadlineForm(data = {'headline_name': 'headline_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_headline_name_proper_chars(self):

        # get object
        form = HeadlineForm(data = {'headline_name': 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'})
        # compare
        self.assertTrue(form.is_valid())

    def test_headline_name_too_many_chars(self):

        # get object
        form = HeadlineForm(data = {'headline_name': 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'})
        # compare
        self.assertFalse(form.is_valid())
