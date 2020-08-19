from django.contrib import admin
from dfirtrack_config.models import ArtifactExporterSpreadsheetXlsConfigModel, SystemExporterSpreadsheetCsvConfigModel, SystemExporterSpreadsheetXlsConfigModel

# all registered models will show up in admin app
admin.site.register(ArtifactExporterSpreadsheetXlsConfigModel)
admin.site.register(SystemExporterSpreadsheetCsvConfigModel)
admin.site.register(SystemExporterSpreadsheetXlsConfigModel)
