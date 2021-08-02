from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_config", "0019_default_configs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="systemexportermarkdownconfigmodel",
            name="markdown_path",
            field=models.CharField(max_length=4096, null=True),
        ),
    ]
