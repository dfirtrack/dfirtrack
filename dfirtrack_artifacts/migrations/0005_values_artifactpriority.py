from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_artifacts', '0004_artifactpriority'),
    ]

    operations = [

        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactpriority (artifactpriority_name, artifactpriority_slug) VALUES ('01_low', '01_low');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactpriority (artifactpriority_name, artifactpriority_slug) VALUES ('02_medium', '02_medium');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactpriority (artifactpriority_name, artifactpriority_slug) VALUES ('03_high', '03_high');"),

    ]
