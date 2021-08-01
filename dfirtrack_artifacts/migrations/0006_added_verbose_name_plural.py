from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_artifacts", "0005_values_artifactpriority"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="artifactpriority",
            options={
                "ordering": ("artifactpriority_id",),
                "verbose_name_plural": "artifactpriorities",
            },
        ),
        migrations.AlterModelOptions(
            name="artifactstatus",
            options={
                "ordering": ("artifactstatus_id",),
                "verbose_name_plural": "artifactstatus",
            },
        ),
    ]
