import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dfirtrack_main', '0017_simplify_system_times'),
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
        migrations.AddField(
            model_name='reportitem',
            name='case',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='dfirtrack_main.case',
            ),
        ),
        migrations.AddField(
            model_name='reportitem',
            name='tag',
            field=models.ManyToManyField(blank=True, to='dfirtrack_main.Tag'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_title', models.CharField(max_length=250, unique=True)),
                ('note_content', models.TextField()),
                ('note_version', models.IntegerField()),
                ('note_is_abandoned', models.BooleanField(blank=True, default=True)),
                ('note_create_time', models.DateTimeField(auto_now_add=True)),
                ('note_modify_time', models.DateTimeField(auto_now=True)),
                (
                    'case',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='dfirtrack_main.case',
                    ),
                ),
                (
                    'note_created_by_user_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='note_created_by',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'note_modified_by_user_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='note_modified_by',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'notestatus',
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to='dfirtrack_main.notestatus',
                    ),
                ),
                ('tag', models.ManyToManyField(blank=True, to='dfirtrack_main.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='reportitem',
            name='notestatus',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to='dfirtrack_main.notestatus',
            ),
        ),
    ]
