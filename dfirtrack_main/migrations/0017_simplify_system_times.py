from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0016_new_relations"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="system",
            name="system_api_time",
        ),
        migrations.AlterField(
            model_name="system",
            name="system_modify_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
