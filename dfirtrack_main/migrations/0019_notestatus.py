from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0018_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notestatus',
            fields=[
                ('notestatus_id', models.AutoField(primary_key=True, serialize=False)),
                ('notestatus_name', models.CharField(max_length=30, unique=True)),
                ('notestatus_note', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'notestatus',
            },
        ),
        migrations.RenameField(
            model_name='note',
            old_name='content',
            new_name='note_content',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='note_title',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='version',
            new_name='note_version',
        ),
        migrations.AddField(
            model_name='note',
            name='note_is_abandoned',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='note',
            name='notestatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dfirtrack_main.notestatus'),
        ),
    ]
