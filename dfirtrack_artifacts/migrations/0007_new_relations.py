from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dfirtrack_main', '0015_added_verbose_name_plural'),
        ('dfirtrack_artifacts', '0006_added_verbose_name_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='tag',
            field=models.ManyToManyField(
                blank=True, related_name='artifact_tag', to='dfirtrack_main.Tag'
            ),
        ),
    ]
