from django.test import TestCase

from dfirtrack_config.forms import SystemExporterSpreadsheetXlsConfigForm


class SystemExporterSpreadsheetXlsConfigFormTestCase(TestCase):
    """system exporter spreadsheet XLS config form tests"""

    def test_system_exporter_spreadsheet_xls_config_form_labels(
        self,
    ):
        """test form label"""

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['spread_xls_system_id'].label, 'Export system ID')
        self.assertEqual(form.fields['spread_xls_dnsname'].label, 'Export DNS name')
        self.assertEqual(form.fields['spread_xls_domain'].label, 'Export domain')
        self.assertEqual(
            form.fields['spread_xls_systemstatus'].label, 'Export systemstatus'
        )
        self.assertEqual(
            form.fields['spread_xls_analysisstatus'].label, 'Export analysisstatus'
        )
        self.assertEqual(form.fields['spread_xls_reason'].label, 'Export reason')
        self.assertEqual(
            form.fields['spread_xls_recommendation'].label, 'Export recommendation'
        )
        self.assertEqual(
            form.fields['spread_xls_systemtype'].label, 'Export systemtype'
        )
        self.assertEqual(form.fields['spread_xls_ip'].label, 'Export IP')
        self.assertEqual(form.fields['spread_xls_os'].label, 'Export OS')
        self.assertEqual(form.fields['spread_xls_company'].label, 'Export company')
        self.assertEqual(form.fields['spread_xls_location'].label, 'Export location')
        self.assertEqual(
            form.fields['spread_xls_serviceprovider'].label, 'Export serviceprovider'
        )
        self.assertEqual(form.fields['spread_xls_tag'].label, 'Export tag')
        self.assertEqual(form.fields['spread_xls_case'].label, 'Export case')
        self.assertEqual(
            form.fields['spread_xls_system_assigned_to_user_id'].label,
            'Export system assigned to user',
        )
        self.assertEqual(
            form.fields['spread_xls_system_create_time'].label,
            'Export system create time',
        )
        self.assertEqual(
            form.fields['spread_xls_system_created_by_user_id'].label,
            'Export system created by user',
        )
        self.assertEqual(
            form.fields['spread_xls_system_modify_time'].label,
            'Export system modify time',
        )
        self.assertEqual(
            form.fields['spread_xls_system_modified_by_user_id'].label,
            'Export system modified by user',
        )
        self.assertEqual(
            form.fields['spread_xls_worksheet_systemstatus'].label,
            'Export worksheet to explain systemstatus',
        )
        self.assertEqual(
            form.fields['spread_xls_worksheet_analysisstatus'].label,
            'Export worksheet to explain analysisstatus',
        )
        self.assertEqual(
            form.fields['spread_xls_worksheet_reason'].label,
            'Export worksheet to explain reason',
        )
        self.assertEqual(
            form.fields['spread_xls_worksheet_recommendation'].label,
            'Export worksheet to explain recommendation',
        )

    def test_system_exporter_spreadsheet_xls_config_spread_xls_worksheet_tag_form_label(
        self,
    ):
        """test form label"""

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(
            form.fields['spread_xls_worksheet_tag'].label,
            'Export worksheet to explain tag',
        )

    def test_system_exporter_spreadsheet_xls_config_form_empty(self):
        """test minimum form requirements / VALID"""

        # get object
        form = SystemExporterSpreadsheetXlsConfigForm(data={})
        # compare
        self.assertTrue(form.is_valid())
