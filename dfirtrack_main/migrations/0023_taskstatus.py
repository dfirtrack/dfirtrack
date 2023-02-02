from django.db import migrations


def insert_taskstatus(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Taskstatus = apps.get_model('dfirtrack_main', 'Taskstatus')

    initial_values = [
        '00_blocked',
        '40_skipped',
    ]

    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Taskstatus.objects.create(taskstatus_name=name)


class Migration(migrations.Migration):
    dependencies = [
        ('dfirtrack_main', '0022_model_update'),
    ]

    operations = [
        migrations.RunPython(insert_taskstatus),
    ]
