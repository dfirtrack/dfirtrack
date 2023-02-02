import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dfirtrack_main', '0024_user_assignment'),
        ('dfirtrack_config', '0022_capitalization_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_case',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='filter_assignment_view_case',
                to='dfirtrack_main.case',
            ),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_keep',
            field=models.BooleanField(default=True),
        ),
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
            name='filter_assignment_view_show_tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_task',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_tag',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='filter_assignment_view_tag',
                to='dfirtrack_main.tag',
            ),
        ),
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_user',
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='filter_assignment_view_tag',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
