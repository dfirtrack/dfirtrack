from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0024_assignment_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfigmodel',
            name='filter_assignment_view_show_tag',
            field=models.BooleanField(default=True),
        ),
    ]
