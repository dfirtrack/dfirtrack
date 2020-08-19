from django.urls import path
from dfirtrack_config.exporter.markdown import system_exporter_markdown_config_editor
from dfirtrack_config.exporter.spreadsheet import artifact_exporter_spreadsheet_config_editor, system_exporter_spreadsheet_config_editor
#from dfirtrack_config.importer.file import csv_config_editor

urlpatterns = [

    path(r'system/exporter/markdown/', system_exporter_markdown_config_editor.system_exporter_markdown_config_view, name='system_exporter_markdown_config_popup'),
    path(r'artifact/exporter/spreadsheet/xls/', artifact_exporter_spreadsheet_config_editor.artifact_exporter_spreadsheet_xls_config_view, name='artifact_exporter_spreadsheet_xls_config_popup'),
    path(r'system/exporter/spreadsheet/csv/', system_exporter_spreadsheet_config_editor.system_exporter_spreadsheet_csv_config_view, name='system_exporter_spreadsheet_csv_config_popup'),
    path(r'system/exporter/spreadsheet/xls/', system_exporter_spreadsheet_config_editor.system_exporter_spreadsheet_xls_config_view, name='system_exporter_spreadsheet_xls_config_popup'),
    #path(r'system/importer/file/csv/configbased/', csv_config_editor.system_importer_file_csv_config_based_config_view, name='system_importer_file_csv_config_based_config_popup'),
    #path(r'system/importer/file/csv/formbased/', csv_config_editor.system_importer_file_csv_form_based_config_view, name='system_importer_file_csv_form_based_config_popup'),

]
