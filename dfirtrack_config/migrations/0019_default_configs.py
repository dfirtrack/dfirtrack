from django.db import migrations


def insert_default_config(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    MainConfigModel = apps.get_model('dfirtrack_config', 'MainConfigModel')
    MainConfigModel.objects.get_or_create(main_config_name='MainConfig')

    ArtifactExporterSpreadsheetXlsConfigModel = apps.get_model('dfirtrack_config', 'ArtifactExporterSpreadsheetXlsConfigModel')
    ArtifactExporterSpreadsheetXlsConfigModel.objects.get_or_create(artifact_exporter_spreadsheet_xls_config_name='ArtifactExporterSpreadsheetXlsConfig')

    SystemExporterMarkdownConfigModel = apps.get_model('dfirtrack_config', 'SystemExporterMarkdownConfigModel')
    SystemExporterMarkdownConfigModel.objects.get_or_create(system_exporter_markdown_config_name='SystemExporterMarkdownConfig')

    SystemExporterSpreadsheetCsvConfigModel = apps.get_model('dfirtrack_config', 'SystemExporterSpreadsheetCsvConfigModel')
    SystemExporterSpreadsheetCsvConfigModel.objects.get_or_create(system_exporter_spreadsheet_csv_config_name='SystemExporterSpreadsheetCsvConfig')

    SystemExporterSpreadsheetXlsConfigModel = apps.get_model('dfirtrack_config', 'SystemExporterSpreadsheetXlsConfigModel')
    SystemExporterSpreadsheetXlsConfigModel.objects.get_or_create(system_exporter_spreadsheet_xls_config_name='SystemExporterSpreadsheetXlsConfig')

    SystemImporterFileCsvConfigModel = apps.get_model('dfirtrack_config', 'SystemImporterFileCsvConfigModel')
    SystemImporterFileCsvConfigModel.objects.get_or_create(system_importer_file_csv_config_name='SystemImporterFileCsvConfig')

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0018_add_defaults'),
    ]

    operations = [
        migrations.RunPython(insert_default_config),
    ]
