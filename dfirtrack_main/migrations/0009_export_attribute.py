# Generated by Django 2.0 on 2019-06-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dfirtrack_main', '0008_rebuild_domain_and_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='system_export_markdown',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='system',
            name='system_export_spreadsheet',
            field=models.BooleanField(default=True),
        ),
    ]
