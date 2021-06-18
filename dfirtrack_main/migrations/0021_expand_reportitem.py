from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0020_notestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportitem',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dfirtrack_main.case'),
        ),
        migrations.AddField(
            model_name='reportitem',
            name='notestatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dfirtrack_main.notestatus'),
        ),
        migrations.AddField(
            model_name='reportitem',
            name='tag',
            field=models.ManyToManyField(blank=True, to='dfirtrack_main.Tag'),
        ),
    ]
