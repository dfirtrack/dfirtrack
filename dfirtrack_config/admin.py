from django.contrib import admin

from dfirtrack_config.models import (
    ArtifactExporterSpreadsheetXlsConfigModel,
    MainConfigModel,
    Statushistory,
    SystemExporterMarkdownConfigModel,
    SystemExporterSpreadsheetCsvConfigModel,
    SystemExporterSpreadsheetXlsConfigModel,
    SystemImporterFileCsvConfigModel,
    UserConfigModel,
    Workflow,
    WorkflowDefaultArtifactAttributes,
    WorkflowDefaultTasknameAttributes,
)

# all registered models will show up in admin app
admin.site.register(ArtifactExporterSpreadsheetXlsConfigModel)
admin.site.register(MainConfigModel)
admin.site.register(SystemExporterMarkdownConfigModel)
admin.site.register(SystemExporterSpreadsheetCsvConfigModel)
admin.site.register(SystemExporterSpreadsheetXlsConfigModel)
admin.site.register(SystemImporterFileCsvConfigModel)
admin.site.register(Statushistory)
admin.site.register(UserConfigModel)
admin.site.register(Workflow)
admin.site.register(WorkflowDefaultArtifactAttributes)
admin.site.register(WorkflowDefaultTasknameAttributes)
