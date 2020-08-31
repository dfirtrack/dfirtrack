from django.test import TestCase
from dfirtrack_config.forms import SystemImporterFileCsvConfigbasedConfigForm
from dfirtrack_main.models import Analysisstatus, Systemstatus

class SystemImporterFileCsvConfigbasedConfigFormTestCase(TestCase):
    """ system importer file CSV config-based config form tests """

    def test_system_importer_file_csv_config_based_config_csv_skip_existing_system_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_skip_existing_system'].label, 'Skip existing systems')

    def test_system_importer_file_csv_config_based_config_csv_column_system_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_column_system'].label, 'Number of the column in the CSV file that contains the system name')

    def test_system_importer_file_csv_config_based_config_csv_headline_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_headline'].label, 'CSV file contains a headline row')

    def test_system_importer_file_csv_config_based_config_csv_choice_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_choice_ip'].label, 'CSV file contains IP addresses')

    def test_system_importer_file_csv_config_based_config_csv_remove_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_ip'].label, 'Remove / overwrite existing IP addresses for already existing systems')

    def test_system_importer_file_csv_config_based_config_csv_column_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_column_ip'].label, 'Number of the column in the CSV file that contains the IP addresses')

    def test_system_importer_file_csv_config_based_config_csv_remove_case_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_case'].label, 'Remove / overwrite existing cases for already existing systems')

    def test_system_importer_file_csv_config_based_config_csv_remove_company_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_company'].label, 'Remove / overwrite existing companies for already existing systems')

    def test_system_importer_file_csv_config_based_config_csv_remove_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_remove_tag'].label, 'Remove / overwrite existing tags for already existing systems')

    def test_system_importer_file_csv_config_based_config_csv_default_systemstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_systemstatus'].label, 'Set systemstatus (*)')

    def test_system_importer_file_csv_config_based_config_csv_default_analysisstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_analysisstatus'].label, 'Set analysisstatus (*)')

    def test_system_importer_file_csv_config_based_config_csv_default_reason_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_reason'].label, 'Set reason')

    def test_system_importer_file_csv_config_based_config_csv_default_domain_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_domain'].label, 'Set domain')

    def test_system_importer_file_csv_config_based_config_csv_default_dnsname_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_dnsname'].label, 'Set DNS name')

    def test_system_importer_file_csv_config_based_config_csv_default_systemtype_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_systemtype'].label, 'Set systemtype')

    def test_system_importer_file_csv_config_based_config_csv_default_os_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_os'].label, 'Set OS')

    def test_system_importer_file_csv_config_based_config_csv_default_location_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_location'].label, 'Set location')

    def test_system_importer_file_csv_config_based_config_csv_default_serviceprovider_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_serviceprovider'].label, 'Set serviceprovider')

    def test_system_importer_file_csv_config_based_config_csv_default_case_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_case'].label, 'Set cases')

    def test_system_importer_file_csv_config_based_config_csv_default_company_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_company'].label, 'Set companies')

    def test_system_importer_file_csv_config_based_config_csv_default_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm()
        # compare
        self.assertEqual(form.fields['csv_default_tag'].label, 'Set tags')

    # testing without 'csv_column_system' and 'csv_column_ip' does not work because of custom field validation
    def test_system_importer_file_csv_config_based_config_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm(data = {
            'csv_column_system': 1,
            'csv_column_ip': 2,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_config_based_config_form_systemstatus_filled(self):
        """ test minimum form requirements / INVALID """

        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='Unknown').systemstatus_id
        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm(data = {
            'csv_default_systemstatus': systemstatus_id,
            'csv_column_system': 1,
            'csv_column_ip': 2,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_config_based_config_form_analysisstatus_filled(self):
        """ test minimum form requirements / INVALID """

        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='Needs analysis').analysisstatus_id
        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm(data = {
            'csv_default_analysisstatus': analysisstatus_id,
            'csv_column_system': 1,
            'csv_column_ip': 2,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_config_based_config_form_same_columns(self):
        """ test field validation / INVALID """

        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='Unknown').systemstatus_id
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='Needs analysis').analysisstatus_id
        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm(data = {
            'csv_default_systemstatus': systemstatus_id,
            'csv_default_analysisstatus': analysisstatus_id,
            'csv_column_system': 1,
            'csv_column_ip': 1,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_config_based_config_form_different_columns(self):
        """ test minimum form requirements / VALID """

        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='Unknown').systemstatus_id
        # get object (does not work the usual way because form with available choices is build before model instance is created during the test)
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='Needs analysis').analysisstatus_id
        # get object
        form = SystemImporterFileCsvConfigbasedConfigForm(data = {
            'csv_default_systemstatus': systemstatus_id,
            'csv_default_analysisstatus': analysisstatus_id,
            'csv_column_system': 1,
            'csv_column_ip': 2,
        })
        # compare
        self.assertTrue(form.is_valid())
