from django.db import migrations


def insert_status(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Systemstatus = apps.get_model("dfirtrack_main", "Systemstatus")
    Systemstatus.objects.create(systemstatus_name="90_not_analyzed")

    Analysisstatus = apps.get_model("dfirtrack_main", "Analysisstatus")
    Analysisstatus.objects.create(analysisstatus_name="50_main_analysis_finished")


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0006_tagcolors"),
    ]

    operations = [
        migrations.RunPython(insert_status),
    ]
