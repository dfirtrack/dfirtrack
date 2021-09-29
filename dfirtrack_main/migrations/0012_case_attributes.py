from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0011_removed_nullbooleanfields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casepriority',
            fields=[
                (
                    'casepriority_id',
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ('casepriority_name', models.CharField(max_length=255, unique=True)),
                ('casepriority_note', models.TextField(blank=True, null=True)),
                ('casepriority_slug', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('casepriority_id',),
            },
        ),
        migrations.CreateModel(
            name='Casestatus',
            fields=[
                ('casestatus_id', models.AutoField(primary_key=True, serialize=False)),
                ('casestatus_name', models.CharField(max_length=255, unique=True)),
                ('casestatus_note', models.TextField(blank=True, null=True)),
                ('casestatus_slug', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('casestatus_id',),
            },
        ),
        migrations.CreateModel(
            name='Casetype',
            fields=[
                ('casetype_id', models.AutoField(primary_key=True, serialize=False)),
                ('casetype_name', models.CharField(max_length=255, unique=True)),
                ('casetype_note', models.TextField(blank=True, null=True)),
                ('casetype_slug', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('casetype_id',),
            },
        ),
    ]
