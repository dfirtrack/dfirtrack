from django.db import migrations


def insert_analysisstatus(apps, schema_editor):
    # We can't import the migrated model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Analysisstatus = apps.get_model("dfirtrack_main", "Analysisstatus")

    initial_values = [
        "10_needs_analysis",
        "20_ready_for_analysis",
        "30_ongoing_analysis",
        "40_nothing_to_do",
    ]

    # We also do not make use of .objects.bulk_create() due to its known caveats, see:
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create
    for name in initial_values:
        Analysisstatus.objects.create(analysisstatus_name=name)


def insert_headlines(apps, schema_editor):
    Headline = apps.get_model("dfirtrack_main", "Headline")

    initial_values = [
        "Summary",
    ]

    for name in initial_values:
        Headline.objects.create(headline_name=name)


def insert_os(apps, schema_editor):
    Os = apps.get_model("dfirtrack_main", "Os")

    initial_values = [
        "Windows Server 2003",
        "Windows Server 2003 R2",
        "Windows Server 2008",
        "Windows Server 2008 R2",
        "Windows Server 2012",
        "Windows Server 2012 R2",
        "Windows Server 2016",
        "Windows XP",
        "Windows Vista",
        "Windows 7",
        "Windows 8",
        "Windows 8.1",
        "Windows 10",
        "tbd",
    ]

    for name in initial_values:
        Os.objects.create(os_name=name)


def insert_osarch(apps, schema_editor):
    Osarch = apps.get_model("dfirtrack_main", "Osarch")

    initial_values = [
        "32-Bit",
        "64-Bit",
    ]

    for name in initial_values:
        Osarch.objects.create(osarch_name=name)


def insert_systemstatus(apps, schema_editor):
    Systemstatus = apps.get_model("dfirtrack_main", "Systemstatus")

    initial_values = [
        "10_unknown",
        "20_analysis_ongoing",
        "30_compromised",
        "40_clean",
        "50_remediation_done",
        "60_reinstalled",
        "70_removed",
    ]

    for name in initial_values:
        Systemstatus.objects.create(systemstatus_name=name)


def insert_systemtypes(apps, schema_editor):
    Systemtype = apps.get_model("dfirtrack_main", "Systemtype")

    initial_values = [
        "Domaincontroller",
        "Mailserver",
        "Fileserver",
        "USB-Drive",
        "Client",
    ]

    for name in initial_values:
        Systemtype.objects.create(systemtype_name=name)


def insert_tagcolors(apps, schema_editor):
    Tagcolor = apps.get_model("dfirtrack_main", "Tagcolor")

    initial_values = [
        "primary",
        "green",
        "orange",
        "red",
    ]

    for name in initial_values:
        Tagcolor.objects.create(tagcolor_name=name)


def insert_taskpriorities(apps, schema_editor):
    Taskpriority = apps.get_model("dfirtrack_main", "Taskpriority")

    initial_values = [
        "10_low",
        "20_medium",
        "30_high",
    ]

    for name in initial_values:
        Taskpriority.objects.create(taskpriority_name=name)


def insert_taskstatus(apps, schema_editor):
    Taskstatus = apps.get_model("dfirtrack_main", "Taskstatus")

    initial_values = [
        "10_pending",
        "20_working",
        "30_done",
    ]

    for name in initial_values:
        Taskstatus.objects.create(taskstatus_name=name)


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(insert_analysisstatus),
        migrations.RunPython(insert_headlines),
        migrations.RunPython(insert_os),
        migrations.RunPython(insert_osarch),
        migrations.RunPython(insert_systemstatus),
        migrations.RunPython(insert_systemtypes),
        migrations.RunPython(insert_tagcolors),
        migrations.RunPython(insert_taskpriorities),
        migrations.RunPython(insert_taskstatus),
    ]
