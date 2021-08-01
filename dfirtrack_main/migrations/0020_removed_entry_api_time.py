from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0019_notestatus_values"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="entry",
            name="entry_api_time",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="entry_date",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="entry_system",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="entry_utc",
        ),
    ]
