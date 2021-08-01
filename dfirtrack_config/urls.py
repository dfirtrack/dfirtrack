from django.urls import path

from dfirtrack_config.exporter.markdown import system_exporter_markdown_config_editor
from dfirtrack_config.exporter.spreadsheet import (
    artifact_exporter_spreadsheet_config_editor,
    system_exporter_spreadsheet_config_editor,
)
from dfirtrack_config.importer.file import system_importer_file_config_editor
from dfirtrack_config.views import main_config_editor, status, statushistory, workflow

urlpatterns = [
    path(
        r"artifact/exporter/spreadsheet/xls/",
        artifact_exporter_spreadsheet_config_editor.artifact_exporter_spreadsheet_xls_config_view,
        name="artifact_exporter_spreadsheet_xls_config_popup",
    ),
    path(r"main/", main_config_editor.main_config_view, name="main_config_popup"),
    path(
        r"system/exporter/markdown/",
        system_exporter_markdown_config_editor.system_exporter_markdown_config_view,
        name="system_exporter_markdown_config_popup",
    ),
    path(
        r"system/exporter/spreadsheet/csv/",
        system_exporter_spreadsheet_config_editor.system_exporter_spreadsheet_csv_config_view,
        name="system_exporter_spreadsheet_csv_config_popup",
    ),
    path(
        r"system/exporter/spreadsheet/xls/",
        system_exporter_spreadsheet_config_editor.system_exporter_spreadsheet_xls_config_view,
        name="system_exporter_spreadsheet_xls_config_popup",
    ),
    path(
        r"system/importer/file/csv/",
        system_importer_file_config_editor.system_importer_file_csv_config_view,
        name="system_importer_file_csv_config_popup",
    ),
    path(r"status/", status.StatusView.as_view(), name="status"),
    path(r"status/<int:pk>/", status.StatusDetailView.as_view(), name="status_detail"),
    path(
        r"statushistory/save/",
        statushistory.statushistory_save,
        name="statushistory_save",
    ),
    path(r"workflow/", workflow.WorkflowList.as_view(), name="workflow_list"),
    path(
        r"workflow/<int:pk>/", workflow.WorkflowDetail.as_view(), name="workflow_detail"
    ),
    path(r"workflow/add/", workflow.WorkflowCreate.as_view(), name="workflow_create"),
    path(
        r"workflow/<int:pk>/update/",
        workflow.WorkflowUpdate.as_view(),
        name="workflow_update",
    ),
    path(
        r"workflow/<int:pk>/delete/",
        workflow.WorkflowDelete.as_view(),
        name="workflow_delete",
    ),
    path(
        r"workflow/apply/<int:system_id>/",
        workflow.apply_workflows,
        name="workflow_apply",
    ),
]
