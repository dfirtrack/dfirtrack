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

class SystemExporterMarkdownConfigModel(models.Model):

    # primary key
    system_exporter_markdown_config_name = models.CharField(max_length=50, primary_key=True)

    # prepare choices
    DOMAINSORTED = 'dom'
    SYSTEMSORTED = 'sys'
    MARKDOWN_SORTING_CHOICES = [
        (DOMAINSORTED, 'Sorted by domain'),
        (SYSTEMSORTED, 'Sorted by system'),
    ]

    # config fields
    markdown_path = models.CharField(max_length=4096, blank=True, null=True)
    markdown_sorting = models.CharField(
        max_length = 3,
        choices = MARKDOWN_SORTING_CHOICES,
        default = SYSTEMSORTED,
    )

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

class SystemImporterFileCsvConfigbasedConfigModel(models.Model):

    # primary key
    system_importer_file_csv_configbased_config_name = models.CharField(max_length=50, primary_key=True)

    # config fields
    csv_skip_existing_system = models.BooleanField(blank=True)
    csv_column_system = models.IntegerField()
    csv_headline = models.BooleanField(blank=True)
    csv_choice_ip = models.BooleanField(blank=True)
    csv_remove_ip = models.BooleanField(blank=True)
    csv_column_ip = models.IntegerField()
    csv_remove_case = models.BooleanField(blank=True)
    csv_remove_company = models.BooleanField(blank=True)
    csv_remove_tag = models.BooleanField(blank=True)
    # TODO: find an alternative for the selection
    csv_default_systemstatus = models.IntegerField()
    csv_default_analysisstatus = models.IntegerField()
    csv_default_reason = models.IntegerField()
    csv_default_domain = models.IntegerField()
    csv_default_dnsname = models.IntegerField()
    csv_default_systemtype = models.IntegerField()
    csv_default_os = models.IntegerField()
    csv_default_location = models.IntegerField()
    csv_default_serviceprovider = models.IntegerField()
    csv_default_case = models.IntegerField()
    csv_default_company = models.IntegerField()
    csv_default_tag = models.IntegerField()

class SystemImporterFileCsvFormbasedConfigModel(models.Model):

    # primary key
    system_importer_file_csv_formbased_config_name = models.CharField(max_length=50, primary_key=True)

    # config fields
    csv_skip_existing_system = models.BooleanField(blank=True)
    csv_column_system = models.IntegerField()
    csv_headline = models.BooleanField(blank=True)
    csv_choice_ip = models.BooleanField(blank=True)
    csv_remove_ip = models.BooleanField(blank=True)
    csv_column_ip = models.IntegerField()
    csv_remove_case = models.BooleanField(blank=True)
    csv_remove_company = models.BooleanField(blank=True)
    csv_remove_tag = models.BooleanField(blank=True)
