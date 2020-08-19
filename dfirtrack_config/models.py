from django.db import models

class ArtifactExporterSpreadsheetXlsConfigModel(models.Model):

    # primary key
    artifact_exporter_spreadsheet_xls_config_name = models.CharField(max_length=50, primary_key=True)

    # config fields
    artifactlist_xls_artifact_id = models.BooleanField(blank=True)
    artifactlist_xls_system_id = models.BooleanField(blank=True)
    artifactlist_xls_system_name = models.BooleanField(blank=True)
    artifactlist_xls_artifactstatus = models.BooleanField(blank=True)
    artifactlist_xls_artifacttype = models.BooleanField(blank=True)
    artifactlist_xls_artifact_source_path = models.BooleanField(blank=True)
    artifactlist_xls_artifact_storage_path = models.BooleanField(blank=True)
    artifactlist_xls_artifact_note = models.BooleanField(blank=True)
    artifactlist_xls_artifact_md5 = models.BooleanField(blank=True)
    artifactlist_xls_artifact_sha1 = models.BooleanField(blank=True)
    artifactlist_xls_artifact_sha256 = models.BooleanField(blank=True)
    artifactlist_xls_artifact_create_time = models.BooleanField(blank=True)
    artifactlist_xls_artifact_modify_time = models.BooleanField(blank=True)
    artifactlist_xls_worksheet_artifactstatus = models.BooleanField(blank=True)
    artifactlist_xls_worksheet_artifacttype = models.BooleanField(blank=True)
    # TODO: find an alternative for the selection
    artifactlist_xls_choice_artifactstatus = models.IntegerField()

class SystemExporterSpreadsheetCsvConfigModel(models.Model):

    # primary key
    system_exporter_spreadsheet_csv_config_name = models.CharField(max_length=50, primary_key=True)

    # config fields
    spread_csv_system_id = models.BooleanField(blank=True)
    spread_csv_dnsname = models.BooleanField(blank=True)
    spread_csv_domain = models.BooleanField(blank=True)
    spread_csv_systemstatus = models.BooleanField(blank=True)
    spread_csv_analysisstatus = models.BooleanField(blank=True)
    spread_csv_reason = models.BooleanField(blank=True)
    spread_csv_recommendation = models.BooleanField(blank=True)
    spread_csv_systemtype = models.BooleanField(blank=True)
    spread_csv_ip = models.BooleanField(blank=True)
    spread_csv_os = models.BooleanField(blank=True)
    spread_csv_company = models.BooleanField(blank=True)
    spread_csv_location = models.BooleanField(blank=True)
    spread_csv_serviceprovider = models.BooleanField(blank=True)
    spread_csv_tag = models.BooleanField(blank=True)
    spread_csv_case = models.BooleanField(blank=True)
    spread_csv_system_create_time = models.BooleanField(blank=True)
    spread_csv_system_modify_time = models.BooleanField(blank=True)

class SystemExporterSpreadsheetXlsConfigModel(models.Model):

    # primary key
    system_exporter_spreadsheet_xls_config_name = models.CharField(max_length=50, primary_key=True)

    # config fields
    spread_xls_system_id = models.BooleanField(blank=True)
    spread_xls_dnsname = models.BooleanField(blank=True)
    spread_xls_domain = models.BooleanField(blank=True)
    spread_xls_systemstatus = models.BooleanField(blank=True)
    spread_xls_analysisstatus = models.BooleanField(blank=True)
    spread_xls_reason = models.BooleanField(blank=True)
    spread_xls_recommendation = models.BooleanField(blank=True)
    spread_xls_systemtype = models.BooleanField(blank=True)
    spread_xls_ip = models.BooleanField(blank=True)
    spread_xls_os = models.BooleanField(blank=True)
    spread_xls_company = models.BooleanField(blank=True)
    spread_xls_location = models.BooleanField(blank=True)
    spread_xls_serviceprovider = models.BooleanField(blank=True)
    spread_xls_tag = models.BooleanField(blank=True)
    spread_xls_case = models.BooleanField(blank=True)
    spread_xls_system_create_time = models.BooleanField(blank=True)
    spread_xls_system_modify_time = models.BooleanField(blank=True)
    spread_xls_worksheet_systemstatus = models.BooleanField(blank=True)
    spread_xls_worksheet_analysisstatus = models.BooleanField(blank=True)
    spread_xls_worksheet_reason = models.BooleanField(blank=True)
    spread_xls_worksheet_recommendation = models.BooleanField(blank=True)
    spread_xls_worksheet_tag = models.BooleanField(blank=True)
