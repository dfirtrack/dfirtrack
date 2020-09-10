from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from dfirtrack_main.importer.file.csv_importer_forms import SystemImporterFileCsvConfigbasedForm

class SystemImporterFileCsvConfigbasedFormTestCase(TestCase):
    """ system importer file CSV config-based form tests """

    def test_system_importer_file_csv_config_based_systemcsv_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvConfigbasedForm()
        # compare
        self.assertEqual(form.fields['systemcsv'].label, 'CSV with systems (*)')

    def test_system_importer_file_csv_config_based_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemImporterFileCsvConfigbasedForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_config_based_systemcsv_form_filled(self):
        """ test minimum form requirements / VALID """

        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {}
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvConfigbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())
