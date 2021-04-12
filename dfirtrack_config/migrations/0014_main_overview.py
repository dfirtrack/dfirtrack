from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0013_csvimporterconfigmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainconfigmodel',
            name='main_overview',
            field=models.CharField(choices=[('main_overview_artifact', 'Artifact'), ('main_overview_case', 'Case'), ('main_overview_system', 'System'), ('main_overview_tag', 'Tag'), ('main_overview_task', 'Task')], default='main_overview_system', max_length=50),
        ),
    ]
