from django.test import TestCase

from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_config.forms import ArtifactExporterSpreadsheetXlsConfigForm


class ArtifactExporterSpreadsheetXlsConfigFormTestCase(TestCase):
    """artifact exporter spreadsheet XLS config form tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_1',
            artifactstatus_slug='artifactstatus_1',
        )

    def test_artifact_exporter_spreadsheet_xls_config_form_labels(
        self,
    ):
        """test form label"""

        # get object
        form = ArtifactExporterSpreadsheetXlsConfigForm()
        # compare
        self.assertEqual(
            form.fields['artifactlist_xls_choice_artifactstatus'].label,
            'Export only artifacts with this artifactstatus',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_id'].label, 'Export artifact ID'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifactpriority'].label,
            'Export artifactpriority',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifactstatus'].label,
            'Export artifactstatus',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifacttype'].label, 'Export artifacttype'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_case_id'].label, 'Export case ID'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_case_name'].label, 'Export case name'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_system_id'].label, 'Export system ID'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_system_name'].label, 'Export system name'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_tag_all'].label, 'Export tags'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_note_analysisresult'].label,
            'Export analysis result',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_note_external'].label,
            'Export external note',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_note_internal'].label,
            'Export internal note',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_md5'].label, 'Export MD5'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_sha1'].label, 'Export SHA1'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_sha256'].label, 'Export SHA256'
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_source_path'].label,
            'Export source path',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_storage_path'].label,
            'Export storage path',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_assigned_to_user_id'].label,
            'Export assigned to user',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_create_time'].label,
            'Export create time',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_created_by_user_id'].label,
            'Export created by user',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_modify_time'].label,
            'Export modify time',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_artifact_modified_by_user_id'].label,
            'Export modified by user',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_worksheet_artifactstatus'].label,
            'Export worksheet to explain artifactstatus',
        )
        self.assertEqual(
            form.fields['artifactlist_xls_worksheet_artifacttype'].label,
            'Export worksheet to explain artifacttype',
        )

    def test_artifact_exporter_spreadsheet_xls_config_form_empty(self):
        """test minimum form requirements / INVALID"""

        # get object
        form = ArtifactExporterSpreadsheetXlsConfigForm(data={})
        # compare
        self.assertFalse(form.is_valid())

    def test_artifact_exporter_spreadsheet_xls_config_artifactlist_xls_choice_artifactstatus_form_filled(
        self,
    ):
        """test minimum form requirements / VALID"""

        # get object
        artifactstatus_id = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        )
        # get object
        form = ArtifactExporterSpreadsheetXlsConfigForm(
            data={
                'artifactlist_xls_choice_artifactstatus': [
                    artifactstatus_id,
                ],
            }
        )
        # compare
        self.assertTrue(form.is_valid())
