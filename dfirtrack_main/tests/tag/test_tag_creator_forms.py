from django.test import TestCase
from dfirtrack_main.forms import TagCreatorForm

class TagFormTestCase(TestCase):
    """ tag form tests """

    @classmethod
    def setUpTestData(cls):

        pass

    def test_tag_creator_tag_form_label(self):
        """ test form label """

        # get object
        form = TagCreatorForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tags (*)')

    def test_tag_creator_system_form_label(self):
        """ test form label """

        # get object
        form = TagCreatorForm()
        # compare
        self.assertEqual(form.fields['system'].label, 'Systems (*)')

    def test_tag_creator_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = TagCreatorForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

# TODO: add tests to test for valid form
