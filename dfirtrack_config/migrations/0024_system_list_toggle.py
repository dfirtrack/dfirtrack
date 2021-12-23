from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0023_user_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_analystmemo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_artifact',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_company_information',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_reportitem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_systemuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_task',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_task_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_technical_information',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_timeline',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_system_detail_show_virtualization_information',
            field=models.BooleanField(default=False),
        ),
    ]
