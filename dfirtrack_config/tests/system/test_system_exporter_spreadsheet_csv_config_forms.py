from django.test import TestCase
from dfirtrack_main.config_forms import SystemExporterSpreadsheetCsvConfigForm

class SystemExporterSpreadsheetCsvConfigFormTestCase(TestCase):
    """ system exporter spreadsheet CSV config form tests """

    def test_system_exporter_spreadsheet_csv_config_spread_system_id_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_system_id'].label, 'Export system ID')

    def test_system_exporter_spreadsheet_csv_config_spread_dnsname_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_dnsname'].label, 'Export DNS name')

    def test_system_exporter_spreadsheet_csv_config_spread_domain_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_domain'].label, 'Export domain')

    def test_system_exporter_spreadsheet_csv_config_spread_systemstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_systemstatus'].label, 'Export systemstatus')

    def test_system_exporter_spreadsheet_csv_config_spread_analysisstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_analysisstatus'].label, 'Export analysisstatus')

    def test_system_exporter_spreadsheet_csv_config_spread_reason_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_reason'].label, 'Export reason')

    def test_system_exporter_spreadsheet_csv_config_spread_recommendation_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_recommendation'].label, 'Export recommendation')

    def test_system_exporter_spreadsheet_csv_config_spread_systemtype_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_systemtype'].label, 'Export systemtype')

    def test_system_exporter_spreadsheet_csv_config_spread_ip_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_ip'].label, 'Export IP')

    def test_system_exporter_spreadsheet_csv_config_spread_os_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_os'].label, 'Export OS')

    def test_system_exporter_spreadsheet_csv_config_spread_company_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_company'].label, 'Export company')

    def test_system_exporter_spreadsheet_csv_config_spread_location_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_location'].label, 'Export location')

    def test_system_exporter_spreadsheet_csv_config_spread_serviceprovider_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_serviceprovider'].label, 'Export serviceprovider')

    def test_system_exporter_spreadsheet_csv_config_spread_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_tag'].label, 'Export tag')

    def test_system_exporter_spreadsheet_csv_config_spread_case_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_case'].label, 'Export case')

    def test_system_exporter_spreadsheet_csv_config_spread_system_create_time_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_system_create_time'].label, 'Export system create time')

    def test_system_exporter_spreadsheet_csv_config_spread_system_modify_time_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_system_modify_time'].label, 'Export system modify time')

    def test_system_exporter_spreadsheet_csv_config_form_empty(self):
        """ test minimum form requirements / VALID """

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm(data = {})
        # compare
        self.assertTrue(form.is_valid())
