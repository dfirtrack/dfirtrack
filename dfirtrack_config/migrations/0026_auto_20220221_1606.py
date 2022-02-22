# Generated by Django 3.2.12 on 2022-02-21 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dfirtrack_main', '0024_user_assignment'),
        ('dfirtrack_config', '0025_auto_20220218_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_documentation_list_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filter_documentation_list_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userconfigmodel',
            name='filter_system_list_tag',
            field=models.ManyToManyField(blank=True, related_name='filter_system_list_tag', to='dfirtrack_main.Tag'),
        ),
        migrations.AlterField(
            model_name='userconfigmodel',
            name='filter_system_list_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filter_system_list_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
