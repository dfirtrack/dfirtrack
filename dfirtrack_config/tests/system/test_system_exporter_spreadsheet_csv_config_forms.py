from django.test import TestCase

from dfirtrack_config.forms import SystemExporterSpreadsheetCsvConfigForm


class SystemExporterSpreadsheetCsvConfigFormTestCase(TestCase):
    """system exporter spreadsheet CSV config form tests"""

    def test_system_exporter_spreadsheet_csv_config_form_labels(
        self,
    ):
        """test form label"""

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['spread_csv_system_id'].label, 'Export system ID')
        self.assertEqual(form.fields['spread_csv_dnsname'].label, 'Export DNS name')
        self.assertEqual(form.fields['spread_csv_domain'].label, 'Export domain')
        self.assertEqual(
            form.fields['spread_csv_systemstatus'].label, 'Export systemstatus'
        )
        self.assertEqual(
            form.fields['spread_csv_analysisstatus'].label, 'Export analysisstatus'
        )
        self.assertEqual(form.fields['spread_csv_reason'].label, 'Export reason')
        self.assertEqual(
            form.fields['spread_csv_recommendation'].label, 'Export recommendation'
        )
        self.assertEqual(
            form.fields['spread_csv_systemtype'].label, 'Export systemtype'
        )
        self.assertEqual(form.fields['spread_csv_ip'].label, 'Export IP')
        self.assertEqual(form.fields['spread_csv_os'].label, 'Export OS')
        self.assertEqual(form.fields['spread_csv_company'].label, 'Export company')
        self.assertEqual(form.fields['spread_csv_location'].label, 'Export location')
        self.assertEqual(
            form.fields['spread_csv_serviceprovider'].label, 'Export serviceprovider'
        )
        self.assertEqual(form.fields['spread_csv_tag'].label, 'Export tag')
        self.assertEqual(form.fields['spread_csv_case'].label, 'Export case')
        self.assertEqual(
            form.fields['spread_csv_system_assigned_to_user_id'].label,
            'Export system assigned to user',
        )
        self.assertEqual(
            form.fields['spread_csv_system_create_time'].label,
            'Export system create time',
        )
        self.assertEqual(
            form.fields['spread_csv_system_created_by_user_id'].label,
            'Export system created by user',
        )
        self.assertEqual(
            form.fields['spread_csv_system_modify_time'].label,
            'Export system modify time',
        )
        self.assertEqual(
            form.fields['spread_csv_system_modified_by_user_id'].label,
            'Export system modified by user',
        )

    def test_system_exporter_spreadsheet_csv_config_form_empty(self):
        """test minimum form requirements / VALID"""

        # get object
        form = SystemExporterSpreadsheetCsvConfigForm(data={})
        # compare
        self.assertTrue(form.is_valid())
