import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dfirtrack_main', '0013_case_attributes_default_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='case_id_external',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='case',
            name='case_modified_by_user_id',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='case_modified_by',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='case',
            name='case_modify_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='case',
            name='case_note_analysisresult',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='case_note_external',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='case_note_internal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='case_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='casepriority',
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.PROTECT,
                to='dfirtrack_main.casepriority',
            ),
        ),
        migrations.AddField(
            model_name='case',
            name='casestatus',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to='dfirtrack_main.casestatus',
            ),
        ),
        migrations.AddField(
            model_name='case',
            name='casetype',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='dfirtrack_main.casetype',
            ),
        ),
    ]
