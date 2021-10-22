# Generated by Django 2.2.5 on 2019-09-07 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0009_export_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='previous_analysisstatus',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='previous_analysisstatus',
                to='dfirtrack_main.Analysisstatus',
            ),
        ),
        migrations.AddField(
            model_name='system',
            name='previous_systemstatus',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='previous_systemstatus',
                to='dfirtrack_main.Systemstatus',
            ),
        ),
        migrations.AlterField(
            model_name='system',
            name='analysisstatus',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='analysisstatus',
                to='dfirtrack_main.Analysisstatus',
            ),
        ),
        migrations.AlterField(
            model_name='system',
            name='systemstatus',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='systemstatus',
                to='dfirtrack_main.Systemstatus',
            ),
        ),
        migrations.CreateModel(
            name='Systemhistory',
            fields=[
                (
                    'systemhistory_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ('systemhistory_type', models.CharField(max_length=30)),
                ('systemhistory_old_value', models.CharField(max_length=30)),
                ('systemhistory_new_value', models.CharField(max_length=30)),
                ('systemhistory_time', models.DateTimeField(auto_now_add=True)),
                (
                    'system',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='dfirtrack_main.System',
                    ),
                ),
            ],
        ),
    ]
