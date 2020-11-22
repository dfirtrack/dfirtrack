from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_artifacts', '0004_artifactpriority'),
    ]

    operations = [

        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactpriority (artifactpriority_name, artifactpriority_slug) VALUES ('Low', 'low');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactpriority (artifactpriority_name, artifactpriority_slug) VALUES ('Medium', 'medium');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactpriority (artifactpriority_name, artifactpriority_slug) VALUES ('High', 'high');"),

    ]
