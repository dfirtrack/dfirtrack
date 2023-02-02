from django.db import migrations
from django.utils.text import slugify


def insert_casepriorities(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Casepriority = apps.get_model('dfirtrack_main', 'Casepriority')

    initial_values = [
        '10_low',
        '20_medium',
        '30_high',
    ]

    # We need to call slugify() here, because our own save() is not called by migrations!
    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Casepriority.objects.create(
            casepriority_name=name, casepriority_slug=slugify(name)
        )


def insert_casestatus(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Casestatus = apps.get_model('dfirtrack_main', 'Casestatus')

    initial_values = [
        '10_open',
        '20_ongoing',
        '30_closed',
    ]

    # We need to call slugify() here, because our own save() is not called by migrations!
    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Casestatus.objects.create(casestatus_name=name, casestatus_slug=slugify(name))


class Migration(migrations.Migration):
    dependencies = [
        ('dfirtrack_main', '0012_case_attributes'),
    ]

    operations = [
        migrations.RunPython(insert_casepriorities),
        migrations.RunPython(insert_casestatus),
    ]
