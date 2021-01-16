from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0011_removed_nullbooleanfields'),
        ('dfirtrack_config', '0011_cron_variables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_case',
            field=models.ManyToManyField(blank=True, related_name='system_importer_file_csv_configbased_config_case', to='dfirtrack_main.Case'),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_company',
            field=models.ManyToManyField(blank=True, related_name='system_importer_file_csv_configbased_config_company', to='dfirtrack_main.Company'),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigbasedconfigmodel',
            name='csv_default_tag',
            field=models.ManyToManyField(blank=True, related_name='system_importer_file_csv_configbased_config_tag', to='dfirtrack_main.Tag'),
        ),
        migrations.CreateModel(
            name='SystemImporterFileCsvCronbasedConfigModel',
            fields=[
                ('system_importer_file_csv_cronbased_config_name', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False)),
                ('csv_column_system', models.IntegerField()),
                ('csv_skip_existing_system', models.BooleanField(blank=True)),
                ('csv_headline', models.BooleanField(blank=True)),
                ('csv_import_path', models.CharField(default='/tmp', max_length=4096)),
                ('csv_import_filename', models.CharField(default='systems.csv', max_length=255)),
                ('csv_import_username', models.CharField(default='cron', max_length=255)),
                ('csv_choice_ip', models.BooleanField(blank=True)),
                ('csv_column_ip', models.IntegerField()),
                ('csv_remove_ip', models.BooleanField(blank=True)),
                ('csv_choice_dnsname', models.BooleanField(blank=True)),
                ('csv_column_dnsname', models.IntegerField()),
                ('csv_choice_domain', models.BooleanField(blank=True)),
                ('csv_column_domain', models.IntegerField()),
                ('csv_choice_location', models.BooleanField(blank=True)),
                ('csv_column_location', models.IntegerField()),
                ('csv_choice_os', models.BooleanField(blank=True)),
                ('csv_column_os', models.IntegerField()),
                ('csv_choice_reason', models.BooleanField(blank=True)),
                ('csv_column_reason', models.IntegerField()),
                ('csv_choice_recommendation', models.BooleanField(blank=True)),
                ('csv_column_recommendation', models.IntegerField()),
                ('csv_choice_serviceprovider', models.BooleanField(blank=True)),
                ('csv_column_serviceprovider', models.IntegerField()),
                ('csv_choice_systemtype', models.BooleanField(blank=True)),
                ('csv_column_systemtype', models.IntegerField()),
                ('csv_choice_case', models.BooleanField(blank=True)),
                ('csv_column_case', models.IntegerField()),
                ('csv_remove_case', models.BooleanField(blank=True)),
                ('csv_choice_company', models.BooleanField(blank=True)),
                ('csv_column_company', models.IntegerField()),
                ('csv_remove_company', models.BooleanField(blank=True)),
                ('csv_choice_tag', models.BooleanField(blank=True)),
                ('csv_column_tag', models.IntegerField()),
                ('csv_remove_tag', models.BooleanField(blank=True)),
                ('csv_default_analysisstatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='system_importer_file_csv_cronbased_config_analysisstatus', to='dfirtrack_main.analysisstatus')),
                ('csv_default_case', models.ManyToManyField(blank=True, related_name='system_importer_file_csv_cronbased_config_case', to='dfirtrack_main.Case')),
                ('csv_default_company', models.ManyToManyField(blank=True, related_name='system_importer_file_csv_cronbased_config_company', to='dfirtrack_main.Company')),
                ('csv_default_dnsname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_dnsname', to='dfirtrack_main.dnsname')),
                ('csv_default_domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_domain', to='dfirtrack_main.domain')),
                ('csv_default_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_location', to='dfirtrack_main.location')),
                ('csv_default_os', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_os', to='dfirtrack_main.os')),
                ('csv_default_reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_reason', to='dfirtrack_main.reason')),
                ('csv_default_recommendation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_recommendation', to='dfirtrack_main.recommendation')),
                ('csv_default_serviceprovider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_serviceprovider', to='dfirtrack_main.serviceprovider')),
                ('csv_default_systemstatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='system_importer_file_csv_cronbased_config_systemstatus', to='dfirtrack_main.systemstatus')),
                ('csv_default_systemtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='system_importer_file_csv_cronbased_config_systemtype', to='dfirtrack_main.systemtype')),
                ('csv_default_tag', models.ManyToManyField(blank=True, related_name='system_importer_file_csv_cronbased_config_tag', to='dfirtrack_main.Tag')),
            ],
        ),
    ]
