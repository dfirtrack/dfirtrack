from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0014_case_expansion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysisstatus',
            options={'verbose_name_plural': 'analysisstatus'},
        ),
        migrations.AlterModelOptions(
            name='casepriority',
            options={'ordering': ('casepriority_id',), 'verbose_name_plural': 'casepriorities'},
        ),
        migrations.AlterModelOptions(
            name='casestatus',
            options={'ordering': ('casestatus_id',), 'verbose_name_plural': 'casestatus'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterModelOptions(
            name='os',
            options={'verbose_name_plural': 'os'},
        ),
        migrations.AlterModelOptions(
            name='systemstatus',
            options={'verbose_name_plural': 'systemstatus'},
        ),
    ]
