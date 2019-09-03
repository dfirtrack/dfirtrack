from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_artifacts', '0001_initial'),
    ]

    operations = [

        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Needs analysis', 'open');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Requested from customer', 'requested');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Collecting through EDR', 'collecting');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Processing ongoing', 'processing');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Import ongoing', 'importing');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Ready for analysis', 'ready');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Analysis ongoing', 'ongoing');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Analysis finished', 'finished');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifactstatus (artifactstatus_name, artifactstatus_slug) VALUES ('Not available', 'unavailable');"),

        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifacttype (artifacttype_name, artifacttype_slug) VALUES ('Image', 'image');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifacttype (artifacttype_name, artifacttype_slug) VALUES ('File', 'file');"),
        migrations.RunSQL("INSERT INTO dfirtrack_artifacts_artifacttype (artifacttype_name, artifacttype_slug) VALUES ('Triage', 'triage');"),

    ]
