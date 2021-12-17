from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dfirtrack_artifacts', '0007_new_relations'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='artifact_assigned_to_user_id',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='artifact_assigned_to',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
