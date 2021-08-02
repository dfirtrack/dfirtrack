from django.db import migrations
from django.utils.text import slugify


def insert_artifactstatus(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Artifactstatus = apps.get_model("dfirtrack_artifacts", "Artifactstatus")

    initial_values = [
        "10_needs_analysis",
        "20_requested",
        "21_requested_again",
        "25_collection_ongoing",
        "30_processing_ongoing",
        "40_import_ongoing",
        "50_ready_for_analysis",
        "60_analysis_ongoing",
        "70_analysis_finished",
        "90_not_analyzed",
        "95_not_available",
    ]

    # We need to call slugify() here, because our own save() is not called by migrations!
    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Artifactstatus.objects.create(
            artifactstatus_name=name, artifactstatus_slug=slugify(name)
        )


def insert_artifacttypes(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Artifacttype = apps.get_model("dfirtrack_artifacts", "Artifacttype")

    initial_values = [
        "File",
        "Image",
        "Information",
        "Triage",
    ]

    # We need to call slugify() here, because our own save() is not called by migrations!
    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Artifacttype.objects.create(
            artifacttype_name=name, artifacttype_slug=slugify(name)
        )


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_artifacts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(insert_artifactstatus),
        migrations.RunPython(insert_artifacttypes),
    ]
