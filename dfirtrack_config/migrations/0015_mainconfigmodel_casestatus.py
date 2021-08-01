from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0014_case_expansion"),
        ("dfirtrack_config", "0014_main_overview"),
    ]

    operations = [
        migrations.AddField(
            model_name="mainconfigmodel",
            name="casestatus_end",
            field=models.ManyToManyField(
                blank=True,
                related_name="main_config_casestatus_end",
                to="dfirtrack_main.Casestatus",
            ),
        ),
        migrations.AddField(
            model_name="mainconfigmodel",
            name="casestatus_open",
            field=models.ManyToManyField(
                blank=True,
                related_name="main_config_casestatus_open",
                to="dfirtrack_main.Casestatus",
            ),
        ),
        migrations.AddField(
            model_name="mainconfigmodel",
            name="casestatus_start",
            field=models.ManyToManyField(
                blank=True,
                related_name="main_config_casestatus_start",
                to="dfirtrack_main.Casestatus",
            ),
        ),
    ]
