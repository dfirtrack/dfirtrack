from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_config', '0021_user_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainconfigmodel',
            name='capitalization',
            field=models.CharField(
                choices=[
                    ('capitalization_keep', 'Keep notation'),
                    ('capitalization_lower', 'Convert to lower case'),
                    ('capitalization_upper', 'Convert to upper case'),
                ],
                default='capitalization_keep',
                max_length=50,
            ),
        ),
    ]
