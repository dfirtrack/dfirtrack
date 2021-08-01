from django.db import migrations
from django.utils.text import slugify


def insert_artifactpriorities(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Artifactpriority = apps.get_model('dfirtrack_artifacts', 'Artifactpriority')

    initial_values = [
        '10_low',
        '20_medium',
        '30_high',
    ]

    # We need to call slugify() here, because our own save() is not called by migrations!
    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Artifactpriority.objects.create(artifactpriority_name=name, artifactpriority_slug=slugify(name))

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_artifacts', '0004_artifactpriority'),
    ]

    operations = [
        migrations.RunPython(insert_artifactpriorities),
    ]
