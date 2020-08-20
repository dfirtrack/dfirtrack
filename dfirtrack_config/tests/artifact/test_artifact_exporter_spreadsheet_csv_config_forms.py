from django.test import TestCase
from dfirtrack_config.forms import ArtifactExporterSpreadsheetCsvConfigForm

class ArtifactExporterSpreadsheetCsvConfigFormTestCase(TestCase):
    """ artifact exporter spreadsheet CSV config form tests """

    # TODO: reactivate after fixing alternative selection
    #def test_artifact_exporter_spreadsheet_csv_config_artifactlist_choice_artifactstatus_form_label(self):
    #    """ test form label """

    #    # get object
    #    form = ArtifactExporterSpreadsheetCsvConfigForm()
    #    # compare
    #    self.assertEqual(form.fields['artifactlist_choice_artifactstatus'].label, 'Export only artifacts with this artifactstatus')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_id_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_id'].label, 'Export artifact ID')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_system_id_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_system_id'].label, 'Export system ID')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_system_name_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_system_name'].label, 'Export system name')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifactstatus_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifactstatus'].label, 'Export artifactstatus')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifacttype_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifacttype'].label, 'Export artifacttype')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_source_path_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_source_path'].label, 'Export source path')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_storage_path_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_storage_path'].label, 'Export storage path')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_note_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_note'].label, 'Export note')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_md5_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_md5'].label, 'Export MD5')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_sha1_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_sha1'].label, 'Export SHA1')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_sha256_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_sha256'].label, 'Export SHA256')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_create_time_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_create_time'].label, 'Export create time')

    def test_artifact_exporter_spreadsheet_csv_config_artifactlist_artifact_modify_time_form_label(self):
        """ test form label """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertEqual(form.fields['artifactlist_artifact_modify_time'].label, 'Export modify time')

    def test_artifact_exporter_spreadsheet_csv_config_form_empty(self):
        """ test minimum form requirements / VALID """

        # get object
        form = ArtifactExporterSpreadsheetCsvConfigForm()
        # compare
        self.assertTrue(form.is_valid())
