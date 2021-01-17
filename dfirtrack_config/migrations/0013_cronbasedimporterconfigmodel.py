from django.db import migrations
from dfirtrack import settings

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0012_cronbasedimporterconfig'),
    ]

    # PostgreSQL (uses TRUE / FALSE as boolean)
    if settings.DATABASES['default']['ENGINE'].split('.')[-1] == 'postgresql':

        operations = [

            migrations.RunSQL("INSERT INTO dfirtrack_config_systemimporterfilecsvcronbasedconfigmodel (system_importer_file_csv_cronbased_config_name, csv_column_system, csv_skip_existing_system, csv_headline, csv_import_path, csv_import_filename, csv_default_systemstatus_id, csv_default_analysisstatus_id, csv_choice_ip, csv_remove_ip, csv_choice_dnsname, csv_choice_domain, csv_choice_location, csv_choice_os, csv_choice_reason, csv_choice_recommendation, csv_choice_serviceprovider, csv_choice_systemtype, csv_choice_case, csv_remove_case, csv_choice_company, csv_remove_company, csv_choice_tag, csv_remove_tag) VALUES ('SystemImporterFileCsvCronbasedConfig', '1', FALSE, TRUE, '/tmp', 'systems.csv', '1', '1', FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, FALSE, TRUE, FALSE, FALSE);"),

        ]

    # SQLite3 (uses 1 / 0 as boolean)
    else:       # coverage: ignore branch

        operations = [

            migrations.RunSQL("INSERT INTO dfirtrack_config_systemimporterfilecsvcronbasedconfigmodel (system_importer_file_csv_cronbased_config_name, csv_column_system, csv_skip_existing_system, csv_headline, csv_import_path, csv_import_filename, csv_default_systemstatus_id, csv_default_analysisstatus_id, csv_choice_ip, csv_remove_ip, csv_choice_dnsname, csv_choice_domain, csv_choice_location, csv_choice_os, csv_choice_reason, csv_choice_recommendation, csv_choice_serviceprovider, csv_choice_systemtype, csv_choice_case, csv_remove_case, csv_choice_company, csv_remove_company, csv_choice_tag, csv_remove_tag) VALUES ('SystemImporterFileCsvCronbasedConfig', '1', 0, 1, '/tmp', 'systems.csv', '1', '1', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0);"),

        ]
