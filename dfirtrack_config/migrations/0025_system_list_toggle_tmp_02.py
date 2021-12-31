from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0024_system_list_toggle_tmp_01'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_artifact_closed',
            field=models.BooleanField(default=False),
        ),
    ]
