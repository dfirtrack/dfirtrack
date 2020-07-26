from django.test import TestCase
from dfirtrack_main.config_forms import SystemImporterFileCsvConfigForm

class SystemImporterFileCsvConfigFormTestCase(TestCase):
    """ system importer file CSV config form tests """

    def test_system_importer_file_csv_config_csv_choice_systemstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigForm()
        # compare
        self.assertEqual(form.fields['csv_choice_systemstatus'].label, 'Systemstatus')

    def test_system_importer_file_csv_config_csv_choice_analysisstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigForm()
        # compare
        self.assertEqual(form.fields['csv_choice_analysisstatus'].label, 'Analysisstatus')

    def test_system_importer_file_csv_config_form_empty(self):
        """ test minimum form requirements / VALID """

        # get object
        form = SystemImporterFileCsvConfigForm(data = {})
        # compare
        self.assertTrue(form.is_valid())
