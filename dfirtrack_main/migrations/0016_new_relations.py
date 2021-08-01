import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_artifacts', '0007_new_relations'),
        ('dfirtrack_main', '0015_added_verbose_name_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='tag',
            field=models.ManyToManyField(blank=True, to='dfirtrack_main.Tag'),
        ),
        migrations.AddField(
            model_name='task',
            name='artifact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfirtrack_artifacts.artifact'),
        ),
        migrations.AddField(
            model_name='task',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfirtrack_main.case'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_is_abandoned',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfirtrack_main.system'),
        ),
    ]
