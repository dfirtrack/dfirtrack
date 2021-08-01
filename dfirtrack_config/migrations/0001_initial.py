import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dfirtrack_artifacts", "0002_default_values"),
        ("dfirtrack_main", "0010_status_history_for_system"),
    ]

    operations = [
        migrations.CreateModel(
            name="SystemExporterMarkdownConfigModel",
            fields=[
                (
                    "system_exporter_markdown_config_name",
                    models.CharField(
                        editable=False, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                (
                    "markdown_path",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                (
                    "markdown_sorting",
                    models.CharField(
                        choices=[
                            ("dom", "Sorted by domain"),
                            ("sys", "Sorted by system"),
                        ],
                        default="sys",
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SystemExporterSpreadsheetCsvConfigModel",
            fields=[
                (
                    "system_exporter_spreadsheet_csv_config_name",
                    models.CharField(
                        editable=False, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                ("spread_csv_system_id", models.BooleanField(blank=True)),
                ("spread_csv_dnsname", models.BooleanField(blank=True)),
                ("spread_csv_domain", models.BooleanField(blank=True)),
                ("spread_csv_systemstatus", models.BooleanField(blank=True)),
                ("spread_csv_analysisstatus", models.BooleanField(blank=True)),
                ("spread_csv_reason", models.BooleanField(blank=True)),
                ("spread_csv_recommendation", models.BooleanField(blank=True)),
                ("spread_csv_systemtype", models.BooleanField(blank=True)),
                ("spread_csv_ip", models.BooleanField(blank=True)),
                ("spread_csv_os", models.BooleanField(blank=True)),
                ("spread_csv_company", models.BooleanField(blank=True)),
                ("spread_csv_location", models.BooleanField(blank=True)),
                ("spread_csv_serviceprovider", models.BooleanField(blank=True)),
                ("spread_csv_tag", models.BooleanField(blank=True)),
                ("spread_csv_case", models.BooleanField(blank=True)),
                ("spread_csv_system_create_time", models.BooleanField(blank=True)),
                ("spread_csv_system_modify_time", models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="SystemExporterSpreadsheetXlsConfigModel",
            fields=[
                (
                    "system_exporter_spreadsheet_xls_config_name",
                    models.CharField(
                        editable=False, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                ("spread_xls_system_id", models.BooleanField(blank=True)),
                ("spread_xls_dnsname", models.BooleanField(blank=True)),
                ("spread_xls_domain", models.BooleanField(blank=True)),
                ("spread_xls_systemstatus", models.BooleanField(blank=True)),
                ("spread_xls_analysisstatus", models.BooleanField(blank=True)),
                ("spread_xls_reason", models.BooleanField(blank=True)),
                ("spread_xls_recommendation", models.BooleanField(blank=True)),
                ("spread_xls_systemtype", models.BooleanField(blank=True)),
                ("spread_xls_ip", models.BooleanField(blank=True)),
                ("spread_xls_os", models.BooleanField(blank=True)),
                ("spread_xls_company", models.BooleanField(blank=True)),
                ("spread_xls_location", models.BooleanField(blank=True)),
                ("spread_xls_serviceprovider", models.BooleanField(blank=True)),
                ("spread_xls_tag", models.BooleanField(blank=True)),
                ("spread_xls_case", models.BooleanField(blank=True)),
                ("spread_xls_system_create_time", models.BooleanField(blank=True)),
                ("spread_xls_system_modify_time", models.BooleanField(blank=True)),
                ("spread_xls_worksheet_systemstatus", models.BooleanField(blank=True)),
                (
                    "spread_xls_worksheet_analysisstatus",
                    models.BooleanField(blank=True),
                ),
                ("spread_xls_worksheet_reason", models.BooleanField(blank=True)),
                (
                    "spread_xls_worksheet_recommendation",
                    models.BooleanField(blank=True),
                ),
                ("spread_xls_worksheet_tag", models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="SystemImporterFileCsvFormbasedConfigModel",
            fields=[
                (
                    "system_importer_file_csv_formbased_config_name",
                    models.CharField(
                        editable=False, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                ("csv_skip_existing_system", models.BooleanField(blank=True)),
                ("csv_column_system", models.IntegerField()),
                ("csv_headline", models.BooleanField(blank=True)),
                ("csv_choice_ip", models.BooleanField(blank=True)),
                ("csv_remove_ip", models.BooleanField(blank=True)),
                ("csv_column_ip", models.IntegerField()),
                ("csv_remove_case", models.BooleanField(blank=True)),
                ("csv_remove_company", models.BooleanField(blank=True)),
                ("csv_remove_tag", models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="SystemImporterFileCsvConfigbasedConfigModel",
            fields=[
                (
                    "system_importer_file_csv_configbased_config_name",
                    models.CharField(
                        editable=False, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                ("csv_skip_existing_system", models.BooleanField(blank=True)),
                ("csv_column_system", models.IntegerField()),
                ("csv_headline", models.BooleanField(blank=True)),
                ("csv_choice_ip", models.BooleanField(blank=True)),
                ("csv_remove_ip", models.BooleanField(blank=True)),
                ("csv_column_ip", models.IntegerField()),
                ("csv_remove_case", models.BooleanField(blank=True)),
                ("csv_remove_company", models.BooleanField(blank=True)),
                ("csv_remove_tag", models.BooleanField(blank=True)),
                (
                    "csv_default_analysisstatus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="system_importer_file_csv_configbased_config_analysisstatus",
                        to="dfirtrack_main.Analysisstatus",
                    ),
                ),
                (
                    "csv_default_case",
                    models.ManyToManyField(
                        blank=True,
                        related_name="artifact_exporter_spreadsheet_xls_config_case",
                        to="dfirtrack_main.Case",
                    ),
                ),
                (
                    "csv_default_company",
                    models.ManyToManyField(
                        blank=True,
                        related_name="artifact_exporter_spreadsheet_xls_config_company",
                        to="dfirtrack_main.Company",
                    ),
                ),
                (
                    "csv_default_dnsname",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_dnsname",
                        to="dfirtrack_main.Dnsname",
                    ),
                ),
                (
                    "csv_default_domain",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_domain",
                        to="dfirtrack_main.Domain",
                    ),
                ),
                (
                    "csv_default_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_location",
                        to="dfirtrack_main.Location",
                    ),
                ),
                (
                    "csv_default_os",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_os",
                        to="dfirtrack_main.Os",
                    ),
                ),
                (
                    "csv_default_reason",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_reason",
                        to="dfirtrack_main.Reason",
                    ),
                ),
                (
                    "csv_default_serviceprovider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_serviceprovider",
                        to="dfirtrack_main.Serviceprovider",
                    ),
                ),
                (
                    "csv_default_systemstatus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="system_importer_file_csv_configbased_config_systemstatus",
                        to="dfirtrack_main.Systemstatus",
                    ),
                ),
                (
                    "csv_default_systemtype",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="system_importer_file_csv_configbased_config_systemtype",
                        to="dfirtrack_main.Systemtype",
                    ),
                ),
                (
                    "csv_default_tag",
                    models.ManyToManyField(
                        blank=True,
                        related_name="artifact_exporter_spreadsheet_xls_config_tag",
                        to="dfirtrack_main.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ArtifactExporterSpreadsheetXlsConfigModel",
            fields=[
                (
                    "artifact_exporter_spreadsheet_xls_config_name",
                    models.CharField(
                        editable=False, max_length=50, primary_key=True, serialize=False
                    ),
                ),
                ("artifactlist_xls_artifact_id", models.BooleanField(blank=True)),
                ("artifactlist_xls_system_id", models.BooleanField(blank=True)),
                ("artifactlist_xls_system_name", models.BooleanField(blank=True)),
                ("artifactlist_xls_artifactstatus", models.BooleanField(blank=True)),
                ("artifactlist_xls_artifacttype", models.BooleanField(blank=True)),
                (
                    "artifactlist_xls_artifact_source_path",
                    models.BooleanField(blank=True),
                ),
                (
                    "artifactlist_xls_artifact_storage_path",
                    models.BooleanField(blank=True),
                ),
                ("artifactlist_xls_artifact_note", models.BooleanField(blank=True)),
                ("artifactlist_xls_artifact_md5", models.BooleanField(blank=True)),
                ("artifactlist_xls_artifact_sha1", models.BooleanField(blank=True)),
                ("artifactlist_xls_artifact_sha256", models.BooleanField(blank=True)),
                (
                    "artifactlist_xls_artifact_create_time",
                    models.BooleanField(blank=True),
                ),
                (
                    "artifactlist_xls_artifact_modify_time",
                    models.BooleanField(blank=True),
                ),
                (
                    "artifactlist_xls_worksheet_artifactstatus",
                    models.BooleanField(blank=True),
                ),
                (
                    "artifactlist_xls_worksheet_artifacttype",
                    models.BooleanField(blank=True),
                ),
                (
                    "artifactlist_xls_choice_artifactstatus",
                    models.ManyToManyField(
                        related_name="artifact_exporter_spreadsheet_xls_config_artifactstatus",
                        to="dfirtrack_artifacts.Artifactstatus",
                    ),
                ),
            ],
        ),
    ]
