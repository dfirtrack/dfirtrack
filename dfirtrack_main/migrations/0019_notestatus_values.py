from django.db import migrations


def insert_notestatus(apps, schema_editor):
    Notestatus = apps.get_model('dfirtrack_main', 'Notestatus')

    initial_values = [
        '10_draft',
        '20_ready_for_review',
        '30_review',
        '40_final',
    ]

    for name in initial_values:
        Notestatus.objects.create(notestatus_name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0018_note_and_notestatus'),
    ]

    operations = [
        migrations.RunPython(insert_notestatus),
    ]
