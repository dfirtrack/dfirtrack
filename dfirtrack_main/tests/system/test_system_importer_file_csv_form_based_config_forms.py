from django.test import TestCase
from dfirtrack_main.config_forms import SystemImporterFileCsvFormbasedConfigForm

class SystemImporterFileCsvFormbasedConfigFormTestCase(TestCase):
    """ system importer file CSV config-based config form tests """

    def test_system_importer_file_csv_form_based_config_csv_skip_existing_system_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_skip_existing_system'].label, 'Skip existing systems')

    def test_system_importer_file_csv_form_based_config_csv_column_system_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_column_system'].label, 'Number of the column in the CSV file that contains the system name')

    def test_system_importer_file_csv_form_based_config_csv_headline_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_headline'].label, 'CSV file contains a headline row')

    def test_system_importer_file_csv_form_based_config_csv_choice_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_choice_ip'].label, 'CSV file contains IP addresses')

    def test_system_importer_file_csv_form_based_config_csv_remove_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_ip'].label, 'Remove / overwrite existing IP addresses for already existing systems')

    def test_system_importer_file_csv_form_based_config_csv_column_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_column_ip'].label, 'Number of the column in the CSV file that contains the IP addresses')

    def test_system_importer_file_csv_form_based_config_csv_remove_case_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_case'].label, 'Remove / overwrite existing cases for already existing systems')

    def test_system_importer_file_csv_form_based_config_csv_remove_company_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_company'].label, 'Remove / overwrite existing companies for already existing systems')

    def test_system_importer_file_csv_form_based_config_csv_remove_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_tag'].label, 'Remove / overwrite existing tags for already existing systems')

#    def test_system_importer_file_csv_form_based_config_form_empty(self):
#        """ test minimum form requirements / VALID """
#
#        # get object
#        form = SystemImporterFileCsvFormbasedConfigForm(data = {})
#        # compare
#        self.assertTrue(form.is_valid())
