from django.test import TestCase
from dfirtrack_main.config_forms import SystemExporterSpreadsheetXlsConfigForm

class SystemExporterSpreadsheetXlsConfigFormTestCase(TestCase):
    """ system exporter spreadsheet XLS config form tests """

    def test_system_exporter_spreadsheet_xls_config_spread_worksheet_systemstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['spread_worksheet_systemstatus'].label, 'Export worksheet to explain systemstatus')

    def test_system_exporter_spreadsheet_xls_config_spread_worksheet_analysisstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['spread_worksheet_analysisstatus'].label, 'Export worksheet to explain analysisstatus')

    def test_system_exporter_spreadsheet_xls_config_spread_worksheet_reason_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['spread_worksheet_reason'].label, 'Export worksheet to explain reason')

    def test_system_exporter_spreadsheet_xls_config_spread_worksheet_recommendation_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['spread_worksheet_recommendation'].label, 'Export worksheet to explain recommendation')

    def test_system_exporter_spreadsheet_xls_config_spread_worksheet_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['spread_worksheet_tag'].label, 'Export worksheet to explain tag')

    def test_system_exporter_spreadsheet_xls_config_form_empty(self):
        """ test minimum form requirements / VALID """

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm(data = {})
        # compare
        self.assertTrue(form.is_valid())
