from django.test import TestCase
from dfirtrack_config.forms import MainConfigForm

class MainConfigFormTestCase(TestCase):
    """ main config form tests """

    @classmethod
    def setUpTestData(cls):

        pass

    def test_main_config_system_name_editable_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['system_name_editable'].label, 'Make system name editable')

    def test_main_config_form_empty(self):
        """ test minimum form requirements / VALID """

        # get object
        form = MainConfigForm(data = {})
        # compare
        self.assertTrue(form.is_valid())
