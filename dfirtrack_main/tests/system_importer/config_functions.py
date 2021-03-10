from dfirtrack_config.models import SystemImporterFileCsvConfigModel


def set_csv_import_path(csv_import_path):
    """ set csv_import_path """

    # change config
    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
    system_importer_file_csv_config_model.csv_import_path = csv_import_path
    system_importer_file_csv_config_model.save()

    # return to test function
    return

def set_csv_import_filename(csv_import_filename):
    """ set csv_import_filename """

    # change config
    system_importer_file_csv_config_model = SystemImporterFileCsvConfigModel.objects.get(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')
    system_importer_file_csv_config_model.csv_import_filename = csv_import_filename
    system_importer_file_csv_config_model.save()

    # return to test function
    return
