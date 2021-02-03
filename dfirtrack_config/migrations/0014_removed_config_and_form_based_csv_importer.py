from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0013_csvimporterconfigmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_analysisstatus',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_case',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_company',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_dnsname',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_domain',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_location',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_os',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_reason',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_serviceprovider',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_systemstatus',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_systemtype',
        ),
        migrations.RemoveField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_tag',
        ),
        migrations.DeleteModel(
            name='SystemImporterFileCsvFormbasedConfigModel',
        ),
        migrations.DeleteModel(
            name='SystemImporterFileCsvConfigbasedConfigModel',
        ),
    ]
