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

    def test_main_config_artifactstatus_open_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['artifactstatus_open'].label, 'Artifactstatus to be considered open')
        self.assertEqual(form.fields['artifactstatus_requested'].label, 'Artifactstatus setting the artifact requested time')
        self.assertEqual(form.fields['artifactstatus_acquisition'].label, 'Artifactstatus setting the artifact acquisition time')

    def test_main_config_statushistory_entry_numbers_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['statushistory_entry_numbers'].label, 'Show only this number of last statushistory entries')

    def test_main_config_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = MainConfigForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_main_config_form_statushistory_entry_numbers_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 5,
        })
        # compare
        self.assertTrue(form.is_valid())
