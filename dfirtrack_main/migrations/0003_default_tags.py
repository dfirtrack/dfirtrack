from django.db import migrations


def insert_tags(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Tag = apps.get_model("dfirtrack_main", "Tag")
    Tagcolor = apps.get_model("dfirtrack_main", "Tagcolor")

    initial_values = [
        ("Suspicious", "orange"),
        ("Backdoor installed", "red"),
        ("Credential harvesting", "red"),
        ("Data theft", "red"),
        ("Important", "red"),
    ]

    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name, color in initial_values:
        Tag.objects.create(
            tag_name=name, tagcolor=Tagcolor.objects.get(tagcolor_name=color)
        )


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0002_default_values"),
    ]

    operations = [
        migrations.RunPython(insert_tags),
    ]
