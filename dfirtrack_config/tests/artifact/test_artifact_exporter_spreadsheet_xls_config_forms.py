from django.test import TestCase
from dfirtrack_config.forms import ArtifactExporterSpreadsheetXlsConfigForm

class ArtifactExporterSpreadsheetXlsConfigFormTestCase(TestCase):
    """ artifact exporter spreadsheet XLS config form tests """

    def test_artifact_exporter_spreadsheet_xls_config_artifactlist_worksheet_artifactstatus_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_worksheet_artifactstatus'].label, 'Export worksheet to explain artifactstatus')

    def test_artifact_exporter_spreadsheet_xls_config_artifactlist_worksheet_artifacttype_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_worksheet_artifacttype'].label, 'Export worksheet to explain artifacttype')

    def test_artifact_exporter_spreadsheet_xls_config_form_empty(self):
        """ test minimum form requirements / VALID """

        # get object
        form = ArtifactExporterSpreadsheetXlsConfigForm(data = {})
        # compare
        self.assertTrue(form.is_valid())
