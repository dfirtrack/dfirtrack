from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0025_assigned_users_tmp_01'),
    ]

    operations = [
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
    ]
