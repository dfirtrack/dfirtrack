from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0023_assignment_view_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_artifact',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_case',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_note',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_reportitem',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_system',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_task',
            field=models.BooleanField(default=True),
        ),
    ]
