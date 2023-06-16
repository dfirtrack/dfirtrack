from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dfirtrack_config', '0024_system_list_toggle'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_assigned_to_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_created_by_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_modified_by_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_case_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_case_name',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_tag_all',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_system_assigned_to_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_system_created_by_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_system_modified_by_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_system_assigned_to_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_system_created_by_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_system_modified_by_user_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifactpriority',
            field=models.BooleanField(default=True),
        ),
    ]
