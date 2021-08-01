from django.db import migrations


def insert_tagcolors(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Tagcolor = apps.get_model("dfirtrack_main", "Tagcolor")

    initial_values = [
        "black",
        "white",
    ]

    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Tagcolor.objects.create(tagcolor_name=name)


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0005_added_tag_note_and_user"),
    ]

    operations = [
        migrations.RunPython(insert_tagcolors),
    ]
