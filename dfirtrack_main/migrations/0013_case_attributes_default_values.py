from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0012_case_attributes'),
    ]

    operations = [

        migrations.RunSQL("INSERT INTO dfirtrack_main_casepriority (casepriority_name, casepriority_slug) VALUES ('10_low', '10_low');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_casepriority (casepriority_name, casepriority_slug) VALUES ('20_medium', '20_medium');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_casepriority (casepriority_name, casepriority_slug) VALUES ('30_high', '30_high');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_casestatus (casestatus_name, casestatus_slug) VALUES ('10_open', '10_open');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_casestatus (casestatus_name, casestatus_slug) VALUES ('20_ongoing', '20_ongoing');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_casestatus (casestatus_name, casestatus_slug) VALUES ('30_closed', '30_closed');"),

    ]
